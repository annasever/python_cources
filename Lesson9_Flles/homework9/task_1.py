# Create a program to copy a file from one file to another.
with open('main.txt', 'r', encoding='utf-8') as main:
    with open('new_main.txt', 'w', encoding='utf-8') as new_main:
        new_main.writelines(main)
