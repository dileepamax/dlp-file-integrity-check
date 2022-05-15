#/bin/python
from argparse import ArgumentParser
import os.path
import hashlib
from colorama import init
from colorama import Fore, Back, Style

__author__ = 'dileepa'
__appname__ = 'dlp file integrity check'
__appversion__ = '1.0.0'

parser = ArgumentParser()

parser.add_argument('-m', '--method', help='integrity method [sha256, md5]')
parser.add_argument('-f', '--file', help='select file for integrity check')
parser.add_argument('-c', '--checksum', help='checksum in text for varification')
parser.add_argument('-V', '--version', action='version', version=__appversion__)

method = ''
file_path = ''
provided_hash = ''

class Report():
    def __init__(self, method, file, computed_hash, provided_hash, status):
        self.method = method
        self.file = file
        self.computed_hash = computed_hash
        self.provided_hash = provided_hash
        self.status = status
    

class OptionValidation():
    def __init__(self, method, file, provided_hash):
        self.method = method
        self.file = file
        self.provided_hash = provided_hash
    
    def methodValiadation(self):
        if(str(self.method).lower == 'md5'):
            return True
        elif(str(self.method).lower == 'sha256'):
            return True
        else:
            return False
    
    def fileValidation(self):
        if(os.path.exists(self.file)):
            return True
        else:
            return False
    
    def checkSumValidation(self, provided_hash):
        pass

class IntegrityCheck():
    def __init__(self):
        pass
    
    def get_md5sum(self, file):
        checksum = hashlib.md5(open(file,'rb').read()).hexdigest()
        return checksum
    
    def get_sha256sum(self, file):
        checksum = hashlib.sha256(open(file,'rb').read()).hexdigest()
        return checksum

def getOptions():
    global method, file_path, provided_hash
    
    args = parser.parse_args()
    
    method = args.method
    file_path = args.file
    provided_hash = args.checksum

def display_status(report):
    print(Style.BRIGHT + report.file + Style.RESET_ALL)
    print('Hash Method   :', Style.BRIGHT + report.method + Style.RESET_ALL)
    print('Computed Hash :', report.computed_hash)
    print('Provided Hash :', report.provided_hash)
    if(report.status):
        print('STATUS\t\t\b\b:', Style.BRIGHT + Fore.GREEN + 'SUCCESS' + Style.RESET_ALL)
    else:
        print('STATUS\t\t\b\b:', Style.BRIGHT + Fore.RED + 'FAILED' + Style.RESET_ALL)     

if __name__ == '__main__':
    getOptions()
    option_validation = OptionValidation(method, file_path, provided_hash)
    
    if not option_validation.methodValiadation():
        #return
        pass
    if not option_validation.fileValidation():
        #return
        pass
    if not option_validation.checkSumValidation(provided_hash):
        #return
        pass
    
    integrity_check = IntegrityCheck()
    report = None
    if(method == 'md5'):
        computed_hash = integrity_check.get_md5sum(file_path)
        if(computed_hash == provided_hash):
            report = Report(method, os.path.basename(file_path), computed_hash, provided_hash, True)
        else:
            report = Report(method, os.path.basename(file_path), computed_hash, provided_hash, False)
    elif(method == 'sha256'):
        computed_hash = integrity_check.get_sha256sum(file_path)
        if(computed_hash == provided_hash):
            report = Report(method, os.path.basename(file_path), computed_hash, provided_hash, True)
        else:
            report = Report(method, os.path.basename(file_path), computed_hash, provided_hash, False)
    display_status(report)

