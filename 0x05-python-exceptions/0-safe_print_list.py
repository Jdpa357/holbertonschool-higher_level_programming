#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
	try:
		result = my_list.__len__()
		print('%s' % ''.join(map(str, my_list[:x])))
		return (result)
	except:
		print("An unknow error")
