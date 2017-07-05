# -*- coding: utf-8 -*-
# @Author: yanyahu
# @Date:   2017-06-23 09:34:55
# @Last Modified by:   yanyahu
# @Last Modified time: 2017-06-26 10:59:09


def fib(n):
	f1 = f2 = 1
	for k in range(1, n):
		f1, f2 = f2, f1 + f2
	return f2

for i in range(10):
	print fib(i),