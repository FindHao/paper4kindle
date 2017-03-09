# coding=utf-8
"""This is a tool to crop paper pdf to the kindle size
author: FindHao(find@findspace.name)"""
from PyPDF2 import PdfFileWriter, PdfFileReader
from copy import copy
# todo: 暴力裁剪会切断行
import sys

file_name = sys.argv[1]

output = PdfFileWriter()
input1 = PdfFileReader(open(file_name, "rb"))
# 需要裁剪的白边
margin = 40
# 阅读顺序应该是
# 1 3
# 2 4
for page in input1.pages:
    # 由于PyPDF2的一些原因，无法做成循环形式，所以只能写成这么丑陋的。。
    upperleft_x = page.mediaBox.getUpperLeft_x()
    upperleft_y = page.mediaBox.getUpperLeft_y()
    upperright_x = page.mediaBox.getUpperRight_x()
    upperright_y = page.mediaBox.getUpperRight_y()
    lowerleft_x = page.mediaBox.getLowerLeft_x()
    lowerleft_y = page.mediaBox.getLowerLeft_y()
    lowerright_x = page.mediaBox.getLowerRight_x()
    lowerright_y = page.mediaBox.getLowerRight_y()
    part1 = copy(page)
    part1.cropBox.lowerLeft = (upperleft_x + margin, upperleft_y / 2 - margin / 4)
    part1.cropBox.upperRight = (upperright_x / 2, upperright_y - margin)
    output.addPage(part1)
    part2 = copy(page)
    part2.cropBox.lowerLeft = (lowerleft_x + margin, lowerleft_y + margin)
    part2.cropBox.upperRight = (upperright_x / 2, upperright_y / 2 + margin / 4)
    output.addPage(part2)
    part3 = copy(page)
    part3.cropBox.lowerLeft = (upperright_x / 2, upperright_y / 2 - margin / 4)
    part3.cropBox.upperRight = (upperright_x - margin, upperright_y - margin)
    output.addPage(part3)
    part4 = copy(page)
    part4.cropBox.lowerLeft = (lowerright_x / 2, lowerright_y + margin)
    part4.cropBox.upperRight = (lowerright_x - margin, upperright_y / 2 + margin / 4)
    output.addPage(part4)


outputStream = file(file_name[:-4]+"_croped.pdf", "wb")
output.write(outputStream)
