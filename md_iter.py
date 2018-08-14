import queue
from md_parser import Paragraph


def sequence_iter(para, include_root=True, max_level=None):
    '''iterate through paragraphs in original/sequential order'''
    if not max_level or para.head.level <= max_level:
        if include_root:
            yield para
        for p in para.children:
            yield from sequence_iter(p, max_level=max_level)


def level_iter(para):
    '''iterate through paragraphs level by level'''
    q = queue.Queue()
    q.put(para)
    while not q.empty():
        cur = q.get()
        yield cur
        for p in cur.children:
            q.put(p)


def sub_para_iter(para, level):
    '''iterate through paragraphs which depth = level
    if the parent Paragraph is yield already, its children will not be yield
    '''
    if para.head.level == level and para.children:
        yield Paragraph(para.head, content=[], link_target=[], children=para.children)
    else:
        for p in para.children:
            yield from sub_para_iter(p, level)
