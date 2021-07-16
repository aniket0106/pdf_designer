from PyPDF2 import PdfFileReader,PdfFileWriter
# rotate_pages.py

"""
rotate_pages() -> takes three arguements
1. pdf_path : in this we have to pass the user pdf path
2. no_of_pages : in this we have to pass the number of pages we want to rotate if all then by
   default it takes zero then we re-intialize it to total number of pages
3. clockwise : it is default args which take boolean value if its value is True then it
   will right rotate by given angle
   if it is false then it will rotate towards the left by given angle
   
getNumPages() : is the function present in the PyPDF2 which is used to get the total number
                of page present inside the inputted pdf 
                
                
getPage(i) : is the function which return the particular page for the specified pdf

rotateClockwise(angle) : is the function which rotate the specified page by given angle
                         towards to right
rotateCounterClockwise(angle) : is the function which rotate the specified page by given angle
                                towards the left
"""
def rotate_pages(pdf_path,no_of_pages=0,clockwise=True):
    # creating the instance of PdfFileWriter we have already initialize it with our output file
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(pdf_path)
    total_pages = pdf_reader.getNumPages()
    if no_of_pages == 0:
        no_of_pages = total_pages
    if clockwise:
        for i in range(no_of_pages):
            page = pdf_reader.getPage(i).rotateClockwise(90)
            pdf_writer.addPage(page)
            with open('rotate_pages.pdf', 'wb') as fh:
                pdf_writer.write(fh)
        for i in range(no_of_pages,total_pages):
            page = pdf_reader.getPage(i)
            pdf_writer.addPage(page)
            with open('rotate_pages.pdf', 'wb') as fh:
                pdf_writer.write(fh)

    else:
        for i in range(no_of_pages):
            page = pdf_reader.getPage(i).rotateCounterClockwise(90)
            pdf_writer.addPage(page)
            with open('rotate_pages.pdf', 'wb') as fh:
                pdf_writer.write(fh)
        for i in range(no_of_pages,total_pages):
            page = pdf_reader.getPage(i)
            pdf_writer.addPage(page)
            with open('rotate_pages.pdf', 'wb') as fh:
                pdf_writer.write(fh)
    """
    f=FileWriter("rotate_pages.pdf","wb")
    pdf_writer = PdfWriter(f)
    pdf_writer.write()
    """



if __name__ == '__main__':
    path = 'F:\pdf\ex1.pdf'
    rotate_pages(path,no_of_pages=10,clockwise=True)