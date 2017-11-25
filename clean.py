#!/usr/bin/env python3
"""A simple pdf cleaner which removes redundant pages, i.e. animations from presentation slides."""
import argparse
from copy import copy
from PyPDF2 import PdfFileReader, PdfFileWriter


def clean_pdf_pages(args: argparse.Namespace):
    """Remove redundant pages of a pdf."""
    with open(args.source, 'rb') as source_file, open(args.target, 'wb') as target_file:
        in_pdf = PdfFileReader(source_file)
        page_count = in_pdf.getNumPages()

        out_pdf = PdfFileWriter()

        prev_page = in_pdf.getPage(0)
        for page_number in range(1, page_count):
            page = in_pdf.getPage(page_number)
            if page.extractText() != prev_page.extractText():
                out_pdf.addPage(prev_page)
            prev_page = page

        # add last page
        out_pdf.addPage(prev_page)

        out_pdf.write(target_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('source')
    parser.add_argument('target')
    args = parser.parse_args()
    clean_pdf_pages(args)
