import sys


def main(filename: str):
    items = set()
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip().lower()
            line = ''.join(c for c in line if c.isalnum() or c == '-').strip('-')
            if len(line) == 0:
                continue
            items.add('site:'+line)
    with open(filename+'.items', 'w') as f:
        f.write('\n'.join(items)+'\n')

if __name__ == '__main__':
    for filename in sys.argv[1:]:
        main(filename)

