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
    '''iterate through paragraphs of which depth == level
    for example in following case:

    # 1
    ## 2
    ## 3
    # 4
    ## 5
    ## 6

    It will yield paragraph #1 and #4 (but its content is removed)
    The yield #1 represents only includes its children #2 and #3
    The yield #4 represents only includes its children ##5 and ##6

    The purpose of this iterator is to gather all the content under level
    `level`
    '''
    if para.head.level == level and para.children:
        yield Paragraph(para.head, content=[], link_target=[],
                        children=para.children)
    else:
        for p in para.children:
            yield from sub_para_iter(p, level)
