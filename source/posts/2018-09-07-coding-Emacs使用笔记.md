---
title: Emacs使用笔记
date: 2018/09/07
categories: 软件使用
tags: [Emacs, 快捷键]
---

<!-- toc -->

<!-- more -->

### 修改配色

打开Emacs的配置文件。配置文件在~/.emacs。增加：

> (set-background-color "black") ;; 使用黑色背景
> (set-foreground-color "white") ;; 使用白色前景
> (set-face-foreground 'region "green")  ;; 区域前景颜色设为绿色
> (set-face-background 'region "blue") ;; 区域背景色设为蓝色

尽管可以重启Emacs使配置生效，但更快捷的方式是在打开~/.emacs的时候执行命令M-x eval-buffer，就可以使配置文件立即生效。

### 快捷键

中文帮助：`C-h t` 

撤消：`C-x u` `C-/` 

启动自动折行模式：` M-x auto-fill-mode <Return> ` 

相关命令搜索（Command Apropos）：`C-h a` 

Emacs 使用手册（manual）：`C-h r` 

自动补全：`M-/`     

在另一个窗口打开缓冲：`C-x 4 b`     

复制：`M-w` 

把当前进程放到后台（之后可用''fg''命令回到前台）： `Ctrl Z`   

清屏：`ctrl L`

### 打开

终端模式：`emacs -nw`

### 配置备份

```lisp
;;用xetex编译,以支持中文
(setq-default TeX-engine 'xetex)
;;默认输出pdf
(setq-default TeX-PDF-mode t)

;;ELPA (Emacs Lisp Package Archive)扩展插件管理,用命令`package-list-packages`调用.
;;主题网站https://emacsthemes.com/ 
(require 'package)
(add-to-list 'package-archives 
             '("melpa" . "http://melpa.org/packages/"))
(package-initialize)

;;加载主题
(load-theme 'light-blue t)
;;auctex插件
(load "auctex.el" nil t t)
(load "preview-latex.el" nil t t)
(setq TeX-auto-save t)
(setq TeX-parse-self t)
(setq-default TeX-master nil)

;;在 LaTeX mode 中，默认开启 PDF mode，即默认使用 xelatex 直接生成 pdf 文 件，而不用每次用 'C-c C-t C-p' 进行切换。设置 'Tex-show-compilation' 为 t，在另一个窗口显示编译信息，对于错误的排除很方便。另外，编译时默认直接 保存文件，绑定补全符号到 TAB 键。
(add-hook 'LaTeX-mode-hook
          (lambda ()
            (setq TeX-auto-untabify t     ; remove all tabs before saving
                  TeX-engine 'xetex       ; use xelatex default
                  TeX-show-compilation t) ; display compilation windows
            (TeX-global-PDF-mode t)       ; PDF mode enable, not plain
            (setq TeX-save-query nil)
            (imenu-add-menubar-index)
            (define-key LaTeX-mode-map (kbd "TAB") 'TeX-complete-symbol)))


;;自动换行，数学公式，reftex，显示号
(mapc (lambda (mode)
      (add-hook 'LaTeX-mode-hook mode))
      (list 'auto-fill-mode
            'LaTeX-math-mode
            'turn-on-reftex
            'linum-mode))
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(package-selected-packages (quote (pyim nord-theme))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )

(elpy-use-ipython)

; python-mode
(setq py-install-directory "~/.emacs.d/python-mode-6.0.11")
(add-to-list 'load-path py-install-directory)
(require 'python-mode)

; use IPython
(setq-default py-shell-name "ipython")
(setq-default py-which-bufname "IPython")
; use the wx backend, for both mayavi and matplotlib
(setq py-python-command-args
  '("--gui=wx" "--pylab=wx" "-colors" "Linux"))
(setq py-force-py-shell-name-p t)

; switch to the interpreter after executing code
(setq py-shell-switch-buffers-on-execute-p t)
(setq py-switch-buffers-on-execute-p t)
; don't split windows
(setq py-split-windows-on-execute-p nil)
; try to automagically figure out indentation
(setq py-smart-indentation t)


(setq TeX-view-program-list
      '(("SumatraPDF" "SumatraPDF.exe %o")
        ("Gsview" "gsview32.exe %o")
        ("Okular" "okular --unique %o")
        ("Evince" "evince %o")
        ("Firefox" "firefox %o")))
 ((eq system-type 'gnu/linux)
  (add-hook 'LaTeX-mode-hook
            (lambda ()
              (setq TeX-view-program-selection '((output-pdf "Okular")
                                                 (output-dvi "Okular")))))))


(add-to-list 'load-path "/home/dx/Downloads/neotree")
(require 'neotree)
(global-set-key [f8] 'neotree-toggle)

(require 'sr-speedbar)

```

