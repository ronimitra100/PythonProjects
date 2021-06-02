import PyPDF2
import sys

# Run file by using the following command : >python pdfmerger.py dummy.pdf twopage.pdf

inputs = sys.argv[1:0]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')


pdf_combiner(inputs)
