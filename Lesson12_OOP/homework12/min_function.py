def find_min(*args) -> str:
    sort_list = sorted(args)
    min_element = sort_list[0]
    return f'Minimum value it is {min_element}'


if __name__ == '__main__':
    print(find_min(1, 4, 10, 3, 15, 12, -11))
