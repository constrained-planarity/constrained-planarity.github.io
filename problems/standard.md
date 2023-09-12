---
title: (Standard) Planarity
complexity: P
reduces_to:
  'level': '[@sch-tat-13]'
  'part-2-page': '[@sch-tat-13]'
  'ec': '[@sch-tat-13]'
  'part-rot': '[@sch-tat-13]'
  'partial': '[@sch-ppe-14]'
---

# Definition

A graph is planar if it can be embedded in the plane such that no two edges cross.

# Complexity

Planarity can be solved in linear time, see [@pat-pta-13] and the
corresponding [Wikipedia Article](https://en.wikipedia.org/wiki/Planarity_testing) for a historic overview over the
various solution.
@ht-pav-08 and @bra-tlr-09 give very accessible descriptions of the state-of-the art planarity tests.

# Related Problems

- Reduces to $level [@sch-tat-13]?
- Reduces to $part-2-page [@sch-tat-13]?
- Trivially reduces to $ec by using an empty constraint set [@sch-tat-13].
- Trivially reduces to $part-rot by using an empty contraint set [@sch-tat-13].
- Reduces to $partial [@sch-ppe-14]?

# See also

- Planar Graphs: Theory and Algorithms [@nc-pg-88]
- Handbook on Graph Drawing and Visualization [@pat-pta-13]
- [Wikipedia Article](https://en.wikipedia.org/wiki/Planar_graph)
- [Information System on Graph Classes and their Inclusions Entry](https://www.graphclasses.org/classes/gc_43.html)