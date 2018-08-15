import os
import unittest

import md_parser
from md_parser import Headline
import md_iter


class TestMdPraser(unittest.TestCase):

    def test_parse(self):
        (0, 45, 3, 9, 27, 29, 10)
        expects = (
            (Headline(level=0, name='root', title='main'), 0),
            (Headline(level=1, name='main', title='C++ Core Guidelines'), 45),
            (Headline(level=3, name='SS-readers',
                      title='In.target: Target readership'), 3),
            (Headline(level=2, name='SS-aims', title='In.aims: Aims'), 9),
            (Headline(level=3, name='R0', title="In.0: Don't panic!"), 27),
            (Headline(level=2, name='SS-struct',
                      title='In.struct: The structure of this document'), 29),
            (Headline(level=1, name='S-introduction',
                      title='In: Introduction'), 10),
        )

        curdir = os.path.dirname(__file__)
        para = md_parser.parse(os.path.join(curdir, 'test_md_parser.md'))
        self.assertEqual(expects, tuple((s.head, len(s.content))
                                        for s in md_iter.sequence_iter(para)))
        self.assertEqual(len(para.children[0].content), 45)


if __name__ == '__main__':
    unittest.main()
