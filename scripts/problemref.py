#!/usr/bin/env python3
import os
import re
import sys

from more_itertools import one

os.chdir(os.path.normpath(__file__ + "/../.."))
sys.path.append(os.getcwd())

from panflute import *

from scripts.parse import problems

PATTERN = "^\\$([A-Za-z0-9-]+)"


def replace_problem_ref(elem, doc):
    if type(elem) == Str and elem.text.startswith("$"):
        m = re.match(PATTERN, elem.text)
        if not m:
            print(f"Weird $-string {elem}", file=sys.stderr)
            return
        key = m.group(1)
        if key not in problems:
            print(f"Problem {key!r} unknown!", file=sys.stderr)
            return
        prob = problems[key]
        repl = f"[{prob['title']}](/problems/{key}.html)".replace("\\", "\\\\")
        md = re.sub(PATTERN, repl, elem.text)
        para = one(convert_text(md))
        return Span(*para.content)


def main(doc=None):
    return run_filter(replace_problem_ref, doc=doc)


if __name__ == "__main__":
    main()
