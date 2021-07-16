from PyPDF2 import PdfFileReader, PdfFileWriter
""""
this is the function which take two args:
1. paths -> in paths we have list of all pdf documents path to be merged
2. output-> in output we defined one destination file or our output file where we
   will store the result of our merged file. 
"""
def merge_pdfs(paths, output):
    #making object of PdfFileWriter writer
    pdf_writer = PdfFileWriter()
    #we are iterating to all the file present in the paths
    for path in paths:
        #making PdfFileReader object by initializing the path
        pdf_reader = PdfFileReader(path)
        """
        getNumPages()-> function return the total number of pages in the pdf
        getPage(page_number)-> function return the content of the specified page 
        we are iterating to each and every pages
        As we have initialize our PdfWriter with merged.pdf all the pages from the pdf
        will one by one added to the output
        """
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))
            with open(output, 'wb') as out:
                pdf_writer.write(out)

    """
    //first we create the file writer object
    //if no file present then new file with this name will be created
    f = FileWriter("merged.pdf","wb")
    //then we pass that file writer object to pdf file writer
    pdf_writer = PdfWriter(f)
    // then we will add the pages
    pdf_writer.addPages()
    """


if __name__ == '__main__':
    #we can n number of files
    paths = ['F:\pdf\Tree1.pdf','F:\pdf\ex1.pdf', 'F:\pdf\Tree2.pdf','F:\pdf\Aniket.pdf','F:\pdf\Aniket.pdf','F:\pdf\ex.pdf']
    merge_pdfs(paths, output='merged.pdf')