import re
import codecs


def format_file(kif_file_path):
    r = re.compile(r'^\d+')
    cnt = 1
    with open(kif_file_path, "r") as before_file, codecs.open(kif_file_path + '_f', "w", "Shift-JIS", "ignore") as after_file:
        for i in before_file:
            i = i.lstrip()
            m = r.search(i)
            if m:
                i = re.sub(r'^\d+', "", i)
                i = re.sub(r'(右|左)', "", i)
                i = re.sub(r'\(\d\d:\d\d\s*/\s*\d\d:\d\d\:\d\d\)', "", i)
                after_file.write('{: 4}{}'.format(cnt, i))
                cnt += 1
    return kif_file_path + '_f'


# format_file('fujii_imai.kif')
