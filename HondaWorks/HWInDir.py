import os

class HWInDir:

    def __init__(self, filePath):
        self.fileList = []
        self.dirList = []
        self.filePath = filePath
        workList = os.listdir(self.filePath)
        for work in workList:
            if os.path.isfile(os.path.join(self.filePath, work)):
                self.fileList.append(work)
            else:
                self.dirList.append(work)

    def getFileList(self):
        return self.fileList
    
    def getDirList(self):
        return self.dirList
    
    def getFilePath(self, fileName):
        return os.path.join(self.filePath, fileName)
    
    def getDirPath(self, dirName):
        return os.path.join(self.filePath, dirName)

#動作確認
if __name__ == '__main__':
    testInDir = HWInDir("d:\\python\\venv\\310venv\\HondaWorks")
    fileList = testInDir.getFileList()
    for file in fileList:
        print(testInDir.getFilePath(file))
    dirList = testInDir.getDirList()
    for dir in dirList:
        print(testInDir.getDirPath(dir))
