import os


def root_dir():
    root = os.path.dirname(__file__)
    while True:
        md_file = os.path.join(root,'readme.md')
        if os.path.exists(md_file):
            break
        root = os.path.dirname(root)
    return root



if __name__ == '__main__':
    print(root_dir())



