from ex1 import *
import unittest

class TestEx1(unittest.TestCase):
	
	def test_split_on_period(self):
		self.assertEqual( split_on_period("123.45"), ['123', '45'] )
		self.assertEqual( split_on_period("23"), ['23', '00'] )

	def test_convert_str(self):
		self.assertEqual( convert_to_str("1"), "one" )
		self.assertEqual( convert_to_str("2"), "two" )
		self.assertEqual( convert_to_str("11"), "eleven" )
		self.assertEqual( convert_to_str("12"), "twelve" )
		self.assertEqual( convert_to_str("13"), "thirteen" )
		self.assertEqual( convert_to_str("14"), "fourteen" )
		self.assertEqual( convert_to_str("15"), "fifteen" )
		self.assertEqual( convert_to_str("16"), "sixteen" )
		self.assertEqual( convert_to_str("17"), "seventeen" )
		self.assertEqual( convert_to_str("18"), "eighteen" )
		self.assertEqual( convert_to_str("19"), "nineteen" )
		self.assertEqual( convert_to_str("21"), "twenty-one" )
		self.assertEqual( convert_to_str("32"), "thirty-two" )
		self.assertEqual( convert_to_str("43"), "forty-three" )
		self.assertEqual( convert_to_str("54"), "fifty-four" )
		self.assertEqual( convert_to_str("65"), "sixty-five" )
		self.assertEqual( convert_to_str("76"), "seventy-six" )
		self.assertEqual( convert_to_str("87"), "eighty-seven" )
		self.assertEqual( convert_to_str("98"), "ninety-eight" )
	
	def test_convert_by_place(self):
		self.assertEqual( convert_by_place("3", 0), "three"  )
		self.assertEqual( convert_by_place("24", 0), "twenty-four"  )
		self.assertEqual( convert_by_place("253", 0), "two hundred fifty-three"  )
		self.assertEqual( convert_by_place("4593", 0), "four thousand five hundred ninety-three"  )
		self.assertEqual( convert_by_place("40593", 0), "forty thousand five hundred ninety-three"  )
		self.assertEqual( convert_by_place("840593", 0), "eight hundred forty thousand five hundred ninety-three"  )
		self.assertEqual( convert_by_place("26730598", 0), "twenty-six million seven hundred thirty thousand five hundred ninety-eight"  )
		self.assertEqual( convert_by_place("626730598", 0), "six hundred twenty-six million seven hundred thirty thousand five hundred ninety-eight"  )
		# we just ignore stuff we can't handle
		self.assertEqual( convert_by_place("12345626730598", 0), "six hundred twenty-six million seven hundred thirty thousand five hundred ninety-eight"  )

	def test_to_fraction(self):
		self.assertEqual( to_fraction("12"), " and 12/100 dollars")


	def test_full_conversion(self): 
		self.assertEqual( readable_number(123.56), "One hundred twenty-three and 56/100 dollars")		
		self.assertEqual( readable_number("626730598"), "Six hundred twenty-six million seven hundred thirty thousand five hundred ninety-eight and 00/100 dollars")		
		self.assertEqual( readable_number("2523.04"), "Two thousand five hundred twenty-three and 04/100 dollars")

if __name__ == '__main__':
	unittest.main()
