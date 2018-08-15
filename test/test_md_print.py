import os
import unittest

import md_parser
import md_print


class TestMdPrint(unittest.TestCase):

    def test_print(self):
        '''
        Not really a test, just to show how it is used and what the output
        looks like.
        '''
        curdir = os.path.dirname(__file__)
        para = md_parser.parse(os.path.join(curdir, 'test_md_parser.md'))
        print("** sequence paragram **")
        md_print.print_paragraph(para)
        print("** rules **")
        md_print.print_rules(para)
        print("** paragraph on level 1 with number of children > 1 **")
        md_print.print_split(para, 1)


if __name__ == '__main__':
    unittest.main()
