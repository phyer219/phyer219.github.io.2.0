---
title: 常用光学知识点
date: 2020/03/18
categories: 专业笔记
tags: [物理, 光学]
---

<!-- toc -->

<!-- more -->
批作业会用到

# 第二章 几何光学 (Geometrical Optics)
## 几何光学精确的, 基本的规律

### 反射定律与折射定律与全反射

### 从波来理解几何光学: 惠更斯作图法

### 费马原理 (Fermat’s Principle) 与物像等光程与虚光程

> Light traverses the route having the smallest optical path length

教材 38 页. 为了把物像之间的等光程性原理推广到虚物或虚像的情形, 需要引入 "虚光程" 的概念.

光程正负号的规定: 与虚物或虚像相联系的与实际光线的延长线对应的光程称为虚光程，规定其符号取负值. (实际光线没有走到虚物或虚像的位置, 所以要减去)

折射率的规定: 虚光程部分的折射率由与之对应的实际光线的折射率决定. (光按照实际光线那边的折射率才能走到虚像或虚物的位置, 所以折射率按实际光线那边算)

## 傍轴近似下的成像

### 球面折射

可以通过折射定律或费马原理在傍轴近似下得到下式:
$$
\frac{n'}{s'} + \frac{n}{s} = \frac{n'-n}{r}
$$

按入射光线从左到右, 式中符号规定如下:

- 物在顶点左侧, $s>0$ , 实物
- 像在顶点右侧, $s'>0$ , 实像
- 球心在顶点右侧, $r>0$

### 球面反射

可理解为一种特殊的 "折射" , $n'=-n$ , 就可以由球面折射得到球面反射.

### 球面焦距

由球面折射可以得到焦距的表达式
$$
\begin{align}
s'\to&\infty \\
s\to& f = n\cdot\frac{r}{n'-n}
\end{align}
$$

$$
\begin{align}
s\to&\infty \\
s'\to& f' = n' \cdot \frac{r}{n'-n}
\end{align}
$$

那么用焦距来表达球面折射
$$
\frac{f'}{s'} + \frac{f}{s} = 1
$$
这也叫高斯物像公式.

### 横向放大率

根据教材图 2-9 , 对于折射, 一定有 $y'<0$ , 在傍轴近似下, 根据折射定律
$$
V = \frac{y'}{y} = \frac{(-i') s'}{i s} = -\frac{ns'}{n's} = -\frac{fs'}{f's}
$$

## 薄透镜成像

薄透镜的假设是两个球面的顶点几乎重合, 那么就可以认为 $s_1'=-s_2$ , 那么用两次球面折射公式可以得到
$$
\frac{n'}{s'} + \frac{n}{s} = \frac{n_L-n}{r_1} + \frac{n' - n_L}{r_2}
$$

由上式将 $s$ 或者 $s'$ 取为 $\infty$ 可以得到焦距公式
$$
\begin{align}
s'\to&\infty \\
s\to& f = \frac{n}{\frac{n_L-n}{r_1} + \frac{n' - n_L}{r_2}}
\end{align}
$$

$$
\begin{align}
s\to&\infty \\
s'\to& f' = \frac{n'}{\frac{n_L-n}{r_1} + \frac{n' - n_L}{r_2}}
\end{align}
$$

取 $n'=n=1$ 可得磨镜者公式
$$
f = f' = \frac{1}{(n_L - 1)(\frac{1}{r_1} - \frac{1}{r_2})}
$$

薄透镜的成像仍然满足高斯公式. 若透镜两边折射率相等, 那么 $f=f'$ , 便得到最常见的薄透镜成像公式
$$
\frac{1}{s'}+\frac{1}{s} = \frac{1}{f}
$$
这个公式的条件是: 傍轴, 薄透镜, 透镜两边折射率相等. 此时过光心的光线方向不变, 横向放大率也变为
$$
V = - \frac{s'}{s}
$$




## 理想光具组成像

### 理想光具组公式

理想光具组可以用高斯公式.

按入射光线从左到右. $s$ 为物到物方面的距离, 在左为正. $s'$ 为像到像方主面的距离, 在右为正. (教材57页) $f, f'$ 与 $s, s'$ 有相同的符号规则. 

两个光具组合在一起
$$
\begin{align}
f =& -\frac{f_1 f_2}{\Delta} \\
f' =& -\frac{f_1' f_2'}{\Delta} \\
X_H = & H_1H =  f_1 \frac{d}{\Delta}\\
X_H' =&H_2'H =  f_2' \frac{d}{\Delta}
\end{align}
$$


其中按照入射光线从左往右, $\Delta$ 是第一个光具组的像方焦点与第二个光具组的物方焦点的距离, $d$ 是对应的主面的距离.

### 理想光具作图

节点(冗余的条件): 角放大率为 $1$

## 光学仪器: 眼镜

近视镜应该让佩戴者看清无穷远的物, 也就是使无穷远处的物成像于佩戴者的远点处.

远视镜应该让佩戴者看清明视距离 ( $25\mathrm{cm}$ ) 处的物, 也就是使明视距离处的物成像于佩戴者近点处.

眼镜的度为
$$
P = 100\mathrm{m}/f
$$
近视眼佩戴凹透镜, 度数为负. 远视眼佩戴凸透镜, 度数为正.

## 几何光学总结

$$
\begin{align}
\left\{\begin{array}{c}惠更斯原理\\费马原理\end{array}\right\}
\overset{精确}{\Rightarrow}
\left\{\begin{array}{c}折射定律\\反射定律\end{array}\right\}
\overset{傍轴近似}{\Rightarrow}
\left\{\begin{array}{c}球面折射公式\\球面反射公式\end{array}\right\}
\overset{薄透镜近似}{\Rightarrow}
薄透镜高斯物像公式
\end{align}
$$





# 第三章 干涉

## 杨氏双缝

在傍轴近似下有
$$
\frac{\delta}{d} = \frac{x}{D}
$$

双缝间距为 $d$ , 距离孔 $D$ 处的屏上,  $x$ 的距离对应 $\delta$ 的光程差.

## 等厚干涉

牛顿环, 由于半波损, 中心为暗点.

## 等倾干涉

上下表面反射的相同倾角的两束光在无穷远处形成干涉条纹. 无近似, $i$ 为介质内的入射反射角(教材3-35)
$$
\Delta L = 2 n h \cos i
$$

F-P 干涉仪条纹的半高全宽 $\varepsilon$ 与反射率 $R$ 之间的关系
$$
\varepsilon = \frac{2(1 - R)}{\sqrt{R}}
$$


# 第四章 衍射

## 用矢量图解法叠加振幅

教材图 4-15

## 菲涅耳半波带片的焦距公式

好像以前那种老式的手电筒上就是用的这种衍射的会聚透镜.
$$
f = \frac{\rho_1^2}{\lambda} = \frac{\rho_k^2}{k\lambda}
$$

## 夫琅禾费衍射

### 单缝

$$
\frac{I}{I_0} = \left(\frac{\sin \alpha}
{\alpha}\right)^2 \quad, \mathrm{where} \quad
\alpha = \frac{a \pi}{\lambda}\sin \theta
$$

### 多缝


$$
\frac{I}{I_0} = \left(\frac{\sin \alpha}{\alpha}\right)^2 
\left(\frac{\sin N\beta}{\sin\beta}\right)^2
\quad, \mathrm{where} 
\quad\alpha = \frac{a \pi}{\lambda}\sin \theta,
\quad\beta = \frac{d \pi}{\lambda}\sin \theta
$$


当 $\beta = k\pi$ 时, 多缝因子为 $N^2$ 为主极大. 当 $\beta = (k + m/N)\pi,m/N\notin \mathbb{Z}$ 时, 强度为零.

半角宽度, 是 $k$ 级主极大到相邻暗纹的距离
$$
\begin{align}
\Delta \theta_k =& (\theta_k+\Delta\theta_k) - \theta_k 
    = \arcsin\left[\left( k + \frac{1}N \right) \frac{\lambda}{d}\right] 
       - \arcsin\left( \frac{k\lambda}{d}\right)
    = \frac{\lambda}{Nd\cos\theta_k} + \mathcal{O}\left( \frac{1}{N^2} \right) \\
    \approx& \frac{\lambda}{Nd\cos\theta_k}

\end{align}{}
$$

### 光栅

"光栅的衍射场鲜明地表现出'多光束干涉'的基本特征". 光栅性能的主要标志为色散本领和色分辨本领.

角色散本领, 是两个很接近的波长产生的两个主极大分开的角度与波长差的比值, 量纲是波长的倒数
$$
\begin{align}
D_{\theta} =& \frac{\delta \theta}{\delta\lambda} 
           =\frac{\mathrm{d}}{\mathrm{d}\lambda}\arcsin\left( \frac{k\lambda}{d} \right) 
           =\frac{k}{d}\frac{1}{\sqrt{1-\left( \frac{k\lambda}{d} \right)^2}}
           =\frac{k}{d}\frac{1}{\sqrt{1-\sin^2 \theta}} \\
           =& \frac{k}{d\cos\theta_k}
\end{align}
$$


线色散本领
$$
D_l = fD_{\theta} = f \frac{k}{d \cos\theta_k}
$$

两个很接近的波长产生的两个主极大分开的角度, 刚好等于此波长处的半角宽度时, 根据瑞利判据, 刚好可以分辨这两条谱线, 光栅的色分辨本领 $R$ 由此定义
$$
D_{\theta} = \frac{\Delta\theta}{\delta \lambda} 
    \Rightarrow R\equiv \frac{\lambda}{\delta\lambda} = Nk
$$




色分辨本领, 是能够分辨的最小波长差

### 圆孔正入射

$$
I(\theta) = I_0 \left[\frac{2J_1(x)}{x}\right]^2\quad\, ,x=\frac{2\pi a}{\lambda} \sin \theta
$$

口径的最小分辨角, 就是第一暗环角半径
$$
\delta \theta_{\mathrm{min}} \Delta\theta = 1.22 \frac{\lambda}{D}
$$

# 第五章 变换光学

## 屏函数

衍射屏的作用可以集中地用屏函数来表征
$$
\tilde{T}(x, y) = \frac{\tilde{U}_\mathrm{out}(x, y)}     {\tilde{U}_\mathrm{in}(x, y)}
$$
它的模叫振幅变换函数, 它的相位叫做相位变换函数.

## 平面波和球面波的复振幅

球面波

从 $(x_0, y_0, 0)$ 发出的球面波, 在点 $(x, y, z)$ 处的复振幅为
$$
\tilde{U}(x, y ) = \frac{Ae^{\mathrm{i}\phi_0}}{r}e^{\mathrm{i}kr}
$$
其中 $r = \sqrt{(x - x_0)^2 + (y - y_0)^2 + z^2}$ . 在傍轴近似下, 可以在 $x = 0, y = 0 ,x_0 = 0, y_0 = 0$ .  做 Taylor 展开, 并且只保留到二阶项
$$
\begin{align}
r =& |z| + \frac{1}{2}\frac{(x-x_0)^2 + (y-y_0)^2}{|z|} 
     + \mathcal{O}\left\{\left[(x-x_0)^2 + (y - y_0)^2\right]^2\right\} \\
  \approx& |z| + \frac{x_0^2 + y_0^2}{2|z|} + \frac{x^2 + y^2}{2|z|}
      - \frac{xx_0 + yy_0}{|z|}
\end{align}
$$
在复振幅中, 分母中可以直接取领头项 $r\approx |z|$ . 而在指数上, 由于 $k$ 很大, 在不满足远场近似时, 需要保留二阶项. 所以傍轴近似下, 复振幅表示为
$$
\tilde{U}(x, y ) = \frac{Ae^{\mathrm{i}\phi_0}}{|z|}e^{\mathrm{i}k\left( |z| + \frac{x_0^2 + y_0^2}{2|z|} + \frac{x^2 + y^2}{2|z|}
      - \frac{xx_0 + yy_0}{|z|} \right)}
$$
取其复共轭, 即为会聚波.

平面波
$$
\tilde{U}(\vec{r}) = Ae^{\mathrm{i}\phi_0}e^{\mathrm{i}\vec{k}\cdot \vec{r}}
$$

## 傅里叶变换

夫琅禾费积分
$$
\begin{align}
\tilde{U}(x', y') =& Ae^{\mathrm{i}kz}e^{\mathrm{i}k\frac{x'^2 + y^2}{2}}
   \int\mathrm{d}x\int\mathrm{d}y \cdot \tilde{T}(x, y)
     \cdot e^{-\mathrm{i}k\frac{xx' + yy'}{z}} \\
\tilde{U}(\theta_1, \theta_2) =& Ae^{\mathrm{i}\phi(\theta_1, \theta_2)}
   \int\mathrm{d}x\int\mathrm{d}y \cdot \tilde{T}(x, y)
     \cdot e^{-\mathrm{i}k(x\sin\theta_1 + y\sin\theta_2)} \\
\end{align}
$$
都是傅里叶变换的形式. 衍射屏上的一点 $(x, y)$ 就对应一对频率. 衍射屏的大小是有限的, 所以衍射屏会过虑掉一些频率的作用.



## 全息照相

全息底片记录了照片的相位信息
$$
I_H(x, y) = (\tilde{U}_O + \tilde{U}_R) (\tilde{U}_O + \tilde{U}_R)^*
$$


 经过线性冲洗后的透过率函数为 $\tilde{T}_H$ , 用 $\tilde{U}_R'$ 照射后, 透射场为
$$
\begin{align}
\tilde{U}_T =& \tilde{T}_H\tilde{U}_R' = [T_O + \beta I_H(x, y)]\tilde{U}_R'\\ 
  =&(T_0 + \beta A_O^2 + \beta A_R^2)\tilde{U}_R'
  + \beta \tilde{U}_R'\tilde{U}_R^* \tilde{U}_O 
  + \beta \tilde{U}_R'\tilde{U}_R \tilde{U}_O^*
\end{align}
$$
三项分别对应 0, 1, -1 级



# 第六章 偏振

## 马吕斯定律

线偏振光通过检偏器后透射光的强度随 $\theta$ 角变化的规律
$$
I_2 = I_1 \cos^2\theta
$$


## 布儒斯特角

使 p 分量反射率为零的入射角 $i_B$ 称为布儒斯特角. 从介质 $n_1$ 到 $n_2$ 的布儒斯特角为
$$
i_B = \arctan \frac{n_2}{n_1}
$$


## 菲涅耳反射折射公式

$$
\begin{align}
&\left\{
  \begin{array}{c}
  \tilde{r}_p = \frac{\tan(i_1 - i_2)}{\tan(i_1 + i_2)} \\
  \tilde{r}_s = \frac{\sin(i_2 - i_1)}{\sin(i_2 + i_1}
  \end{array}
\right. \\
&\left\{
  \begin{array}{c}
  \tilde{t}_p = \frac{2n_1\cos i_1}{n_2\cos i_1 + n_1 \cos i_2} \\
  \tilde{t}_s = \frac{2n_1\cos i_1}{n_1\cos i_1 + n_2 \cos i_2}
  \end{array}
\right.
\end{align}
$$



## 偏振度

$$
I = \frac{I_{\mathrm{max}} - I_{\mathrm{min}}}{I_{\mathrm{max}} + I_{\mathrm{min}}}
$$



## 强度透射反射率

$$
R = \frac{I_1'}{I_1} = |\tilde{r}|^2
$$


$$
T = \frac{I_2}{I_1} = \frac{n_2}{n_1}|\tilde{t}|^2
$$


## 全反射光的相移

$$
\begin{align}
\left\{
\begin{array}{c}
  \delta_p = 2 \arctan \left( \frac{n_1}{n_2}
     \frac{\sqrt{\left(\frac{n_1}{n_2}\right)^2\sin^2i_1-1}}{\cos i_1}                          \right) \\
\delta_s = 2 \arctan \left( \frac{n_2}{n_1}
\frac{\sqrt{\left(\frac{n_1}{n_2}\right)^2\sin^2i_1-1}}{\cos i_1}                          \right)
\end{array}
\right.
\end{align}
$$



## 双折射

光线垂直于主光轴传播, 可用折射定律

# 第七章 光与物质相互作用

## 布格定律

$$
I = I_0 e^{-\alpha l}
$$

## 科西公式

$$
n = A + \frac{B}{\lambda^2}
$$

## 群速度与相速度的关系

群速度
$$
v_{\mathrm{g}} = \frac{\mathrm{d}\omega}{\mathrm{d}k}
$$


# Reference

- 赵凯华, 新概念物理教程 光学 , 2004, 高等教育出版社 
- Eugene Hecht, Optics, Global Edition, 2017, Pearson Higher Education