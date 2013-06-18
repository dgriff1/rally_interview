

def split_on_period( number ):
	if "." in number:
		return number.split(".") 
	else:
		return [ number, '00']

look_ups = {
	1 : "one",
	2 : "two",
	3 : "three",
	4 : "four",
	5 : "five",
	6 : "six",
	7 : "seven",
	8 : "eight",
	9 : "nine",
	10 : "ten",
	11 : "eleven",
	12 : "twelve",
	13 : "thirteen",
	14 : "fourteen",
	15 : "fifteen",
	16 : "sixteen",
	17 : "seventeen",
	18 : "eighteen",
	19 : "nineteen",
	20 : "twenty",
	30 : "thirty",
	40 : "forty",
	50 : "fifty",
	60 : "sixty",
	70 : "seventy",
	80 : "eighty",
	90 : "ninety",
}

def convert_to_str( number ):
	if not number:
		return ''
	elif int(number) in look_ups.keys() :
		return look_ups[int(number)]
	elif len(number) == 2:
		return look_ups[ int(number[0] + "0" ) ] + "-" + look_ups[ int(number[1]) ]
	else:
		raise Exception("Invalid Number %s " % number ) 

def convert_by_place( number, offset = 0):
	if not number:
		return ""
	elif offset == 0:
		return convert_by_place(number[:-2], 2) + convert_to_str( number[-2:] ) 
	elif offset == 2:
		return convert_by_place(number[:-1], 3) + convert_to_str( number[-1:] ) + " hundred and "
	elif offset == 3:
		return convert_by_place(number[:-2], 5) + convert_to_str( number[-2:] ) + " thousand, "
	elif offset == 5:
		return convert_by_place(number[:-1], 6) + convert_to_str( number[-1:] ) + " hundred and "
	elif offset == 6:
		return convert_by_place(number[:-2], 8) + convert_to_str( number[-2:] ) + " million, "
	elif offset == 8:
		return convert_by_place(number[:-1], 9) + convert_to_str( number[-1:] ) + " hundred and "
	return ""

def to_fraction( number ):
	return " and %s/100 dollars" % number


def readable_number( num ):
	try:
		float(num)
	except ValueError:
		raise ValueError("%s is not a valid number" % (num))

	(dollars, cents) = split_on_period(num)
	return convert_by_place(dollars) + to_fraction( cents )  


if __name__ == "__main__":
	import sys
	if len(sys.argv) == 2:
		print readable_number( sys.argv[1] )
	else:
		print "No number specified"
