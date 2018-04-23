import os
import xlrd

class read():
    module_path = os.path.dirname(__file__)

    def __init__(self,file):
        self.file = file

    def get_filedata(self):
        url = self.module_path +'/'+ self.file
        return xlrd.open_workbook(url,formatting_info=True)