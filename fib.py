# -*- coding: utf-8 -*-
# @Author: yanyahu
# @Date:   2017-06-23 09:34:55
# @Last Modified by:   yanyahu
# @Last Modified time: 2019-05-07 01:37:06
# yanyahu

def fib(n):
	f1 = f2 = 1
	for k in range(1, n):
		f1, f2 = f2, f1 + f2
	return f2

for i in range(12):
	print fib(i),
