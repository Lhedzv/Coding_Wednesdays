def bigdigits(line_splitted):
	
	line_splitted = list(line_splitted)

	string_row_one = '-**----*--***--***---*---****--**--****--**---**--'
	list_row_one = list(string_row_one)

	string_row_two = '*--*--**-----*----*-*--*-*----*-------*-*--*-*--*-'
	list_row_two = list(string_row_two)

	string_row_three = '*--*---*---**---**--****-***--***----*---**---***-'
	list_row_three = list(string_row_three)

	string_row_four = '*--*---*--*-------*----*----*-*--*--*---*--*----*-'
	list_row_four = list(string_row_four)

	string_row_five = '-**---***-****-***-----*-***---**---*----**---**--'
	list_row_five = list(string_row_five)

	string_row_six = '--------------------------------------------------'
	list_row_six = list(string_row_six)

	rows_formatted = [list_row_one,list_row_two,list_row_three,list_row_four,list_row_five,list_row_six]

	line_splitted = [ord(c.lower()) for c in line_splitted]

	for x in range(0,len(line_splitted)):
		

		if(x>=len(line_splitted)):
			pass
		elif(line_splitted[x] >= 48 and line_splitted[x]<=57):
			pass
		else:
			line_splitted.pop(x)
			x = x-1

	line_splitted = [chr(i) for i in line_splitted]
	

	for x in range(0,6):
		
		current_row = ''

		for i in range(0,len(line_splitted)):
			
			current_number = int(line_splitted[i])

			current_row = current_row + ''.join(rows_formatted[x][current_number*5 : current_number*5+5])
	
		print(current_row)





test_cases = open('test_cases','r')


for line in test_cases:
	line_splitted = line.strip()
	bigdigits(line_splitted)