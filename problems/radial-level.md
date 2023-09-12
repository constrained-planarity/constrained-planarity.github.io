---
title: Radial Level Planarity
complexity: P
reduces_to:
  'clustered': '[@sch-tat-13, Lemma 6.18]'
---

# Definition

Radial Level Planarity is a generalization of $level where levels are not represented by axis-parallel lines, but by concentric rings.
Equivalently, this can be seen as drawing the horizontal levels on a standing torus instead of in the plane.

# Complexity

Testing level planarity can be reduced to the radial variant by introducing an edge from the lowest to the highest level, at which the cylinder can be cut to transform a radial solution back into the plane.
Bachmaier et al. give a linear-time algorithm for testing radial level planarity @bbf-rlp-05.
While the dissertation by @bac-cpo-04 describes a prototypical implementation, no implementations exist of this
algorithm.
@brue-pvf-21 points out some issues with the algorithm by @bbf-rlp-05.
A simple polynomial-time algorithm is suggested by @brs-lpt-22.

# Related Problems

Reduces to $clustered by interpreting the concentric levels (including all levels below) as clusters [@sch-tat-13, Lemma 6.18].

# See Also

- Planarity Variants for Directed Graphs [@brue-pvf-21]
