#!/usr/bin/python3
# -*- coding: utf-8 -*-
# pip install black
# pip install flake
"""
Вариант 8. Написать программу, которая считывает текст из файла и выводит на экран только цитаты,
то есть предложения, заключенные в кавычки.
"""


def main(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        for line in file:
            start = line.find('"')
            while start != -1:
                end = line.find('"', start + 1)
                if end != -1:
                    print(line[start + 1:end])
                    start = line.find('"', end + 1)
                else:
                    break


if __name__ == "__main__":
    main('text.txt')
