#!/usr/bin/env python3

import os
import textwrap

import frontmatter
import more_itertools
from pylatexenc.latex2text import LatexNodes2Text

latex = LatexNodes2Text()


def get_meta(file):
    key = file.removesuffix(".md")
    meta = frontmatter.load("problems/" + file).to_dict()
    meta["key"] = key
    if meta["reduces_to"] == [""]:
        meta["reduces_to"] = []
    meta["label"] = latex.latex_to_text(meta['title'])
    meta["label_wrapped"] = "\\n".join(textwrap.wrap(meta["label"], 10, break_long_words=False))
    return key, meta


problems = dict(
    get_meta(file)
    for file in os.listdir("problems")
    if not file.startswith("_") and file.endswith(".md")
)

for key, meta in problems.items():
    meta["above"], meta["same"] = map(list, more_itertools.partition((lambda r: key in problems[r]["reduces_to"]), meta["reduces_to"]))
    meta["same_repr"] = all(key < r for r in meta["same"])
    meta["same_dedup"] = [r for r in meta["same"] if key < r]
