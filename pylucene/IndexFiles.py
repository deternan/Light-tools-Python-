#!/usr/bin/env python

'''
version: December 31 2019, 10:00 AM
Last revision: December 31 2019, 01:46 PM

Author : Chao-Hsuan Ke
'''

"""
This class is loosely based on the Lucene (java implementation) demo class
org.apache.lucene.demo.IndexFiles.  It will take a directory as an argument
and will index all of the files in that directory and downward recursively.
It will index on the file path, the file name and the file contents.  The
resulting Lucene index will be placed in the current directory and called
'index'.
"""

base_dir = '/tmp/data/pylucene/data/'
INDEX_DIR = '/tmp/data/pylucene/index/'

import sys, os, lucene, threading, time
from datetime import datetime

from java.nio.file import Paths
from org.apache.lucene.analysis.miscellaneous import LimitTokenCountAnalyzer
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.document import Document, Field, FieldType
from org.apache.lucene.index import FieldInfo, IndexWriter, IndexWriterConfig, IndexOptions
from org.apache.lucene.store import SimpleFSDirectory

queryField = 'contents'

class Ticker(object):

    def __init__(self):
        self.tick = True

    def run(self):
        while self.tick:
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(1.0)

class IndexFiles(object):
    """Usage: python IndexFiles <doc_directory>"""
    # data source, index storage
    #def __init__(self, root, storeDir, analyzer):
    def __init__(self, sourceDir, storeDir, analyzer):

        if not os.path.exists(storeDir):
            os.mkdir(storeDir)

        store = SimpleFSDirectory(Paths.get(storeDir))
        analyzer = LimitTokenCountAnalyzer(analyzer, 1048576)
        config = IndexWriterConfig(analyzer)
        config.setOpenMode(IndexWriterConfig.OpenMode.CREATE)
        writer = IndexWriter(store, config)

        self.indexDocs(sourceDir, writer)
        ticker = Ticker()
        print('index ...')
        threading.Thread(target=ticker.run).start()
        writer.commit()
        writer.close()
        ticker.tick = False
        print('done')

    def indexDocs(self, sourceDir, writer):

        t1 = FieldType()
        t1.setStored(True)
        t1.setTokenized(False)
        t1.setIndexOptions(IndexOptions.DOCS_AND_FREQS)

        t2 = FieldType()
        t2.setStored(False)
        t2.setTokenized(True)
        t2.setIndexOptions(IndexOptions.DOCS_AND_FREQS_AND_POSITIONS)

        for sourceDir, dirnames, filenames in os.walk(sourceDir):
            for filename in filenames:
                if not filename.endswith('.txt'):
                    continue
                print(filename)
                try:
                    path = os.path.join(sourceDir, filename)
                    file = open(path, 'r', encoding="utf-8")
                    contents = file.read()
                    #contents = str(filecontent, 'utf-8')
                    #contents = filecontent.encode('utf-8')
                    #print('path', path, len(contents))
                    doc = Document()
                    doc.add(Field("name", filename, t1))            # filename (title)
                    #doc.add(Field("path", root, t1))
                    if len(contents) > 0:
                        doc.add(Field(queryField, contents, t2))    # content
                    else:
                        print("warning: no content in %s" % filename)
                    writer.addDocument(doc)
                    file.close()
                except NameError:
                    print("Failed in indexDocs:")

if __name__ == '__main__':
    lucene.initVM(vmargs=['-Djava.awt.headless=true'])
    #print 'lucene', lucene.VERSION
    start = datetime.now()
    try:
        IndexFiles(base_dir, INDEX_DIR, StandardAnalyzer())
        end = datetime.now()
        print(end - start)
    except NameError:
        print("File Failed")
        #raise e
