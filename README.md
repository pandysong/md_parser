# `CppCoreGuidelines` markdown parser

This parser is for parsing the markdown file in following project and it also
provides utilities to split the big markdown file to small pieces

```
https://github.com/isocpp/CppCoreGuidelines
```

## Initiatives

People raised an issue
[here](https://github.com/isocpp/CppCoreGuidelines/issues/923), and complained
about the big files.

The purpose for this project is for helping this issue.

## Modules

### `md_parser`

Following function parse the `file_path` to Paragraphs tree.

```
def parse_markdown(file_path):
```

Each node  have following `namedtuple` `Paragraph`, which has head (defined in
Headline) and content (a list of lines), `link_target` (the list of link
target/destination that the content contains), children (a list of Paragraph)

```
Headline = namedtuple('Headline', 'level name title')
Paragraph = namedtuple('Paragraph', 'head content link_target children')

```

### `md_iter`

This includes several iterator which traverse the above Paragraph tree.

### unit test

```
$ python -m unittest test/test_md_parser.py
```
