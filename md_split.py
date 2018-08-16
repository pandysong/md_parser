import os
import re
import md_iter


def _relink(line, file_name, linkmap):
    '''search the text with pattern `(#some_name)` in `line` and using the
    `some_name` to lookup in map `linkmap` the destination file_name.
    If the destination file_name is same as parameter `file_name`, ignore.
    Otherwise replace the pattern with (file_name#some_name)

    Note that the `file_name` must not contains white spaces otherwise the
    github external link will not work.
    '''

    def _segments():
        '''
        This interator split the line to segments, each segment either is plain
        text or matched the pattern and contain a name.
        '''
        last_end = 0
        for m in re.finditer('\(#.*?\)', line):
            name = m.group()[2:-1]
            start, end = m.span()
            leading_str = line[last_end:start]
            yield leading_str, None  # plain text
            yield line[start:end], name  # contains a link name
            last_end = end
        yield line[last_end:], None

    result = ''
    for orig_text, name in _segments():
        fn = linkmap.get(name) if name else None
        if name and not fn:
            print('warning: link target "{}" not found'.format(name))

        if name and fn and fn != file_name:
            result += '(' + fn + '#' + name + ')'
        else:
            result += orig_text
    return result


def _write_para(file_name, para, linkmap, max_level=None):
    '''write the paragraph `para` to `file_name`

    - `linkmap` contains the maps from linkname to file_name this is used to
    replace the orginal link with new external link.
    - `max_level` indicates to which level of paragraph it will write. the level
    `max_level` is inclusive.
    '''
    with open(file_name, 'w') as f:
        for p in md_iter.sequence_iter(para, include_root=False, max_level=max_level):
            for line in p.content:
                f.write(_relink(line, file_name, linkmap))


def _link_map(linkmap, file_name, para, max_level=None):
    '''add all the links target in para to linkmap'''
    for p in md_iter.sequence_iter(para, include_root=False, max_level=max_level):
        if p.head.name:
            linkmap[p.head.name] = file_name
        for lnk in p.link_target:
            linkmap[lnk] = file_name


def _split_iter(para, split_level):
    ''' split the para to top level (until the level `split_level`) and all
        paragraphs under `split_level`
    '''
    idx = 1
    file_name = '{:02}_{}.md'.format(
        idx, para.head.title).replace(' ', '_').replace(':', '')
    yield file_name, para, split_level

    for p in md_iter.sub_para_iter(para, split_level):
        idx += 1
        file_name = '{:02}_{}.md'.format(
            idx, p.head.title).replace(' ', '_').replace(':', '')

        yield file_name, p, None


def split(para, split_level, out_path):
    '''split the paragraphs into multiple paragraph

    put the Paragraph including level `max_level` to one file, and put their
    children in to separate files.

    more complex seperation algorithm could be constructed with the Paragraph
    tree provided in md_parser.py
    '''

    linkmap = {}
    for fn, p, max_level in _split_iter(para, split_level):
        _link_map(linkmap, fn, p, max_level)

    for fn, p, max_level in _split_iter(para, split_level):
        file_name = os.path.join(out_path, fn)
        _write_para(file_name, p, linkmap, max_level=max_level)
        yield file_name
