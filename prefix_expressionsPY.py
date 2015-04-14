import sys

def prefix_expressions(expression):

	start_position = int(len(expression)/2)
	result = int(expression[start_position])

	for x in range(0,start_position):

		operator = expression[start_position-x-1]
		current_number = int(expression[start_position+x+1])

		if(operator == '+'):
			result = result + current_number
		elif(operator == '*'):
			result = result * current_number
		else:
			result = result / current_number

	print(result)

test_cases = open('test_cases','r')

for line in test_cases:
	line = line.strip().split(' ')
	prefix_expressions(line)