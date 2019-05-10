#!/usr/bin/env python

"""
Converts PDF text content (though not images containing text) to plain text, html, xml or "tags".
"""
import pdfminer.settings
pdfminer.settings.STRICT = False
import pdfminer.high_level
from pdfminer.layout import LAParams
import glob



if __name__ == '__main__':
    codec = 'cp949'
    laparams = LAParams()
    files = glob.glob('*.pdf')
    for fname in files:
        with open(fname, "rb") as fp:
            out_name = fname.split('.')[0]
            print(out_name)
            outfp = open("{}.txt".format(out_name), "w")
            pdfminer.high_level.extract_text_to_fp(fp, outfp, codec=codec,laparams = laparams)
            outfp.close()