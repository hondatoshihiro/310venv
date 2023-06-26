import os
import HWTargetDir

class HWOutDir(HWTargetDir):

    def __init__(self, filePath):
        #HWTargetDirのコンストラクタ
        super().__init__(filePath)
        #独自のコンストラクタの処理
