---
title: 库仑势的Fourier transform(update 16/Nov/2020)
date: 2018/09/24
categories: 专业笔记
tags: [数学, 物理, 库仑势, Fourier]
---

<!-- toc -->

<!-- more -->

## 问题

三维库仑势的形式为：
$$
V(\vec{r}) = \frac{1}{r}
$$
按动量Fourier展开：
$$
V(\vec{r}) = \frac{1}{(2\pi)^3} \int_{-\infty}^{+\infty} \mathrm{d}^3\vec{k} \cdot V(\vec{k})\cdot e^{i\vec{k}\cdot\vec{r}}
$$
求 $V(\vec{k})$ 。

## 求解

$$
V{(\vec{k})} = \int_{-\infty}^{+\infty} \mathrm{d}^3\vec{r}\cdot V(\vec{r})\cdot e^{-i\vec{k}\cdot \vec{r}} = \int_0^{2\pi}\mathrm{d}\varphi \int_0^{+\infty}\mathrm{d}r\int_0^{\pi}\mathrm{d}\theta\cdot \frac{1}{r}e^{-ikr\cos\theta}r^2\sin\theta \\\\
=2\pi\int_0^{+\infty}\mathrm{d}r\int_0^{\pi}\mathrm{d}\theta\cdot e^{-ikr\cos\theta}r\sin\theta  = -2\pi\int_0^{+\infty}\mathrm{d}r\int_1^{-1}\mathrm{d}\cos\theta\cdot e^{-ikr\cos\theta}r \\\\
=-2\pi\int_0^{+\infty}\mathrm{d}r\cdot \left[e^{-ikr\cos\theta}r\frac{1}{-ikr}\right]_{\cos\theta = 1}^{\cos\theta =-1} = 2\pi\int_0^{+\infty}\mathrm{d}r\cdot \left[(e^{ikr}-e^{-ikr})\frac{1}{ik}\right] \\\\
=\frac{2\pi}{ik}\left[\frac{e^{ikr}}{ik}-\frac{e^{-ikr}}{-ik}\right] _0^{+\infty}
$$

但 $e^{-ikr}$ 与 $e^{-ikr}$ 在 $+\infty$ 处发散。

## 使其收敛

为了解决发散问题，可在一开始令
$$
V(\vec{r}) = \frac{1}{r} = \lim_{\mu\rightarrow 0} \frac{e^{-\mu r}}{r}
$$
所以
$$
V{(\vec{k})}  = \lim_{\mu\rightarrow 0} 2\pi\int_0^{+\infty}\mathrm{d}r\cdot \left[(e^{(ik-\mu)r}-e^{(-ik-\mu)r})\frac{1}{ik}\right] \\\\
= \lim_{\mu\rightarrow 0}\frac{2\pi}{ik}\left[\frac{e^{(ik-\mu)r}}{ik-\mu r}-\frac{e^{(-ik-\mu)r}}{-ik-\mu r}\right] _0^{+\infty} \\\\
$$

$$
= \lim_{\mu\rightarrow 0}\frac{2\pi}{ik}\left[\frac{-1}{ik-\mu }-\frac{-1}{-ik-\mu }\right] \\\\
=\lim_{\mu\rightarrow 0}\frac{2\pi}{ik}\frac{2ik}{k^2 + \mu ^2} =\lim_{\mu\rightarrow 0}\frac{4\pi}{k^2 + \mu ^2} \\\\
=\frac{4\pi}{k^2}
$$



### 注

函数满足一致收敛，积分与极限才可交换顺序。



## 类似的变换

用同样的方法, 可以得到
$$
\lim_{\eta \to 0^+}\int \mathrm{d}^3\vec{r} . e^{\mathrm{i}\vec{k}\cdot\vec{r}} r e^{-r\eta}
 = \frac{8 \pi}{k^4}
$$
$$
\lim_{\eta \to 0^+}\int \mathrm{d}^3\vec{r} . e^{\mathrm{i}\vec{k}\cdot\vec{r}} e^{-r\eta}
 = 0
$$

用 Mathematica 可以验证.

## Reference

- 关于使其收敛的说明, 分别从物理的角度, 数学的角度阐述这样做的合理性和必要性: https://physics.stackexchange.com/questions/7462/fourier-transform-of-the-coulomb-potential