# -*- coding: utf-8 -*-
import os
import sys
import optparse
from scrapy.cmdline import execute


resource = './resources'


def run_crawler(argv=None):
    argv = ['crawl', 'spider'] if argv is None else argv
    print("Spiders running...")
    for arg in argv:
        sys.argv.append(arg)
    os.environ.setdefault('XDG_CONFIG_HOME', './crawler')
    execute()


def main(argv=None):
    print(sha256('...'))


def usage():
    parser = optparse.OptionParser("usage: %prog -i <input> -o <output>")
    parser.add_option("-i", dest="input", type="string", help="specify input")
    parser.add_option("-o", dest="output", type="string", help="specify output")
    options, args = parser.parse_args()
    if options.input is None:
        print(parser.print_help())
    else:
        main(options)


if __name__ == '__main__':
    run_crawler()
    print('Finished!')