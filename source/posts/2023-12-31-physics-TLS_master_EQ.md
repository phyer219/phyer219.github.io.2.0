---
title: 原子自发辐射与主方程
date: 2023/12/31
categories: 专业笔记
tags: [physics, master equation, spontaneous emission]
---

<!-- toc -->

<!-- more -->

- [原子自发辐射与主方程](#原子自发辐射与主方程)
  - [模型](#模型)
  - [粗粒化的时间演化 (coarse-grained rate of variation)](#粗粒化的时间演化-coarse-grained-rate-of-variation)
  - [对热库的假设](#对热库的假设)
    - [热库很大，处于定态](#热库很大处于定态)
    - [热库关联时间很短](#热库关联时间很短)
    - [真空电磁场作为热库](#真空电磁场作为热库)
  - [对相互作用的假设](#对相互作用的假设)
  - [近似之后的结果](#近似之后的结果)
    - [$V$ 的一阶项为零](#v-的一阶项为零)
    - [截断 $V$ 的二阶项](#截断-v-的二阶项)
    - [利用 $\\tau \>\\tau\_c$ 时 $g(\\tau) \\to 0$，把对 $t'$ 和 $t''$ 的积分解耦](#利用-tau-tau_c-时-gtau-to-0把对-t-和-t-的积分解耦)
  - [在能量本征态下写出，积掉 $t'$，做久期近似](#在能量本征态下写出积掉-t做久期近似)
- [Reference](#reference)


# 原子自发辐射与主方程

## 模型

$$
H = H_A + H_R + V
$$

- $H_A$ : 要研究的系统 $A$ 的哈密顿量， 比如原子 (Atom)。
- $H_R$ : 系统所处的热库 (Reservoir) $R$ 的哈密顿量，比如真空电磁场 (Radiation)
- $V = -AR$ : 系统与热库的耦合。$A$ 系统子空间的算符。$R$ 热库子空间的算符。

对于二能级原子与真空电磁场的耦合：
$$
\begin{align}
H_A = \frac{\hbar}{2}\left(\omega_{ba}|b\rangle\langle b|
           - \omega_{ba}|a\rangle\langle a|\right)
\end{align}
$$
真空电磁场：
$$
\begin{align}
H_R = \sum_i \hbar \omega_i a_i^{\dagger} a_i
\end{align}
$$
偶极近似下，算符 $A$ 是原子偶极跃迁的矩阵元，算符 $R$ 是量子化的电场强度。具体来讲:
$$
\begin{align}
A =& D (|a\rangle\langle b| + |b\rangle\langle a|) \\
R =& \sum_i \epsilon_i (a_i - a_i^\dagger)
\end{align}
$$
其中 $D, \epsilon_i$ 都是系数。

## 粗粒化的时间演化 (coarse-grained rate of variation)

有两个重要的时间尺度。第一个是热库的关联时间 $\tau_c$ 。第二个是系统 $A$ 演化的时间尺度 $T_R$。他们应当满足 $\tau_c\ll T_R$
主方程的时间尺度 $\Delta t$ 的量级为
$$
\begin{align}
\tau_c \ll \Delta t \ll T_R
\end{align}
$$
以下考虑相互作用绘景，任意算符 $O$ 在相互作用绘景中记为 $\tilde{O}(t) = e^{-\frac{1}{i\hbar} (H_A + H_R)}Oe^{\frac{1}{i\hbar} (H_A + H_R)}$ 。系统加热库的密度矩阵记为 $\rho(t)$ 。在相互作用绘景中
$$
\begin{align}
\tilde{\rho}(t) =& e^{-\frac{1}{i\hbar} (H_A + H_R)}\rho(t)e^{\frac{1}{i\hbar} (H_A + H_R)}\\
\tilde{V}(t) =& e^{-\frac{1}{i\hbar} (H_A + H_R)}Ve^{\frac{1}{i\hbar} (H_A + H_R)}\\
\tilde{A}(t) =& e^{-\frac{1}{i\hbar} H_A}Ae^{\frac{1}{i\hbar} H_A}\\
\tilde{R}(t) =& e^{-\frac{1}{i\hbar} H_R}Re^{\frac{1}{i\hbar} (H_R)}
\end{align}
$$
根据密度矩阵在相互作用绘景中的演化方程 $i\hbar \dot{\tilde{\rho}(t)} = [\tilde{V(t)}, \tilde{\rho}(t)]$， 可知在我们粗粒化的时间 $t$ 到 $t + \Delta t$ 内，密度矩阵的演化为
$$
\begin{align}
\tilde{\rho}(t + \Delta t) = \tilde{\rho}(t) + \frac{1}{i\hbar}\int_t^{t+\Delta t} dt'\,
\left[ \tilde{V}(t'), \tilde{\rho}(t') \right]
\end{align}
$$
我们对上式迭代一次，并把环境求偏迹掉，得到环境密度矩阵 $\tilde{\sigma}(t) = \mathrm{Tr}_R [\tilde{\rho}(t)]$ 的演化增量
$$
\begin{align}
\Delta\tilde{\sigma}(t) \equiv &
\tilde{\sigma}(t + \Delta t) - \tilde{\sigma}(t) \\
=& \frac{1}{i\hbar}\int_t^{t+\Delta t} dt'\,
\mathrm{Tr}_R\left[ \tilde{V}(t'), \tilde{\rho}(t) \right]\\
& + \left(\frac{1}{i\hbar}\right)^2\int_t^{t+\Delta t} dt'\,
\int_t^{t'} dt''\,
\mathrm{Tr}_R\left[ \tilde{V}(t'), \left[\tilde{V}(t''), \tilde{\rho}(t'') \right] \right]
\end{align}
$$
直到上式，都是严格精确的，没有做任何近似。

## 对热库的假设

### 热库很大，处于定态

热库，顾名思义，要比研究的系统 $A$ 大得多。把系统 $A$ 求偏迹掉，热库的密度矩阵记为 $\tilde{\sigma}_R(t) = \mathrm{Tr}_A [\tilde{\rho} (t)]$ 。

由于热库比系统 $A$ 大得多，所以可以认为一直不变
$$
\begin{align}
\tilde{\sigma}_R(t) \approx \tilde{\sigma}_R(t) = \sigma_R
\end{align}
$$
其次，假设热库一直处在一个定态上，也就是说
$$
\begin{align}
[\sigma_R, H_R] = 0
\end{align}
$$
记热库的能量本征态为
$$
\begin{align}
H_R |\mu \rangle = E_{\mu} |\mu \rangle
\end{align}
$$
那么定态 $\sigma_R$ 可以展开为
$$
\begin{align}
\sigma_R = \sum_{\mu} p_{\mu} | \mu \rangle \langle \mu |
\end{align}
$$
假设 $R$ 在 $\sigma_R$ 上的均值为 $0$
$$
\begin{align}
\mathrm{Tr}[\sigma_R R] = \mathrm{Tr}[\sigma_R \tilde{R}(t)]
\end{align}
$$
因此就有
$$
\begin{align}
\mathrm{Tr}_R[\tilde{V}(t')\sigma_R] = 0
\end{align}
$$

### 热库关联时间很短

定义热库中的算符 $R$ 的双时平均
$$
\begin{align}
g(\tau) \equiv g(t' - t'') \equiv \mathrm{Tr}\left[\sigma_R \tilde{R}(t') \tilde{R}(t'')\right]
= \mathrm{Tr}\left[\sigma_R \tilde{R}(\tau) \tilde{R}(0)\right]
\end{align}
$$
我们假设 $g(\tau)$ 只集中在 $\tau<\tau_c$ 的范围内， 在 $\tau > \tau_c$ 迅速衰减。这在热库很大是，是自然的。热库很大，能谱倾向于连续，求和在 $\tau$ 很大时，就会干涉相消。

### 真空电磁场作为热库

真空电磁场的密度矩阵为
$$
\begin{align}
\sigma_R = |0\rangle \langle 0|
\end{align}
$$
是一个温度为零的玻色场，每一个模式都处于基态，没有任何光子激发。它显然满足
$$
\begin{align}
\mathrm{Tr}_R[\tilde{V}(t')\sigma_R] = -\tilde{A}(t') \langle 0 |\tilde{R}(t') | 0\rangle
= -\tilde{A}(t') \sum_i \epsilon_i \langle 0 | (a_i - a_i^\dagger) | 0\rangle
= 0
\end{align}
$$
真空电磁场的 $g(\tau)$ 为
$$
\begin{align}
g(\tau) = \sum_{i} |\epsilon_i|^2 \langle 0 | a_i e^{i \omega_i\tau} a_i^{\dagger} |0\rangle
= \sum_i |\epsilon_i|^2 e^{-i\omega_i \tau}
\end{align}
$$
这个是可以具体算出的，但是可以看出，当 $\omega_i$ 非常密时，当 $\tau$ 大于某个值时，会由于干涉相消变成 $0$ 。一个用于理解的情况是，$\epsilon_i$ 是一个常数，$\omega_i$ 太密，以至于连续，求和化积分，结果就变成一个 $\delta$ 函数，只在 $\tau=0$ 时非零。

## 对相互作用的假设

当然是弱耦合。

其次，因为是弱耦合，这也会导致系统 $A$ 和热库的关联
$$
\begin{align}
\tilde{\rho}_{\mathrm{correl}}(t) \equiv \tilde{\rho}(t)
- \mathrm{Tr}_R [\tilde{\rho}(t)]\otimes  \mathrm{Tr}_A [\tilde{\rho}(t)]
\end{align}
$$
在粗粒化的时间尺度下($\tau_c \ll \Delta t$)只作为高阶项贡献（详见书），因此可以将总的密度矩阵近似为直积
$$
\begin{align}
\tilde{\rho}(t)
\approx \mathrm{Tr}_R [\tilde{\rho}(t)]\otimes  \mathrm{Tr}_A [\tilde{\rho}(t)]
\end{align}
$$

## 近似之后的结果

现在，我们结合对大环境小系统，弱耦合的假设，对之前的严格结果
$$
\begin{align}
\Delta\tilde{\sigma}(t) \equiv &
\tilde{\sigma}(t + \Delta t) - \tilde{\sigma}(t) \\
=& \frac{1}{i\hbar}\int_t^{t+\Delta t} dt'\,
\mathrm{Tr}_R\left[ \tilde{V}(t'), \tilde{\rho}(t) \right]\\
& + \left(\frac{1}{i\hbar}\right)^2\int_t^{t+\Delta t} dt'\,
\int_t^{t'} dt''\,
\mathrm{Tr}_R\left[ \tilde{V}(t'), \left[\tilde{V}(t''), \tilde{\rho}(t'') \right] \right]
\end{align}
$$
进行化简。

### $V$ 的一阶项为零

$$
\begin{align}
\mathrm{Tr}_R\left[ \tilde{V}(t'), \tilde{\rho}(t) \right]
= \tilde{A}(t') \tilde{\sigma}(t) \, \mathrm{Tr}\left[ \tilde{R}(t'), \sigma_R \right]
= 0
\end{align}
$$
因此一阶项消失。

### 截断 $V$ 的二阶项

也就是把 $V$ 的二阶项中的 $\tilde{\rho}(t'')$ 换成 $\tilde{\rho}(t)$

### 利用 $\tau >\tau_c$ 时 $g(\tau) \to 0$，把对 $t'$ 和 $t''$ 的积分解耦
$$
\begin{align}
\int_t^{t+\Delta t} dt'\, \int_t^{t'} dt''\
= \int_0^{\Delta t} d\tau \, \int_{t+\tau}^{t+\Delta t} dt'\
\approx \int_0^{\infty} d\tau \, \int_{t}^{t+\Delta t} dt'\
\end{align}
$$
此时，严格的结果现在变成了
$$
\begin{align}
\frac{\Delta \tilde{\sigma}(t)}{\Delta t}
=& - \frac{1}{\hbar^2}\int_0^\infty d\tau \, \frac{1}{\Delta{t}}\int_t^{t+\Delta t} d t' \\
&\left\{
  g(\tau) \left[\tilde{A}(t')\tilde{A}(t'-\tau) \tilde{\sigma}(t)
                - \tilde{A}(t'-\tau) \tilde{\sigma} (t) \tilde{A}(t')\right]
\right.
                \\
&\left.
  + g(-\tau)\left[
     \tilde{\sigma} (t)\tilde{A}(t'-\tau) \tilde{A}(t')
     - \tilde{A}(t') \tilde{\sigma} (t)\tilde{A}(t'-\tau)
   \right]
\right\}
\end{align}
$$

## 在能量本征态下写出，积掉 $t'$，做久期近似

在能量本征表象下，花括号中的四项中关于 $t'$ 的部分是相同的，因此可以拿出来积掉

$$
\begin{align}
\frac{1}{\Delta t} \int_t^{t+\Delta t} dt'\, e^{-i (\omega_{ba} - \omega_{dc})}
\end{align}
$$
在 $|\omega_{ba} - \omega_{dc}|\Delta t \ll 1$ 时， 结果为 $1$ 。
在 $|\omega_{ba} - \omega_{dc}|\Delta t \gg 1$ 时， 结果为 $0$ 。
在 $|\omega_{ba} - \omega_{dc}|\Delta t \sim 1$ 时， 为弱耦合，可以忽略。

因此
$$
\begin{align}
\frac{\Delta \tilde{\sigma}_{ab}(t)}{\Delta t} = \sum_{c, d}^{\mathrm{sec}}
e^{-i(\omega_{ba} - \omega_dc)t} \mathcal{R}_{abcd}\tilde{\sigma}_{cd}(t)
\end{align}
$$
其中
$$
\begin{align}
\mathcal{R}_{abcd}
=& -\frac{1}{\hbar^2} \int_0^{\infty} d\tau\, \\
=& \left\{
  g(\tau)\left[ \delta_{bd} \sum_n A_{an}A_{nc} e^{i\omega_{cn}\tau}
  -A_{ac}A_{db}e^{i\omega_{ca}\tau}   \right] \right. \\
  &+\left.
    g(-\tau)\left[ \delta_{ac} \sum_n A_{dn}A_{nb} e^{i\omega_{nd}\tau}
  -A_{ac}A_{db}e^{i\omega_{bd}\tau}   \right]
 \right\} \\
\end{align}
$$

# Reference

- Cohen-Tannoudji, Claude, Jacques Dupont-Roc, and Gilbert Grynberg. Atom-Photon Interactions: Basic Processes and Applications. New York: Wiley, 1992. Chapter IV.
