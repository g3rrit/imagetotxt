#!/usr/bin/python
import sys
from PIL import Image

def getShadingList(path):
    img = Image.open(path)
    img = img.resize((128,64), Image.ANTIALIAS)
    pxl = img.load()
    print(img.size)

    def getaverage(pixel):
        return (pixel[0] + pixel[1] + pixel[2])/3

    res = {}

    res["size"] = img.size

    print("with: {}", img.size[0])
    
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            res[x,y] = getaverage(pxl[x,y])

    return res

def getChar(val):
    charr = [
            " ",
            ".",
            ",",
            "-",
            ";",
            "+",
            "L",
            "H",
            "M",
            "#"
    ]

    size = len(charr)
    pos = (val / 255) * size

    return charr[int(pos)]

def getHL(lst):
    hi = 0
    low = 255
    for x in range(lst["size"][0]):
        for y in range(lst["size"][1]):
            if lst[x,y] < low:
                low -= 1 
            if lst[x,y] > hi:
                hi += 1

    return (hi,low)


def getCharList(path):
    shlst = getShadingList(path) 
    
    res = {}
    res["size"] = shlst["size"]

    for x in range(shlst["size"][0]):
        for y in range(shlst["size"][1]):
            res[x,y] = getChar(shlst[x,y])

    return res


def main():
    if(len(sys.argv) < 2):
        print("Error! Use picture path as arg")
        return

    path = sys.argv[1] 

    reslst = getCharList(path)
    for y in range(reslst["size"][1]):
        for x in range(reslst["size"][0]):
            print(reslst[x,y], end='')
        print("")


if __name__ == "__main__":
    main()
