def find_max(*args) -> str:
    sort_list = sorted(args)
    max_element = sort_list[-1]
    return f'Maximum value it is {max_element}'


if __name__ == '__main__':
    print(find_max(1, 2, 10, 3, 15, 12, 11))
