from PyPDF2 import PdfReader, PdfWriter
import sys as s
import copy
from time import sleep
def crop_pdf(input_pdf, output_pdf):
    pdf_reader = PdfReader(input_pdf)
    pdf_writer = PdfWriter()
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        new_page = copy.copy(page)  # Copy the page
        new_page.mediabox.lower_left = (188, 459)
        new_page.mediabox.upper_right = (406, 816)
        pdf_writer.add_page(new_page)
    with open(output_pdf, 'wb') as output_file:
        pdf_writer.write(output_file)

def main() -> int:
    
    a = s.argv 
    del a[0]
    try:
        for i in a:
            crop_pdf(input_pdf=f"{i}", output_pdf=f"{i[:-4]}_edited.pdf")
    except Exception as e:
        print(f"Error: {e}")
        sleep(5)
        
    print("Edited")    
    return 0
    

if __name__ == "__main__":
    main()