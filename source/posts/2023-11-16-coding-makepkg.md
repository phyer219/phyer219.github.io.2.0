---
title: Arch安装deb包：为 deb 包编写 PKGBUILD 文件
date: 2023/11/16
categories: 软件使用
tags: [Arch, manjaro, makepkg, PKGBUILD]
---

- [前言](#前言)
- [`makepkg` 简介](#makepkg-简介)
- [一个最简单的 `PKGBUILD` 文件](#一个最简单的-pkgbuild-文件)
- [打包流程（一个不 trivial 的测试）](#打包流程一个不-trivial-的测试)
- [deb 包示例：wps-office](#deb-包示例wps-office)

## 前言

使用 Arch, 或者基于 Arch 的 Manjaro 时，有些软件官方仓库里没有，而网上又可以下载到编译好的二进制文件，deb包，或者rpm包。二进制文件可以直接运行，deb或者rpm包解压后，找到对应的二进制文件，也可以直接运行。

但时，它们不被 `pacman` 包管理器管理，也不能从 app lancher 里面便捷的运行。

对于 deb 包，AUR库里有一个 `debtap` 脚本，可以将 deb 包转换成 `pacman -U` 可以直接安装的 `.pkg.tar.zst` 格式。这个脚本非常方便，但是由于这个脚本考虑非常全面，注意普适性，这就导致有时候转换后的 `.pkg.tar.zst` 包会出现一些问题，安装不上。

用 `makepkg` 打包软件是非常简单的事情，只是如果一点也不了解的话，会生怵。但是只要知道了它的运行机理，就会觉得非常简单，而且很多问题也就不存在了。

## `makepkg` 简介

详细地介绍在 ArchWiki 里面都有介绍。在此按我的理解梳理一下。

`makepkg` 是 Arch 系统中的一个软件，它的作用是将写好的程序源代码编译好，并且打包成 `.pkg.tar.zst` 格式，然后发布。大家就可以下载打包好的 `.pkg.tar.zst` 文件在 Arch 上直接安装。

要想用 `makepkg` 打包一个程序，必须先写一个 `PKGBUILD` 文件。系统中有一些示例文件，比如 `/usr/share/pacman/PKGBUILD.proto` 。

写好了 `PKGBUILD` 文件，就可以直接在  `PKGBUILD` 文件所在的目录直接运行

```shell
makepkg
```

然后就生成了 `.pkg.tar.zst` 格式的软件包，然后 `pacman -U` 安装就可以了。

## 一个最简单的 `PKGBUILD` 文件

 `PKGBUILD` 文件使用的是 `shell` 语言。最简单的 `PKGBUILD` 文件如下

```
pkgname=hello-makepkg
pkgver=1.0
pkgrel=1
arch=('x86_64')

package() {
	echo "packaging..."
}
```

前四行定义了四个变量，是软件的名字，版本，以及运行架构。最后三行定义了一个函数，输出一行字 packaging...。

`pkgname` 、 `pkgver` 、 `pkgrel` 、 `arch` 四个变量必须定义。名为 `package()` 的函数会被 `makepkg` 自动执行。

这个最简单的 `PKGBUILD` 文件是 trivial 的，因为它什么也没干，只是走了个过场。

## 打包流程（一个不 trivial 的测试）

下面写一个不 trivial 的 `PKGBUILD` 文件。如下：

```shell
# This is an example PKGBUILD file. Use this as a start to creating your own,
# and remove these comments. For more information, see 'man PKGBUILD'.
# NOTE: Please fill out the license field for your package! If it is unknown,
# then please put 'unknown'.

# Maintainer: Your Name <youremail@domain.com>
pkgname=zqwtest
pkgver=1.0
pkgrel=1
arch=('x86_64')
source=("m.vsix")
md5sums=('541126551a459a74e740ac6a82875d24')


prepare() {
	echo "prepare..."
}

build() {
	echo "building..."
#	pwd
#	cd ${srcdir}
#	pwd
#	mkdir diraa
}

check() {
	echo "checking..."
}

package() {
	echo "packaging..."
	mkdir ${pkgdir}/home
	cp m.vsix ${pkgdir}/home/m.vsix
}
```

`PKGBUILD` 文件所在的目录结构如下：

```shell
.
├── m.vsix
└── PKGBUILD
```

与之前相比，多定义了两个变量，`source` 和 `md5sums` 。这两个变量有什么用处呢？那应该先说一下 `makepkg` 具体都做了什么。

首先，它们通过我们定义的变量，得到软件包的名字，版本号等信息。`source` 变量是告诉 `makepkg` 我们打包过程中所需要的文件，它可以是一个本地文件，也可以是一个文件网址。 `makepkg` 会获取这个文件，验证它的 md5，然后将它放在（链接）目录 `src` 下。 `src` 目录是 `makepkg` 进行一些处理，比如编译，时的工作目录。

接下来， `makepkg` 依次执行四个函数 `prepare()` 、 `build()` 、 `check()` 、 `package()` 。 `prepare()` 一般做编译前的处理，比如解压文件。 `build()` 进行编译。`check()` 检查编译结果。最后 `package()` 进行打包。我们这里的 `prepare()` 、 `build()` 、 `check()` 不进行操作，只输出一行文字提示。

最后，我在函数 `package()` 中，先新建了一个目录 `${pkgdir}/home` 。这里先说明一下，  `makepkg` 会默认定义两个变量：`${srcdir}` 是前面提到的工作路径 `src`；另一个 `${pkgdir}` 是软件包的目录 `pkg/${pkgname}` 。 `${pkgdir}` 目录就是最终打包成 `.pkg.tar.zst` 的目录。在安装包时，`${pkgdir}` 会被安装对应的目录中。比如我们在这个例子中，将文件 `m.vsix` 放在 `${pkgdir}/home/m.vsix` ，那么我们用 `pacman -U` 安装时，就会把 `m.vsix` 复制到 `/home/m.vsix` 。

运行

```shell
makepkg
```

后，目录结构如下

```shell
.
├── m.vsix
├── pkg
│   └── zqwtest
├── PKGBUILD
├── src
│   ├── [Content_Types].xml
│   ├── extension
│   ├── extension.vsixmanifest
│   └── m.vsix -> /home/zqw/pkgtest/m.vsix
└── zqwtest-1.0-1-x86_64.pkg.tar.zst
```

然后我们运行

```shell
sudo pacman -U zqwtest-1.0-1-x86_64.pkg.tar.zst
```

安装一下，就可以看到，如我们所预期，`/home` 目录下多了文件 `m.vsix`：

```shell
/home
├── m.vsix
└── zqw
```

然后我们运行

```shell
sudo pacman -R zqwtest
```

删除软件包，就发现`/home` 目录下的 `m.vsix` 被删除了：

```shell
/home
└── zqw
```

更加多的例子可以去 AUR 仓库里随便找一些看。比如 [quickapp-ide](https://aur.archlinux.org/packages/quickapp-ide) ，可以直接 clone 下来学习。

## deb 包示例：wps-office

我们提前准备好 wps-office 的 deb 格式安装包，并和 `PKGBUILD` 文件放在一起：

```shell
.
├── PKGBUILD
└── wps-office_11.1.0.11698.XA_amd64.deb
```

 `PKGBUILD` 文件如下：

```shell
# This is an example PKGBUILD file. Use this as a start to creating your own,
# and remove these comments. For more information, see 'man PKGBUILD'.
# NOTE: Please fill out the license field for your package! If it is unknown,
# then please put 'unknown'.

# Maintainer: Your Name <youremail@domain.com>
pkgname=wps-office
pkgver=11.1.0.11698
pkgrel=1
arch=('x86_64')
source=("wps-office_11.1.0.11698.XA_amd64.deb")
md5sums=('c80a2b32604cb2a8eb0de456a062fe30')


prepare() {
	mv wps-office_11.1.0.11698.XA_amd64.deb ${pkgver}_${pkgver}.deb
 	ar -x ${pkgver}_${pkgver}.deb
  	mkdir ${pkgname}-${pkgver}
	tar -xf data.tar.xz --directory="${pkgname}-${pkgver}"
}


package() {
  cd "$pkgname-$pkgver"
  cp -r ./ ${pkgdir}/
}
```

这里说明一下， `deb` 包全部解压后会有两个文件夹，`control` 和 `data` 。`control` 类似于我们的  `PKGBUILD` ，包含了软件的信息和安装过程中进行的一些操作。 `data` 类似于 `{pkgdir}` ，包含了需要安装的所有文件。因此我们要做的就是把 `deb` 全部解压，然后将 `data` 目录打包。
