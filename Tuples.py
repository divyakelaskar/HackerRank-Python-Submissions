if __name__ == '__main__':
    n = int(raw_input())
    lists = map(int, raw_input().split())
    print hash(tuple(lists))
