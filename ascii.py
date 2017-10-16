#!/usr/bin/python
# _*_ coding:utf-8 _*_

__author__ = 'Svend'

from PIL import Image
import argparse


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    gary = (2126 * r + 7152 * g + 722 * b) / 10000
    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    # gary / 256 = x / len(ascii_char)
    x = int(gary / (alpha + 1.0) * len(ascii_char))
    return ascii_char[x]


def write_file(out_file_name, content):
    with open(out_file_name, 'w') as f:
        f.write(content)


def main(file_name, img_width, img_height, out_file_name):
    im = Image.open(file_name)
    im = im.resize((img_width, img_height), Image.NEAREST)
    txt = ''
    for i in range(img_height):
        for j in range(img_width):
            content = im.getpixel((j, i))
            txt += get_char(*content)
        txt += '\n'
    print(txt)
    write_file(out_file_name, txt)


def parse_args():
    """
    参数解析
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('out_file')
    parser.add_argument('--width', type=int, default=50)
    parser.add_argument('--height', type=int, default=50)

    args = parser.parse_args()
    img_width, img_height, input_file_name, out_file_name = \
        args.width, args.height, args.input_file, args.out_file

    return img_width, img_height, input_file_name, out_file_name


if __name__ == '__main__':
    width, height, input_file, out_file = parse_args()
    main(file_name=input_file, img_width=width, img_height=height, out_file_name=out_file)

