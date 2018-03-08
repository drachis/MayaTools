import sys
def syspath():
    print(sys.version)
    print('sys.path:')
    for p in sys.path:
        print ('\t'+p)
if __name__ == '__main__':
    syspath()
