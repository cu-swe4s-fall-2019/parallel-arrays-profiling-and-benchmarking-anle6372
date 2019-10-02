import data_viz

def linear_search(key, L):
    if L is None:
        return None
    if len(L) == 0:
        return None
    if not isinstance(L, list):
        raise TypeError('Input must be list')
    for i in range(len(L)):
        curr = L[i]
        if not type(key) == type(curr):
            raise TypeError('key and list elements must be same types')
        if key == curr:
            return i
    return -1

def binary_serach(key, L):
    pass


def main():
    pass

if __name__ == '__main__':
    main()
