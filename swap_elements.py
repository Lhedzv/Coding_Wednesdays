import sys


def swap_elements(array,swap_cases):
	
	array = array.split(' ')
	swap_cases = swap_cases.split(',')

	for x in range(0,len(swap_cases)):
		
		elements_to_swap = swap_cases[x].strip().split('-')
		pos_1 = int(elements_to_swap[0])
		pos_2 = int(elements_to_swap[1])

		auxiliar_element = array[pos_1]
		array[pos_1] = array[pos_2]
		array[pos_2] = auxiliar_element

	print(' '.join(array))

test_cases = open('test_cases','r')

for line in test_cases:
	
	line_splitted = line.strip().split(':')
	swap_elements(line_splitted[0].strip(),line_splitted[1].strip())