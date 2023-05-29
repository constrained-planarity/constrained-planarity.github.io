#!/usr/bin/env python3
import os
import sys

os.chdir(os.path.normpath(__file__ + "/../.."))
sys.path.append(os.getcwd())

from panflute import *

from scripts.parse import problems


def replace_problem_ref(elem, doc):
    if type(elem) == Str and elem.text.startswith("$"):
        key = elem.text[1:]
        if key not in problems: return
        prob = problems[key]
        return Link(Str(prob["title"]), url=f"/problems/{key}.html")


def main(doc=None):
    return run_filter(replace_problem_ref, doc=doc)


if __name__ == "__main__":
    main()
