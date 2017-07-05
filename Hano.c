//将n个盘子从x针借助y针移到z针上。

move(int n,char x,char y,char z)
{
    if(n==1)
      printf("%c-->%c\n",x,z);
    else
    {
      move(n-1,x,z,y);
      printf("%c-->%c\n",x,z);
      move(n-1,y,x,z);
    }
}
