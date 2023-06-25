import os
import datetime

class HWTargetFile:

    #ファイル名を含んだフルパスを引数として渡す
    def __init__(self, fileFullPath):
        self.fileFullPath = fileFullPath

    def getCreateTimeStr(self):
        mtime = os.stat(self.fileFullPath).st_mtime
        dtTimeStamp = datetime.datetime.fromtimestamp(mtime)
        strTimeStamp = dtTimeStamp.strftime('%Y-%m-%d')
        return strTimeStamp

#動作確認
if __name__ == '__main__':
    testInDir = HWTargetFile("d:\\python\\venv\\310venv\\HondaWorks\\test.ini")
    print(testInDir.getCreateTimeStr())
