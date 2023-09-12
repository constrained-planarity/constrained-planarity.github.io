---
title: Level Planarity
complexity: P
reduces_to:
  'proper-cl': '[@dloz-pgw-15, Theorem 7.4]'
  'strip': '[@dloz-pgw-15, Theorem 9.3]'
  'radial-level': '[@sch-tat-13, Lemma 6.12]'
image: ../graphics/level.svg
---

# Definition

:::{.column-margin}
![](../graphics/level.svg){width=100%}
:::

A graph is level planar if it can be embedded in the plane such that no two edges
cross and the vertices lie on some prescribed horizontal lines.

Formally, in Level Planarity, the directed graph $G=(V,E)$ is equipped with a function $\gamma : V \mapsto
\{1,2,\ldots,k\}$ with
$k\in\mathbb{N}$ such that for every edge $(u,v)\in E$ it is $\gamma(u)<\gamma(v)$.
The level graph is called *proper* if it is $\gamma(u)+1=\gamma(v)$ for every edge.
With $V_i=\gamma^{-1}(i)$ we denote all vertices on level $i$.
A level planar drawing maps all vertices $v\in V_I$ of a level $i$ to a point on the line $y=i$ such that every edge is
y-monotone and no two edges cross.
A level graph is level planar if it admits a level planar drawing.

# Complexity

@jlm-lpt-98 give a linear-time algorithm for testing level planarity.
While the dissertation by @lei-lpt-98 describes a prototypical implementation, no implementations exist of this
algorithm.
@brue-pvf-21 gives an alternative linear-time algorithms and points out some issues with the algorithm by @jlm-lpt-98.
Simpler algorithms with a super-linear runtime have been proposed [@hh-plp-07;@rsb-asf-01;@brs-lpt-22;@fpss-hmd-12].
For these, we could only find an implementation by @efk-gat-10 for the quadratic algorithm by @hh-plp-07.

# Related Problems

Trivially reduces to $proper-cl by making the instances proper (i.e., inserting subdivision vertices on edges spanning
multiple levels) and adding all vertices to the same (root-)cluster [@dloz-pgw-15, Theorem 7.4].

Reduces to $strip by converting each level to three strips and subdividing the edges
appropriately [@dloz-pgw-15, Theorem 9.3].

Reduces to $radial-level by adding a single edge that spans from the lowest to the highest level,
at which the radial drawing can be cut to a planar one [@sch-tat-13, Lemma 6.12].

# See Also

- Planarity Variants for Directed Graphs @brue-pvf-21