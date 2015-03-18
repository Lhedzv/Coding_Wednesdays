def panagrams(text_line):

	array_to_line = list(text_line)
	
	array_to_line = [ord(c.lower())-97 for c in array_to_line]


	array_of_ascii = [0]*26


	for x in range(0,len(array_to_line)):
		current_char = array_to_line[x]

		if(current_char >= 0 and current_char<len(array_of_ascii)):
			array_of_ascii[current_char] += 1


	not_on_array = []

	for x in range(0,len(array_of_ascii)):
		if(array_of_ascii[x] == 0):
			not_on_array.append(x + 97)

	if(len(not_on_array) > 0):
		print(''.join(chr(i) for i in not_on_array))
	else:
		print('NULL')



test_cases = open('test_cases','r')

for line in test_cases:

	line = line.strip().replace(' ', '')
	panagrams(line)