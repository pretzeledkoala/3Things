<link href="../../whirlwind.css" rel="stylesheet">

<whirlheader>
    <p>Ravi Vakil</p>
    <p>The Mathematics of Doodling</p>
    <p>January 11, 2025</p>
</whirlheader>

Source: JMM 2025 

# Doodling
I want to remember that if we doodle around a diagram it eventually becomes more and more like a circle.

# Volume of $n$-sphere 

<theorem>

The volume of an $n$-sphere of radius $r$ is 
$$
\frac{\pi^{n/2} r^n}{\Gamma(\frac{n}{2}+1)}
$$

</theorem>

# Witten's Conjecture

Suppose that $M_{g,n}$ is the moduli stack of compact Riemann surfaces of genus $g$ with $n$ distinct marked points $x_1, \dots, x_n$, and $\overline{M}_{g,n}$ is its Deligne–Mumford compactification. There are $n$ line bundles $L_i$ on $\overline{M}_{g,n}$, whose fiber at a point of the moduli stack is given by the cotangent space of a Riemann surface at the marked point $x_i$. The intersection index $\langle \tau_{d_1}, \dots, \tau_{d_n} \rangle$ is the intersection index of 
$$
\prod_{i=1}^n c_1(L_i)^{d_i}
$$
on $\overline{M}_{g,n}$, where $\sum_{i=1}^n d_i = \dim \overline{M}_{g,n} = 3g - 3 + n$, and 0 if no such $g$ exists, where $c_1$ is the first Chern class of a line bundle. 

Witten's generating function:
$$
F(t_0,t_1,\dots) = \sum \langle \tau_0^{k_0} \tau_1^{k_1} \cdots \rangle \prod_{i \geq 0} \frac{t_i^{k_i}}{k_i!} 
= \frac{t_0^3}{6} + \frac{t_1}{24} + \frac{t_0 t_2}{24} + \frac{t_1^2}{24} + \frac{t_0^2 t_3}{48} + \cdots
$$
encodes all the intersection indices as its coefficients.

<theorem>
<src>Witten's Conjecture</src>

The partition function $Z = \exp F$ is a $\tau$-function for the KdV hierarchy, in other words, it satisfies a certain series of partial differential equations corresponding to the basis $\{ L_{-1}, L_0, L_1, \dots \}$ of the Virasoro algebra.

</theorem>
