import os
import re


file_list = [f for f in os.listdir('./')
             if re.search(r'\.org$', f) or re.search(r'\.md$', f)]

olds = ["想说", "专业笔记", "软件使用", "故事"]
news = ["thinking", "physics", "coding", "story"]


def myreplace(myfile):
    with open(myfile, 'r')as f:
        lines = f.readlines()
    with open(myfile, 'w') as f:
        for line in lines:
            res = re.search(r'(\.\/)?(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})-(?P<category>想说|专业笔记|软件使用|故事)-(?P<url_title>.*)', line)
            if res:
                cat_string = res.string
                for old, new in zip(olds, news):
                    cat_string = cat_string.replace(old, new)
                print('---', line)
                new_line = line.replace(res.string, cat_string)
                print('==>', new_line)
                f.writelines(new_line)
            else:
                f.writelines(line)

for myfile in file_list:
    myreplace(myfile)


print('====================')
