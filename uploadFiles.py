import os
import dropbox
from dropbox.files import WriteMode

class TransferToDropbox:
    def __init__(self, access_key):
        self.access_key = access_key

    def upload_files(self, fromDir, toDir):
        dbx = dropbox.Dropbox(self.access_key)
        for root, Dirs, files in os.walk(fromDir):
            for fileName in files:
                localPath = os.path.join(root, fileName)
                relativePath = os.path.relpath(localPath, fromDir)
                dropboxPath = os.path.join(toDir, relativePath)
                
                with open(localPath, 'rb') as f:
                    dbx.files_upload(f.read(), dropboxPath, mode=WriteMode("overwrite"))


def main():
    access_token = "sl.AxEgBcpglCO06F1E3f6H3nmg2HwWtx2wBGiLKPJuV9n-LBsQ7KW1b0sIbOuFn1FJDpIF-xZIPM-NeJqQjfN60Wm-0W-uPQVv38yDdyrpzZeXLFv_01qaoDW-sdXp1qromGc5UR0"
    transferToDropBox = TransferToDropbox(access_token)
    fileFrom = "./hwFiles/c101HW"
    fileTo = "/CS101HW/myFiles"

    transferToDropBox.upload_files(fileFrom, fileTo)
    print("Files Loaded Successfully")

if __name__ == '__main__':
    main()