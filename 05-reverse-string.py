#!/usr/bin/python3

def reverse_string(a_string):
	new_string = ''
	index = len(a_string)
	while index:
		index -= 1
		new_string += a_string[index]
	return new_string

print(reverse_string('test string'))
