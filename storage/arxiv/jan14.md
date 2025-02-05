<link href="../../whirlwind.css" rel="stylesheet">

<whirlheader>
    <p>Gary</p>
    <p>Arxiv</p>
    <p>January 14</p>
</whirlheader>

# Calabi-Yau 3-fold 

<definition>

A **Calabi–Yau 3-fold** is a complex, compact, Kähler manifold of real dimension 6 that has a vanishing first Chern class. 

The Chern class condition is implied by any of the following (equivalent) conditions:

1. The canonical bundle of $M$ is trivial.
2. $M$ has a holomorphic $n$-form that vanishes nowhere.
3. The structure group of the tangent bundle of $M$ can be reduced from $U(3)$, the unitary group, to $SU(3)$, the special unitary group.
4. $M$ has a Kähler metric with global holonomy contained in $SU(3)$.

</definition>

# Fukaya Category

<definition>

The **Fukaya category** of a symplectic manifold $(X,\omega)$ is a category $\mathcal{F}(X)$ whose objects are Lagrangian submanifolds of $X$ and morphisms are Lagrangian Floer chain groups: $\text{Hom}(L_0, L_1)=CF(L_0, L_1)$.

</definition>

# Foliations

A **foliation** is a geometric structure on a manifold that describes how the manifold can be "split" or "partitioned" into a collection of lower-dimensional submanifolds called leaves. Intuitively, a foliation organizes the manifold into a family of submanifolds, each of which looks locally like a Euclidean space.

Rigorously:

<definition>


Let $M$ be a smooth manifold of dimension $n$, and let $D$ be a smooth distribution on $M$, i.e., a smooth assignment of a subspace of $T_p M$ (the tangent space at each point $p \in M$) for each point in $M$. A **foliation** is a decomposition of $M$ into a collection of disjoint, smooth submanifolds, called **leaves**, such that:

1. Local Trivialization:
For each point $p \in M$, there exists a neighborhood $U \subset M$ of $p$, and coordinates on $U$ (called **leaf coordinates**) such that the leaves of the foliation locally look like the product of a lower-dimensional Euclidean space with the remaining coordinates. More precisely, if the leaves are $k$-dimensional, there is a smooth map from $U$ to $\mathbb{R}^k \times \mathbb{R}^{n-k}$ that maps the leaves to $\mathbb{R}^k \times \{ 0 \}$, while preserving the smooth structure of the foliation.

2. Integrability Condition:
The distribution $D$ is **integrable**, meaning that for any two vector fields $X, Y$ in the distribution, their Lie bracket $[ X, Y ]$ is also in the distribution. This condition ensures that locally through every point there exists a smooth $k$-dimensional submanifold, tangent to $D$, that forms a leaf of the foliation.

3. Codimension:
The **codimension** of the foliation is the difference between the dimension of the manifold and the dimension of the leaves. If the leaves are $k$-dimensional, then the foliation has codimension $n - k$. The dimension of the leaves is often referred to as the **leaf dimension**, and the codimension is the dimension of the **transverse space** (the space orthogonal to the leaves).


</definition>