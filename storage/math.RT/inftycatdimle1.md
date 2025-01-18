<link href="../../whirlwind.css" rel="stylesheet">

<whirlheader>
    <p>Eric Zhang</p>
    <p>Infinity Categories of Dimension Less Than Or Equal To 1</p>
    <p>January 9, 2025</p>
</whirlheader>

Source: JMM 2025

# Simplicial Set 

<definition>

A **simplicial set** $X$ is a functor $\Delta^{\text{op}}\to \text{Sets}$, where $\Delta$ is the category whose objects are linearly ordered and morphisms are non-decreasing maps.

</definition>

# Connection to Quivers 

<theorem>
<src>Lurie, 2018</src>

The category of simplicial sets of $\dim \le 1$ is equivalent to the category of quivers.

</theorem>

# Gelfand-Kirillov Dimension 

<definition>

The **Gelfand-Kirillov Dimension** of a right module $M$ over a $k$-algebra $A$ is
$$
\operatorname{GKdim} = \sup_{V, M_0} \limsup_{n\to\infty} \log_n \dim_k M_0 V^n
$$

where the supremum is taken over all finite-dimensional subspaces $V\subset A$ and $M_0\subset M$.

</definition>
