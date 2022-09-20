 #include <stdio.h>
 #include <stdlib.h>

 void f(void)
 {
     void* s;
     s = malloc(50); /* 申请内存空间 */
     return;  /* 内在泄漏 - 参见以下资料 */
     /*
      * s 指向新分配的堆空间。
      * 当此函数返回，离开局部变量s的作用域后将无法得知s的值，
      * 分配的内存空间不能被释放。
      *
      * 如要「修复」这个问题，必须想办法释放分配的堆空间，
      * 也可以用alloca(3)代替malloc(3)。
      * （注意：alloca(3)既不是ANSI函数也不是POSIX函数）
      */
 }
 int main(void)
 {
     /* 该函数是一个死循环函数 */
     while (1) f(); /* Malloc函数迟早会由于内存泄漏而返回NULL*/
     return 0;
 }

/* #include <stdio.h> */
/* #include <stdlib.h> */
/* #include <math.h> */
/* int *ivector(long nl, long nh) */
/* { */
/*   int *v; */
/*   v = (int *)malloc((size_t) ((nh-nl+1+1) * sizeof(int))); */
/*   return v-nl+2; */
/* } */

/* int main(){ */
/*   int *a; */
/*   int b[8]; */
/*   int *c; */
/*   c = (int *)malloc(3 * sizeof(int)); */
/*   a = ivector(1, 3); */
/*   printf("------ %lu -------", sizeof(a)); */
/*   printf("\n%p", a); */
/*   printf("\n%p", &a); */

/*   printf("\n%d", b[0]); */
/*   printf("\n%lu", sizeof(*b)); */
/*   free(c); */
/* } */
