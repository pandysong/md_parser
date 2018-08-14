import re
from collections import namedtuple

Headline = namedtuple('Headline', 'level name title')
Paragraph = namedtuple('Paragraph', 'head content link_target children')


def _headline(line):
    m = re.match(r'(#+)\s<a.*name="(.*)".*/a>(.*)', line, re.M | re.I)
    if m:
        return Headline(len(m.group(1)), m.group(2), m.group(3))
    m = re.match(r'(#+)\s(.*)', line, re.M | re.I)
    if m:
        return Headline(len(m.group(1)), '', m.group(2))
    raise SyntaxError


def _fetch_link_name(line):
    m = re.match(r'\*\s<a.*name="(.*)".*/a>', line, re.M | re.I)
    if m:
        return m.group(1)


def _paragraphs(lines):
    h, content, link_target = None, [], []

    try:
        while True:
            s = next(lines)
            if s.startswith('#'):
                if h:
                    yield (h, content, link_target)
                h, content, link_target = _headline(s), [s], []
            else:
                lnk = _fetch_link_name(s)
                if lnk:
                    link_target += [lnk]
                content += [s]
    except StopIteration:
        if h:
            yield (h, content, link_target)


def _fold_until(stack, target_level):
    prev, children = None, []
    while True:
        cur = stack.pop()
        if prev and cur.head.level < prev.head.level:
            update_cur = Paragraph(cur.head, cur.content, cur.link_target,
                                   cur.children + children)
            stack.append(update_cur)
            if cur.head.level <= target_level:
                break
            prev, children = None, []
        else:
            prev, children = cur, [cur, ] + children


def parse(file_path):
    stack = [Paragraph(Headline(0, 'root', 'main'), content=[], link_target=[],
                       children=[])]

    with open(file_path, 'r') as f:
        for h, c, lnk in _paragraphs(f):
            if stack and stack[-1].head.level > h.level:
                _fold_until(stack, h.level)
            stack.append(Paragraph(h, content=c, link_target=lnk, children=[]))
    _fold_until(stack, 0)
    assert(len(stack) == 1)
    return stack[0]
