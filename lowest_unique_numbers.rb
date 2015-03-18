def lowest_unique_numbers(array)

	auxiliar= [0]*9
	lowest_unique_int = 0
	lowest_unique_int_pos = 0
	 for x in 0..array.length()-1
	 	actual_int = array[x].to_i
	 	auxiliar[actual_int-1] += 1
	 end



	 for x in 0..8
	 	
	 	if(auxiliar[x] == 1)
	 		lowest_unique_int = x+1
	 		break
	 	end

	 end

	 for x in 0..array.length()-1
	 	
	 	if(array[x].to_i == lowest_unique_int)
	 		lowest_unique_int_pos = x+1
	 		break
	 	end
	 
	 end

	 puts(lowest_unique_int_pos)

end


File.open('testcases.txt').each_line do |line|
	
	line_splitted = line.strip().split(" ")
	lowest_unique_numbers(line_splitted)

end