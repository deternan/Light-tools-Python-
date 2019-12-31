#!/usr/bin/env python

'''
version: December 31 2019, 11:30 AM
Last revision: December 31 2019, 11:56 AM

Author : Chao-Hsuan Ke
'''

"""
This script is loosely based on the Lucene (java implementation) demo class
org.apache.lucene.demo.SearchFiles.  It will prompt for a search query, then it
will search the Lucene index in the current directory called 'index' for the
search query entered against the 'contents' field.  It will then display the
'path' and 'name' fields for each of the hits it finds in the index.  Note that
search.close() is currently commented out because it causes a stack overflow in
some cases.
"""

INDEX_DIR = '/tmp/data/pylucene/index/'

import sys, os, lucene

from java.nio.file import Paths
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher

queryField = 'contents'
queryMaxNum = 100

def run(searcher, analyzer):
    while True:
        print("Hit enter with no input to quit.")
        #command = raw_input("Query:")
        command = input("Query:")
        if command == '':
            return

        print("Searching for:", command)
        query = QueryParser(queryField, analyzer).parse(command)
        scoreDocs = searcher.search(query, queryMaxNum).scoreDocs
        print("%s total matching documents." % len(scoreDocs))

        for scoreDoc in scoreDocs:
            doc = searcher.doc(scoreDoc.doc)
            print('path:', doc.get("path"), 'name:', doc.get("name"))


if __name__ == '__main__':
    lucene.initVM(vmargs=['-Djava.awt.headless=true'])
    directory = SimpleFSDirectory(Paths.get(INDEX_DIR))
    searcher = IndexSearcher(DirectoryReader.open(directory))
    analyzer = StandardAnalyzer()
    run(searcher, analyzer)
    del searcher
