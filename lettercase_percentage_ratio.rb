
def lowercase_uppercase_case(array)
	
	lowercases = 0
	uppercases = 0	

			
	for x in 0..array.length()-1
		
		

		if array[x] == array[x].upcase
			uppercases += 1
		else
			lowercases += 1
		end
	
	
	end

	lowercases = (100.00*lowercases/array.length()).to_f.round(2)
	uppercases = (100.00*uppercases/array.length()).to_f.round(2)

	lowercases = '%.2f' % lowercases
	uppercases = '%.2f' % uppercases

	puts("lowercase: " + lowercases.to_s + " uppercase: " + uppercases.to_s)

end

File.open('test_cases.txt').each_line do |line|
	line_splitted = line.strip().split("")
	lowercase_uppercase_case(line_splitted)
end
