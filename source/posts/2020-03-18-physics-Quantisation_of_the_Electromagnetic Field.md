---
title: 量子光学读书会01电磁场的量子化
date: 2020/03/18
categories: 专业笔记
tags: [物理, 量子光学读书会, 电磁场的量子化]
---

<!-- toc -->

<!-- more -->

3.11 日 DRJ 主讲.

### 2.1 电磁场的量子化

选取 Coulomb gauge, 由 Maxwell equations 可以得到关于矢势 $\vec{A}$ 的波动方程
$$
\nabla^2 \vec{A}(\vec{r},t) = \frac{1}{c^2} \frac{\partial^2 \vec{A}(\vec{r}, t)}{\partial t^2}
$$
选取基底和适当的单位, 解可以写为
$$
A(\vec{r},t) = \sum_k \sqrt{\frac{\hbar}{2\omega_k\varepsilon_0}} \left[ a_k \vec{u}_k(\vec{r}) e^{-\mathrm{i}\omega_k t} + a_k^{\dagger} \vec{u}_k^*(\vec{r}) e^{\mathrm{i}\omega_k t}\right]
$$
电磁场的经典 Hamiltonian 为
$$
H = \frac{1}{2} \int (\varepsilon_0 \vec{E}^2 + \mu_0\vec{H}^2) \,\mathrm{d}^3\vec{r}
$$
将 $\vec{A}$ 代入, 然后做对应 $a_k \to \hat{a}_k$ , 并满足 Boson 对应关系, 最后得到量子化的电磁场
$$
H = \sum_k \hbar\omega_k \left( a_k^{\dagger} a_k + \frac{1}{2} \right)
$$

## 2.2 Fock 表象

# 参考

- D.F. Walls, Gerard J. Milburn, Quantum Optics, Springer (2008)