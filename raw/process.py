import re
import sys


def main(filepath: str):
    items = set()
    with open(filepath, 'r') as f:
        for line in f:
            for s in re.findall(r'([^\./]+)\.zhubai\.love', line):
                items.add('site:'+s)
    with open(filepath+'.items', 'w') as f:
        f.write('\n'.join(sorted(items))+'\n')

if __name__ == '__main__':
    main(sys.argv[1])

