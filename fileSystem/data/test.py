#!coding=utf-8

import os

f =open("2015-11-16 10:00:00")

try:
	lists=f.readlines()
	print lists
	print lists[1]

	time=lists[1].split("#")
	print time
	#for list in lists:
	#	print list

finally:
	f.close()