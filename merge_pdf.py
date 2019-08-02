from PyPDF2 import PdfFileMerger, PdfFileReader

file_names = [
    'file1.PDF',
    'file2.PDF',
    'file3.PDF'
]

file_path = '/path/to/folder'

merger = PdfFileMerger()
for filename in file_names:
    merger.append(PdfFileReader(file(file_path + filename, 'rb')))

merger.write(file_path + "merged.pdf")
