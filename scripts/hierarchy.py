#!/usr/bin/env python3
from panflute import convert_text

from scripts.parse import problems


# import sys
# print("v1", file=sys.stderr)

def no_dash(s):
    if isinstance(s, str):
        return s.replace("-", "")
    else:
        return [no_dash(i) for i in s]


def mermaid():
    print("flowchart TB")
    for k, p in problems.items():
        print(f"\t{k}[\"{p['label_wrapped']}\"]" + (" --> " if p["reduces_to"] else "") + " & ".join(p["reduces_to"]) + ";")


def dot_node(k, p):
    return f"""{no_dash(k)} [label="{p['label_wrapped']}", href="/problems/{k}.html"];"""


def parse_cite(c):
    lines = convert_text(c, output_format="plain", extra_args=["--bibliography", "references.bib", "--citeproc"])
    return lines.splitlines()[0]


def dot():
    print("digraph G {")
    print("\tconcentrate=true;")
    print("\tfontname=\"'Source Sans Pro', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif\";")
    print("\tfontsize=18;")
    print("\tlheight=0;")
    print("\tnode [fontname=\"'Source Sans Pro', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif\", fillcolor=\"white\", style=\"filled\"];")
    for t in ["P", "?", "NPC"]:
        if t == "?":
            print(f"\tsubgraph cluster_X {{")
        else:
            print(f"\tsubgraph cluster_{t} {{")
        print(f"\t\tlabel=\"{t}\";")
        print(f"\t\tlabeljust=r;")

        for k, p in problems.items():
            if p["complexity"] != t: continue
            if not p["same_repr"]: continue
            if p["same_dedup"]:
                print(f"\t\tsubgraph cluster_{no_dash(k)} {{")
                print(f"\t\t\tlabel=\"\";")
                print(f"\t\t\tstyle=\"invis\";")
                print(f"\t\t\t{{ rank=same {no_dash(k)} {' '.join(no_dash(p['same_dedup']))} }}")
                print("\t\t\t" + dot_node(k, p))
                for r in p['same_dedup']:
                    print("\t\t\t" + dot_node(r, problems[r]))
                print("\t\t}")
            else:
                print("\t\t" + dot_node(k, p))
        print("\t}")
    print()
    for k, p in problems.items():
        for a in p["above"]:
            props = ""
            # if isinstance(problems[k]["reduces_to"], dict):
            #     props = " [label=\"" + parse_cite(problems[k]["reduces_to"][a]) + "\"]"
            print(f"\t{no_dash(k)} -> {{ " + no_dash(a) + " }" + props + ";")
        if p["same_dedup"]:
            print(f"\t{no_dash(k)} -> {{ " + " , ".join(no_dash(p['same_dedup'])) + " } " +
                  "[dir=none, constraint=false, color=\"black:invis:black\"];")

        # if p["reduces_to"]:
        #     print(f"\t{k.replace('-','')} -> {{ " + " , ".join(s.replace('-','') for s in p["reduces_to"]) + " };")
    print("}")


def ogdf():
    from ogdf_python import ogdf, cppinclude
    cppinclude("ogdf/layered/SugiyamaLayout.h")

    G = ogdf.Graph()
    GA = ogdf.GraphAttributes(G, ogdf.GraphAttributes.all)

    for k, p in problems.items():
        p["n"] = G.newNode()
        GA.label[p["n"]] = p['label']

    for k, p in problems.items():
        for r in p["reduces_to"]:
            G.newEdge(p["n"], problems[r]["n"])

    SL = ogdf.SugiyamaLayout()
    SL.call(GA)
    ogdf.GraphIO.drawSVG(GA, "hierarchy.svg")


if __name__ == "__main__":
    dot()
    ogdf()
