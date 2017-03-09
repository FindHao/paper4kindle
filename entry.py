# coding=utf-8
# coding:utf8
from PyPDF2 import PdfFileWriter, PdfFileReader
from copy import copy, deepcopy

output = PdfFileWriter()
input1 = PdfFileReader(open("/home/find/ddown/p97-chung.pdf", "rb"))
# 设置左下角和右上角的坐标

for page in input1.pages:
    upperleft_x = page.mediaBox.getUpperLeft_x()
    upperleft_y = page.mediaBox.getUpperLeft_y()
    upperright_x = page.mediaBox.getUpperRight_x()
    upperright_y = page.mediaBox.getUpperRight_y()
    lowerleft_x = page.mediaBox.getLowerLeft_x()
    lowerleft_y = page.mediaBox.getLowerLeft_y()
    lowerright_x = page.mediaBox.getLowerRight_x()
    lowerright_y = page.mediaBox.getLowerRight_y()
    part1 = copy(page)
    part1.cropBox.lowerLeft = (upperleft_x, upperleft_y / 2)
    part1.cropBox.upperRight = (upperright_x / 2, upperright_y)
    output.addPage(part1)
    part2 = copy(page)
    part2.cropBox.lowerLeft = (upperright_x / 2, upperright_y / 2)
    part2.cropBox.upperRight = (upperright_x, upperright_y)
    output.addPage(part2)
    part3 = copy(page)
    part3.cropBox.lowerLeft = (lowerleft_x, lowerleft_y)
    part3.cropBox.upperRight = (upperright_x / 2, upperright_y / 2)
    output.addPage(part3)
    part4 = copy(page)
    part4.cropBox.lowerLeft = (lowerright_x / 2, lowerright_y)
    # part4.cropBox.upperRight = (611.0, 395.0),
    part4.cropBox.upperRight = (lowerright_x *0.999, upperright_y / 2 ),
    output.addPage(part4)
# print how many pages input1 has:
# print "document1.pdf has %d pages." % input1.getNumPages()
#
# # add page 1 from input1 to output document, unchanged
# output.addPage(input1.getPage(0))
#
# # add page 2 from input1, but rotated clockwise 90 degrees
# output.addPage(input1.getPage(1).rotateClockwise(90))
#
# # add page 3 from input1, rotated the other way:
# output.addPage(input1.getPage(2).rotateCounterClockwise(90))
# # alt: output.addPage(input1.getPage(2).rotateClockwise(270))
#
# # add page 4 from input1, but first add a watermark from another PDF:
# page4 = input1.getPage(3)
# output.addPage(page4)
#
# # add page 5 from input1, but crop it to half size:
# page5 = input1.getPage(4)
# page5.mediaBox.upperRight = (
#     page5.mediaBox.getUpperRight_x() / 2,
#     page5.mediaBox.getUpperRight_y() / 2
# )
# output.addPage(page5)

# finally, write "output" to document-output.pdf
outputStream = file("/home/find/ddown/a.pdf", "wb")
output.write(outputStream)
