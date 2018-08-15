import md_iter


def print_paragraph(para):
    '''
    print the paragraph sequentially
    '''
    total = 0
    for p in md_iter.sequence_iter(para):
        total += 1
        print('{}title:{}, name: {}, lines {}, targets {} children {}'
              .format(' '*4*p.head.level,
                      p.head.title[:min(
                          len(p.head.title), 40)],
                      p.head.name,
                      len(p.content),
                      len(p.link_target),
                      len(p.children)))
    return total


def print_rules(para):
    '''print all rules
    rules are headline with sub-paragraph `reason`
    '''
    total = 0
    for p in md_iter.sequence_iter(para):
        if para.children and para.children[0].head.title.lower() == 'reason':
            total += 1
            print('{}title:{}, name: {}, lines {}, children {}'
                  .format(' '*4*para.head.level,
                          para.head.title[:min(
                              len(para.head.title), 40)],
                          para.head.name,
                          len(para.content),
                          len(para.children)))
    return total


def print_level(para, max_level):
    '''
    print level by level includes the contents but not sub-paragraph
    '''
    total, num_lines, cur_level = 0, 0, 0
    for p in md_iter.level_iter(para):
        if p.head.level > max_level:
            return

        if p.head.level != cur_level:
            if cur_level > 0:
                print(' -- summary -- total Paragraphs: ',
                      total, 'content lines', num_lines)

            total, num_lines, cur_level = 0, 0, p.head.level

        if p.head.level > 0:
            num_lines += len(p.content)
            print('{}title:{}, name: {}, lines {}, children {}'
                  .format(' '*4*(p.head.level-1),
                          p.head.title[:min(
                              len(p.head.title), 40)],
                          p.head.name,
                          len(p.content),
                          len(p.children)))


def print_split(para, split_level):
    for p in md_iter.sub_para_iter(para, split_level):
        print('{}title:{}, name: {}, lines {}, children {}'
              .format(' '*4*(p.head.level-1),
                      p.head.title[:min(
                          len(p.head.title), 40)],
                      p.head.name,
                      len(p.content),
                      len(p.children)))
