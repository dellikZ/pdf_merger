import sys
import PyPDF2


inputs = sys.argv[1:]


def pdf_merger(pdfs_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdfs_list:
		merger.append(pdf)
	merger.write('merged.pdf')


pdf_merger(inputs)
