import sys


def overlapping_rectangles(line):

	
	trimmed_line = line.split('\n')
	coordinates = (trimmed_line[0].split(','))
	coordinates = [int(i) for i in coordinates]
	
	print(coordinates)

	if(coordinates[6] >= coordinates[0] 
		and coordinates[1] >= coordinates[7] 
		and coordinates[2] >= coordinates[4] 
		and coordinates[3] <= coordinates[5]):
		print('True')
	else:
		print('False')




test_cases = open('testcases.txt','r')

for line in test_cases:
	splitted_line = line.strip().split(',')
	overlapping_rectangles(splitted_line)
