import configparser

class HWIniFile:
    def __init__(self, fileFullPath):
        self.fileFullPath = fileFullPath

    def read(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.fileFullPath, encoding='utf-8')

    def getvalue(self, sectionName, keyName):
        val = self.config.get(sectionName, keyName)
        return val

#動作確認
if __name__ == '__main__':
    testIniFile = HWIniFile("test.ini")
    testIniFile.read()
    print(testIniFile.getvalue("sec01", "key01-01"))
    print(testIniFile.getvalue("sec01", "key01-02"))
    print(testIniFile.getvalue("sec02", "key02-01"))
