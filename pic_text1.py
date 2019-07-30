from PIL import Image
# import argparse
# I=Image.open(r"C:\Users\ls\Desktop\py\wm.png")
# I.show()

# parser = argparse.ArgumentParser()
# parser.add_argument('file')
# parser.add_argument('-o', '--output')
# parser.add_argument('--width', type=int, default=80)
# parser.add_argument('--height', type=int, default=80)
# args = parser.parse_args()
# IMG = args.file
# WIDTH = args.width
# HEIGHT = args.height
# OUTPUT = args.output
ascii_char = list(
    "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# RGB值转字符串
def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256 + 1) / length
    return ascii_char[int(gray / unit)]


if __name__ == '__main__':
    im = Image.open(r"C:\Users\ls\Desktop\py\wm.png")
    im = im.resize((80, 80), Image.NEAREST)
    txt = ""
    for i in range(80):
        for j in range(80):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'
    print(txt)

    # if OUTPUT:
    #     with open(OUTPUT, 'w') as f:
    #         f.write(txt)
    # else:
    with open(r"C:\Users\ls\Desktop\py\output5.txt", 'w') as f:
        f.write(txt)
