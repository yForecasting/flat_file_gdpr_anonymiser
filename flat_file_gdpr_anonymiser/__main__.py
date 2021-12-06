#! /usr/bin/python

import pandas as pd
# Using the grafton anonymise function
from grafton import anonymise

# replace the original data by the anonymised data
def main():
    # execute anonymisation process
    # Calling grafton
    anonymise(pseudonyms_file="pseudonyms.csv", consent_file ="consent.csv", flat_file="flatfile.csv", export_file="flatfile_dataexport_consent.csv")


if __name__ == '__main__':
    main()
