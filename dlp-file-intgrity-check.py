#/bin/python
from argparse import ArgumentParser
import os.path
import hashlib
from colorama import init
from colorama import Fore, Back, Style
from enum import Enum

__author__ = 'dileepa'
__appname__ = 'dlp file integrity check'
__appversion__ = '1.0.1'

parser = ArgumentParser()

parser.add_argument('-a', '--algorithm', help='algorithm to generate hash [md5, sha1, sha224, sha256, sha384, sha512]')
parser.add_argument('-f', '--file', help='select file for integrity check')
parser.add_argument('-c', '--checksum', help='checksum in text for varification')
parser.add_argument('-V', '--version', action='version', version=__appversion__)

algorithm = ''
file_path = ''
provided_hash = ''

class Algorithm(Enum):
    md5 = 1
    sha1 = 2
    sha224 = 3
    sha256 = 4
    sha384 = 5
    sha512 = 6
    sha3_224 = 7
    sha3_256 = 8
    sha3_384 = 9
    sha3_512 = 10
    shake_128 = 11
    shake_256 = 12

class Report():
    def __init__(self, algorithm, file, computed_hash, provided_hash, status):
        self.algorithm = algorithm
        self.file = file
        self.computed_hash = computed_hash
        self.provided_hash = provided_hash
        self.status = status

class OptionValidation():
    def __init__(self, algorithm, file, provided_hash):
        self.algorithm = algorithm
        self.file = file
        self.provided_hash = provided_hash
    
    def algorithmValidation(self):
        print(self.algorithm, type(self.algorithm), Algorithm.md5.name, type(Algorithm.md5.name))
        print(self.algorithm == Algorithm.md5.name)
        if(self.algorithm == Algorithm.md5.name):
            return True
        elif(self.algorithm == Algorithm.sha1.name):
            return True
        elif(self.algorithm == Algorithm.sha224.name):
            return True
        elif(self.algorithm == Algorithm.sha256.name):
            return True
        elif(self.algorithm == Algorithm.sha384.name):
            return True
        elif(self.algorithm == Algorithm.sha512.name):
            return True
        elif(self.algorithm == Algorithm.sha3_224.name):
            return True
        elif(self.algorithm == Algorithm.sha3_256.name):
            return True
        elif(self.algorithm == Algorithm.sha3_384.name):
            return True
        elif(self.algorithm == Algorithm.sha3_512.name):
            return True
        elif(self.algorithm == Algorithm.shake_128.name):
            return True
        elif(self.algorithm == Algorithm.shake_256.name):
            return True
        else:
            return False
    
    def fileValidation(self):
        if(os.path.exists(self.file)):
            return True
        else:
            return False
    
    def checkSumValidation(self, provided_hash):
        return True

class IntegrityCheck():
    def __init__(self, file):
        self.file = file
    
    def get_md5sum(self):
        checksum = hashlib.md5(open(self.file, 'rb').read()).hexdigest()
        return checksum
    
    def get_sha1sum(self):
        checksum = hashlib.sha1(open(self.file, 'rb').read()).hexdigest()
        return checksum    
    
    def get_sha224sum(self):
        checksum = hashlib.sha224(open(self.file, 'rb').read()).hexdigest()
        return checksum    
    
    def get_sha256sum(self):
        checksum = hashlib.sha256(open(self.file, 'rb').read()).hexdigest()
        return checksum
    
    def get_sha384sum(self):
        checksum = hashlib.sha384(open(self.file, 'rb').read()).hexdigest()
        return checksum
    
    def get_sha512sum(self):
        checksum = hashlib.sha512(open(self.file, 'rb').read()).hexdigest()
        return checksum
    
    def get_shake128sum(self):
        checksum = hashlib.shake_128(open(self.file, 'rb').read()).hexdigest()
        return checksum
    
    def get_shake256sum(self):
        checksum = hashlib.shake_256(open(self.file, 'rb').read()).hexdigest()
        return checksum

def getOptions():
    global algorithm, file_path, provided_hash
    
    args = parser.parse_args()
    
    algorithm = args.algorithm.lower()
    file_path = args.file
    provided_hash = args.checksum
    print(algorithm, type(algorithm))

def display_status(report):
    print(Style.BRIGHT + report.file + Style.RESET_ALL)
    print('Algorithm     :', Style.BRIGHT + report.algorithm + Style.RESET_ALL)
    print('Computed Hash :', report.computed_hash)
    print('Provided Hash :', report.provided_hash)
    if(report.status):
        print('STATUS\t\t\b\b:', Style.BRIGHT + Fore.GREEN + 'SUCCESS' + Style.RESET_ALL)
    else:
        print('STATUS\t\t\b\b:', Style.BRIGHT + Fore.RED + 'FAILED' + Style.RESET_ALL)     

if __name__ == '__main__':
    getOptions()
    option_validation = OptionValidation(algorithm, file_path, provided_hash)
    
    if not option_validation.algorithmValidation():
        print (Fore.YELLOW + "WARNING", Style.RESET_ALL + ': Invalid algorithm')
        exit(0)
    if not option_validation.fileValidation():
        print (Fore.YELLOW + "WARNING", Style.RESET_ALL + ': File not found')
        exit(0)
    if not option_validation.checkSumValidation(provided_hash):
        print (Fore.YELLOW + "WARNING", Style.RESET_ALL + ': Invalid hash')
        exit(0)
    
    integrity_check = IntegrityCheck(file_path)
    report = None
    
    if(algorithm == Algorithm.md5.name):
        computed_hash = integrity_check.get_md5sum()
        if(computed_hash == provided_hash):
            report = Report(algorithm, os.path.basename(), computed_hash, provided_hash, True)
        else:
            report = Report(algorithm, os.path.basename(), computed_hash, provided_hash, False)
    elif(algorithm == Algorithm.sha1.name):
        computed_hash = integrity_check.get_sha1sum()
        if(computed_hash == provided_hash):
            report = Report(algorithm, os.path.basename(), computed_hash, provided_hash, True)
        else:
            report = Report(algorithm, os.path.basename(), computed_hash, provided_hash, False)
    elif(algorithm == Algorithm.sha224.name):
        computed_hash = integrity_check.get_sha224sum()
        if(computed_hash == provided_hash):
            report = Report(algorithm, os.path.basename(), computed_hash, provided_hash, True)
        else:
            report = Report(algorithm, os.path.basename(), computed_hash, provided_hash, False)
    elif(algorithm == Algorithm.sha256.name):
        computed_hash = integrity_check.get_sha256sum()
        if(computed_hash == provided_hash):
            report = Report(algorithm, os.path.basename(), computed_hash, provided_hash, True)
        else:
            report = Report(algorithm, os.path.basename(), computed_hash, provided_hash, False)
    elif(algorithm == Algorithm.sha384.name):
        computed_hash = integrity_check.get_sha384sum()
        if(computed_hash == provided_hash):
            report = Report(algorithm, os.path.basename(), computed_hash, provided_hash, True)
        else:
            report = Report(algorithm, os.path.basename(), computed_hash, provided_hash, False)
    elif(algorithm == Algorithm.sha512.name):
        computed_hash = integrity_check.get_sha512sum()
        if(computed_hash == provided_hash):
            report = Report(algorithm, os.path.basename(), computed_hash, provided_hash, True)
        else:
            report = Report(algorithm, os.path.basename(), computed_hash, provided_hash, False)
    display_status(report)