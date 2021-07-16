# pdf_splitting.py

from PyPDF2 import PdfFileReader, PdfFileWriter
"""
split function takes three arguements:
1. path: in this arg we have to specify the path of inputted pdf path
2. name_of_split: in this we can pass name of split by which are modified file name comes
3.from_: in this args we can pass the starting point from where we want to start to 
split the pdf
4.to_: in this args we can pass the ending point upto this we want to split
"""
def split(path, name_of_split,from_=0,to_=0,whole=True):
    pdf_reader = PdfFileReader(path)
    total_pages = pdf_reader.getNumPages()
    if whole:
        pdf = PdfFileReader(path)
        for page in range(pdf.getNumPages()):
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(pdf.getPage(page))

            output = f'{name_of_split}{page}.pdf'
            with open(output, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)
        return

    if (from_ < total_pages) and (to_ < total_pages) and (from_ <= to_):
        for page in range(from_,to_):
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(pdf_reader.getPage(page))
    else:
        from_ = 0
        to_ = total_pages//2
        for page in range(from_,to_):
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(pdf_reader.getPage(page))
    output = f'{name_of_split}{page}.pdf'
    with open(output, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)




if __name__ == '__main__':
    path = 'F:\pdf\dp.pdf'
    split(path, 'jupyter_page')