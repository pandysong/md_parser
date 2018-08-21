import sys
import md_parser
import md_split


def do_split(markdown_file, output_path, verbose=0):
    p = md_parser.parse(markdown_file)
    for fn in md_split.split(p, split_level=1,
                             out_path=output_path):
        if verbose:
            print("writen file:", fn)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('usage:\n'
              '  python {} input.md output_path'.format(sys.argv[0]))
    else:
        do_split(sys.argv[1], sys.argv[2])
