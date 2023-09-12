#!/usr/bin/env python3
import os
import sys

from more_itertools import one

os.chdir(os.path.normpath(__file__ + "/../.."))
sys.path.append(os.getcwd())

from panflute import *

from scripts.parse import problems


def replace_problem_ref(elem, doc):
    if type(elem) == Str and elem.text.startswith("$"):
        key = elem.text[1:]
        if key not in problems:
            print(f"Problem {key!r} unknown!", file=sys.stderr)
        prob = problems[key]
        para = one(convert_text(f"[{prob['title']}](/problems/{key}.html)"))
        return para.content[0]


def main(doc=None):
    return run_filter(replace_problem_ref, doc=doc)


if __name__ == "__main__":
    main()
