---
title: Partially Embedded Planarity
complexity: P
reduces_to:
  'clustered': '[@diss]'
---

# Definition

In Partially Embedded Planarity we are given a prescribed planar drawing of a subgraph and want to know whether this
drawing can be planarly extended by adding some further edges.

Formally, the undirected graph $G=(V,E)$ is accompanied by a *prescribed* subgraph $H$ for which
a planar embedding $\mathcal H$ is given.
The triplet $(G, H, \mathcal H)$ is often called *partially embedded graph (PEG)*.
We call a planar embedding $\mathcal G$ of $G$ an *extension* of the embedding $\mathcal H$ of $H$ if the restriction of
$\mathcal G$ to $H$ coincides with $\mathcal H$.
The problem Partially Embedded Planarity asks whether such an extension exists for a PEG.

# Complexity

@abf-tpo-15 give a linear-time algorithm for testing Partially Embedded Planarity.
A simpler linear-time algorithm is given by @frs-asp-23.

# Related Problems

The problem can reduced to $clustered by fixing the embedding of $\mathcal H$ using wheels and using clusters to
fix the endpoints of the edges of $G\setminus H$ to their vertices and to ensure that these edges are embedded in the
correct faces [@diss].

Schaefer gives a reduction to $sefe-2, where $G$ constitutes the one exclusive graph and the other exclusive graph is
obtained by triangulating $\mathcal H$ [@sch-tat-13, Theorem 6.2.].