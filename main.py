# -*- coding: utf-8 -*-
import optparse
from basics.regression_model import LinearRegression


def scan():
	parser = optparse.OptionParser("usage: %prog -i <input_file> -o <output_file>")
	parser.add_option("-i", dest="input_file", type="string", help="specify input xlsx file")
	parser.add_option("-o", dest="output_file", type="string", help="specify output xlsx file")
	(options, args) = parser.parse_args()
	print(options, args)


def main():
	model = LinearRegression()
	model()


if __name__ == '__main__':
	main()
