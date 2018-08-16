import md_parser
import md_split

p = md_parser.parse('../CppCoreGuidelines/CppCoreGuidelines.md')
for fn in md_split.split(p, split_level=1,
                         out_path='../CppCoreGuidelines_SmallFiles/guidelines'):
    print("writen file:", fn)
    pass
