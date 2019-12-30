
'''

Reference
https://graus.nu/blog/pylucene-4-0-in-60-seconds-tutorial/
'''

import sys
import lucene

import os
from os import listdir
from os.path import isfile, isdir, join
from java.io import File
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.document import Document, Field
from org.apache.lucene.index import IndexWriter, IndexWriterConfig
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.util import Version

lucene.initVM()

#filePath = "D:\\Phelps\\GitHub\\Python\\Light-tools\\pylucene\\data\\";  # folder name
filePath = '/tmp/data/pylucene/'
files = listdir(filePath)

#luceneDefinition():
# lucene.initVM()
# indexDir = SimpleFSDirectory(File("/tmp/data/pylucene/index/"))
# writerConfig = IndexWriterConfig(Version.LUCENE_8_1_1, StandardAnalyzer())
# writer = IndexWriter(indexDir, writerConfig)

def luceneindex(text):
  for n, l in enumerate(text):
    doc = Document()
    doc.add(Field("text", l, Field.Store.YES, Field.Index.ANALYZED))
    writer.addDocument(doc)
    #print( "Indexed %d lines from stdin (%d docs in index)" % (n, writer.numDocs()))
    #print( "Closing index of %d docs..." % writer.numDocs())
    writer.close()

def readdata(path):
  f = open(path, 'r', encoding="utf-8")
  data = f.read()
  #print(len(data))
  luceneindex(data)
  f.close()


if (os.path.exists(filePath)):
  for fileName in files:
    fullpath = join(filePath, fileName)
    if isfile(fullpath):
      readdata(fullpath)
    elif isdir(fullpath):
      print("folder：", fileName)


if __name__ == "__main__":
  indexDir = SimpleFSDirectory(File("index/"))
  writerConfig = IndexWriterConfig(Version.LUCENE_8_1_1, StandardAnalyzer())
  writer = IndexWriter(indexDir, writerConfig)
  for n, l in enumerate(sys.stdin):
    doc = Document()
    doc.add(Field("text", l, Field.Store.YES, Field.Index.ANALYZED))
    writer.addDocument(doc)
  writer.close()
