# -*- coding: utf-8 -*-
"""Repair unescaped straight double quotes inside double-quoted strings in
scripts/content_pages.py by replacing them with typographic quotes.

Rule: while inside a "..." string, a quote only closes the string if the next
non-space character is one of , ] } ) or end of line/file. Otherwise it is an
author typo and becomes a curly quote.
"""
import io, re, sys

PATH = "scripts/content_pages.py"
src = io.open(PATH, encoding="utf-8").read()

# flatten away escaped quotes so we do not touch them
SENT = "\x00"
work = src.replace('\\"', SENT)

out = []
in_str = False
i = 0
flip = 0
fixes = 0
n = len(work)
while i < n:
    ch = work[i]
    if work.startswith('"""', i) and not in_str:
        # skip a triple-quoted block untouched
        k = work.find('"""', i + 3)
        if k == -1:
            k = n - 3
        out.append(work[i:k+3])
        i = k + 3
        continue
    if ch == '"':
        if not in_str:
            in_str = True
            out.append(ch)
            i += 1
            continue
        # inside a string: decide
        j = i + 1
        while j < n and work[j] in " \t":
            j += 1
        if j >= n or work[j] in ",]})\n:" or work[j] == "#":
            in_str = False
            out.append(ch)
        else:
            out.append("\u201c" if flip % 2 == 0 else "\u201d")
            flip += 1
            fixes += 1
        i += 1
        continue
    if ch == "\n":
        in_str = False
    elif in_str:
        pass
    out.append(ch)
    i += 1

res = "".join(out).replace(SENT, '\\"')
io.open(PATH, "w", encoding="utf-8").write(res)
print("inner quotes repaired:", fixes)
