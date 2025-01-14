import PyPDF2
def watermark(in_file , out_file, wat):
    with open(in_file, mode= "rb") as infile , open(wat , mode="rb") as water:
        input_file = PyPDF2.PdfReader(infile)
        watermark = PyPDF2.PdfReader(water)
        writer = PyPDF2.PdfWriter()

        for page_index in range(len(input_file.pages)):
            page = input_file.pages[page_index]
            page.merge_page(watermark.pages[0])
            writer.add_page(page)

        with open(out_file , mode="wb") as out:
            writer.write(out)
watermark("merged.pdf", "final.pdf", "pdfFiles/wtr.pdf")


