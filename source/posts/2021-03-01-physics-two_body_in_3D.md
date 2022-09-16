---
title: 两体束缚态
date: 2021/03/01
categories: 专业笔记
tags: [two body, bound state]
---

<!-- toc -->

<!-- more -->
# any

$r > r_0$ 时, $V(r) = 0$ , 径向 Schrodinger 方程为
$$
\label{eq:sq}
-\chi'' + \frac{l(l+1)}{r^2}\chi = k^2 \chi
$$

将 $\chi$ 在 $k=0$ 处做低能展开
$$
\chi(r) = \phi(r) + k^2 f(r) +k^4 g(r) + \mathcal{O}(k^6)
$$

将展开代回到 $(\ref{eq:sq})$ , 对比 $k$ 的系数得到:

零能时, 也就是 $\phi$ 满足的方程为
$$
\label{eq:phi}
- \phi '' + \frac{l(l+1)}{r^2}\phi = 0
$$
$f$ 满足的方程为
$$
\label{eq:f}
- f '' + \frac{l(l+1)}{r^2}f = \phi
$$
$g$ 满足的方程为
$$
\label{eq:g}
- g'' + \frac{l(l+1)}{r^2}g = f
$$

# s-wave

$l = 0$ 代入 $(\ref{eq:phi})$ 零能解为
$$
\phi \propto \sharp_1  + \sharp_2 r
$$
舍去一个归一化因子, 相对系数可定义散射长度
$$
\label{eq:phi_s}
\phi = 1 - \frac{r}{a}
$$

$$
\psi(r)|_{k=0} = \frac{\chi(r)}{r} \propto \frac{1}{r} - \frac{1}{a}
$$
$(\ref{eq:phi_s})$ 代入 $(\ref{eq:f})$ 解得
$$
f = -\frac{r^2}{2} + \frac{r^3}{6a} + C_1 + C_2 r
$$
重新定义 $f \to f - C_1\phi$ (这总是可以做到的, 因为相当于直接在展开的时候令 $\chi = \phi + k^2 (f-C_1\phi) + k^4 g$ , $f - C_1 \phi$ 也可以做一到是任意函数 ) ,并用系数定义 effective range
$$
\label{eq:f_s}
f = -\frac{r^2}{2} + \frac{r^3}{6a} + \frac{r_s}{2} r
$$
$(\ref{eq:f_s})$ 代入 $(\ref{eq:f})$ ,并做类似地处理 ( $g\to g - \cdots$ , 定义 $r_s'$ ) 得到 (  $r_s'$ **的系数why?1/24??** ) 
$$
g = \frac{r^4}{24} - \frac{r^5}{120a} - \frac{r_s}{12}r^3 +\frac{r_s'}{24}r
$$
s-wave 非零能的径向方程实际是严格可解的, 舍去一个归一化系数, 另一个系数定义相移( 是 $k$ 的函数 ), 形式为
$$
\psi(r) = \frac{\sin (k r + \delta_k)}{r\sin\delta_k}
$$
$\psi(r)$ 也做低能 $k\to 0$ 的展开
$$
\psi(r) = \frac{\chi(r)}{r} = \cot\delta_k \sin(kr)\frac{1}{r} + \cos(kr)\frac{1}{r} 
= \frac{1}{r} + k\cot\delta_k + \mathcal{O}(r^2)
$$
 $k\cot\delta_k$ 为 $r^0$ 的系数, 因此得到 $k\cot\delta_k$ 低能展开
$$
k\cot \delta_k = -\frac{1}{a} + k^2\frac{r_s}{2} + k^4 \frac{r_s'}{24} + \mathcal{O}(k^6)
$$

# p-wave

 $l = 1$ 代入 $(\ref{eq:phi})$ 零能解为零能时
$$
-\phi'' + \frac{1\times(1+1)}{r^2}\phi = 0
$$
解为
$$
\phi(r) \propto \sharp_1 r^2 + \sharp_2 \frac{1}{r}
$$

舍去一个归一化因子, 相对系数可定义 $v$ 
$$
\label{eq:phi_p}
\phi(r) = \frac{1}{r} - \frac{r^2}{3v}
$$
$(\ref{eq:phi_p})$ 代入 $(\ref{eq:f})$ 解得
$$
f = \frac{r}{2} + \frac{r^4}{30v} + \sharp_1 r^2 +\sharp_2 \frac{1}{r}
$$
与 s-wave 类似的处理, 用系数定义 $R$ , 重新定义后的 $f$ 为
$$
f = \frac{r}{2} + \frac{r^4}{30v} - \frac{r^2}{3R}
$$
所以
$$
\psi(r) = \frac{\chi(r)}{r} = \left( \frac{1}{r^2} - \frac{r}{3v} \right)
         + k^2 \left( \frac{1}{2} - \frac{r}{3R} + \frac{r^3}{30v}  \right) + \mathcal{O}(k^4)
$$


~~p-wave 非零能的径向方程的严格解是求 Bessel 函数, 舍去一个归一化系数, 另一个系数定义相移( 是 $k$ 的函数 ), 在 $r\to\infty$ 的渐近形式为~~

> $$
> \begin{align}
> \psi(r) = \frac{\chi(r)}{r} \sim& \frac{1}{r\sin\delta_k}\sin\left(kr - \frac{1}{2}\pi + \delta_k  \right) \\
>  =& -\frac{1}{r}\cot \delta_k  + k + r\frac{k^2}{2}\cot\delta_k+\mathcal{O}(r^2)\quad, \quad \mathrm{as}\, r \to\infty
>  \end{align}
> $$



将严格解也在低能展开 ( **此式的来源???** )
$$
\psi(r) = \frac{\chi(r)}{r} \propto \cot\delta_k j_1(kr) - y_1(kr) = \frac{1}{k^2 r^2} + \frac{1}{2} 
             + \frac{r}{3}k \cot\delta_k + \mathcal{O}(r^2)
$$

对比 $\frac{1}{r^2}$ 及 $r$ 的系数可得
$$
\cot \delta_k = -\frac{1}{v k^3} - \frac{1}{kR} + \mathcal{O}(k)
$$


# d-wave

 $l = 2$ 代入 $(\ref{eq:phi})$ 零能解为零能时
$$
-\phi'' + \frac{2(2+1)}{r^2}\phi = 0
$$
解为
$$
\phi(r) = \sharp_1 r^3 + \sharp_2 \frac{1}{r^2}
$$

舍去一个归一化因子, 相对系数可定义 $D$ 
$$
\label{eq:phi_d}
\phi(r) = \frac{1}{r^2} - \frac{r^3}{45 D}
$$
$(\ref{eq:phi_d})$ 代入 $(\ref{eq:f})$ 解得
$$
f = \frac{1}{6} + \frac{r^5}{630 D} + \sharp_1 r^3 + \frac{\sharp_2}{r^2}
$$
与 s-wave 类似的处理, 用系数定义 $v$ , 重新定义后的 $f$ 为
$$
\label{eq:f_d}
f = \frac{1}{6} + \frac{r^5}{630 D} - \frac{r^3}{45v}
$$
$(\ref{eq:f_d})$ 代入 $(\ref{eq:g})$ ,并做类似地处理 ( $g\to g - \cdots$ , 定义 $r_s'$ ) 得到
$$
\begin{align}
g =& \frac{r^5}{630 v} + \frac{r^2}{24} - \frac{r^7}{22680 D} + \sharp_1 r^3 + \frac{\sharp_2}{r^2} \\
\Rightarrow g =& \frac{r^5}{630 v} + \frac{r^2}{24} - \frac{r^7}{22680 D} -\frac{r^3}{45R}  
\end{align}
$$
所以
$$
\begin{align}
\psi(r) =& \frac{\chi(r)}{r} = \frac{\phi(r) + k^2 f(r) +k^4 g(r) + \mathcal{O}(k^6)}{r} \\
        =&  \left(\frac{1}{r^3} - \frac{r^2}{45 D} \right)
         +k^2\left( \frac{1}{6} + \frac{r^5}{630 D} - \frac{r^3}{45v} \right)
         +k^4\left( \frac{r^5}{630 v} + \frac{r^2}{24} - \frac{r^7}{22680 D} -\frac{r^3}{45R} \right)
\end{align}
$$


将严格解也在低能展开
$$
\psi(r) = \frac{\chi(r)}{r} \propto \cot\delta_k j_2(kr) - y_2(kr) 
        = \frac{3}{k^3 r^3} + \frac{1}{2kr} + \frac{kr}{8} 
             + \frac{r^2}{15}k^2 \cot\delta_k + \mathcal{O}(r^3)
$$

对比系数得
$$
\cot \delta_k = - \frac{1}{Dk^5} - \frac{1}{vk^3} - \frac{1}{kR} + \mathcal{O}(k)
$$