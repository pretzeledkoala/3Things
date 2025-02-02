<link href="../../whirlwind.css" rel="stylesheet">

<whirlheader>
    <p>Christopher Woodward</p>
    <p>Integrable Systems and Markov Numbers</p>
    <p>June 14, 2024</p>
</whirlheader>


Source: Rutgers Current Trends in Mathematics

# Fourier Restriction Problem 

<problem>

When does an inequality of the form $ \| \hat{f} \|_{L^q(S^{n-1})} \leq C \| f \|_{L^p(\mathbb{R}^n)} $ hold for functions $ f \in L^p(\mathbb{R}^n) $, where $ \hat{f} $ denotes the Fourier transform of $ f $ and $ q $ is related to $ p $?

</problem>

# Fourier Transform

The **Fourier transform** of a function $ f $ defined on a measure space $ (X, \mu) $ is defined as:
$$
    \hat{f}(\xi) = \int_X f(x) e^{-i \langle x, \xi \rangle} \, d\mu(x)
$$
where $ \xi \in \mathbb{R}^n $, $ \langle x, \xi \rangle $ denotes the inner product between $ x $ and $ \xi $, and $ d\mu(x) $ is the measure on $ X $.

# Stein-Tomas Inequality 

For $ f \in L^p(\mathbb{R}^n) $ with $ 1 \leq p \leq \frac{2(n+1)}{n+3} $, the Fourier transform $ \hat{f} $ restricted to the unit sphere $ S^{n-1} $ belongs to $ L^2(S^{n-1}) $, and there exists a constant $ C $ such that
$$
    \left( \int_{S^{n-1}} |\hat{f}(\xi)|^2 \, d\sigma(\xi) \right)^{1/2} \leq C \| f \|_p
$$
where $ d\sigma $ is the surface measure on $ S^{n-1} $.