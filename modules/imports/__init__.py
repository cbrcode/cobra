import os.path as path
import glob

def readImports(fn): # Reads all lines that have import in them from a file
    with open(fn, "r") as f:
        finalLn = []
        ln = f.readlines()
        for l in ln:
            if l.lower().startswith("from ") or l.lower().startswith("import "):
                finalLn.append(l)

def parseImport(importStr):
    

def getFileList(dir):
    return glob.glob('**/*.py',recursive=True)    

def handleImports(dir, fileList, folderList):
    finalList = []
    
    newFL = []

    for file in fileList: