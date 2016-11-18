import os
import sys
import re
from time import sleep
from Crypto.Cipher import AES
class Encrypter:
    '''created by Xiao on 16/11/2016'''
    def __init__(self):
        self.__CHOOSE_MODE_MESSAGE = "Please choose mode:"
        self.__SHOW_HELP = True
        self.__HELP_INFO = '''1 for encryption;
        \r2 for decryption;
        \r0 to exit.'''
        self.__CHOOSE_FILE_MESSAGE = "Please enter file name (with file extension):\n"
        self.__FILE_NOT_EXIST = "File {} does not exist"
        self.__ENTER_PASSWORD = "Please enter password:\n"
        self.__ENCODE_FINISH = "File {} has been encrypted!"
        self.__REMEMBER_PASSWORD = "Please remember your password: '{}'"
        self.__DECODE_FINISH = "File {} has been decrypted!"
        self.__WRONG_PASSWORD = "Invalid password or file {} is not decrypted or damaged. File decryption failed"
        self.__DECRYPTION_FAILED = "File {} is not decrypted or damaged. File decryption stopped"

    def main(self):
        mode = '1'
        while(mode != '0'):
            print(self.__CHOOSE_MODE_MESSAGE)
            if self.__SHOW_HELP:
                print(self.__HELP_INFO)
                self.__SHOW_HELP = False
            mode = raw_input()
            if(mode == '1'):
                self.encrypt()
            elif(mode == '2'):
                self.decrypt()
            else:
                continue
            sleep(0.5)
        sys.exit(0)

    def encrypt(self):
        filename = raw_input(self.__CHOOSE_FILE_MESSAGE)
        if os.path.isfile(filename):
            password = raw_input(self.__ENTER_PASSWORD)
            key = self.generateKey(password)
            file = open(filename, "r+")
            content = file.read()
            contentWithMark = self.addWatermark(content, password)
            contentPadded = self.pad16(contentWithMark)
            cipher = AES.new(key, AES.MODE_ECB)
            encoded = cipher.encrypt(contentPadded)
            file.seek(0)
            file.write(encoded)
            file.truncate()
            file.close()
            print(self.__ENCODE_FINISH.format(filename))
            print(self.__REMEMBER_PASSWORD.format(password))
        else:
            print(self.__FILE_NOT_EXIST.format(filename))

    def decrypt(self):
        filename = raw_input(self.__CHOOSE_FILE_MESSAGE)
        if not os.path.isfile(filename):
            print(self.__FILE_NOT_EXIST.format(filename))
            return

        file = open(filename, "r+")
        encoded = file.read()
        if len(encoded) % 16 != 0:
            print(self.__DECRYPTION_FAILED.format(filename))
            return

        password = raw_input(self.__ENTER_PASSWORD)
        key = self.generateKey(password)
        cipher = AES.new(key, AES.MODE_ECB)
        contentWithMark = cipher.decrypt(encoded)
        if self.checkPasswordMatch(contentWithMark, password):
            content = self.removeWatermark(contentWithMark)
            file.seek(0)
            file.write(content)
            file.truncate()
            print(self.__DECODE_FINISH.format(filename))
        else:
            print(self.__WRONG_PASSWORD.format(filename))
        file.close()

    def generateKey(self, password):
        '''only takes in first 32 bytes of password'''
        return password.ljust(32)[:32]

    def pad16(self, string):
        '''padding empty space for content to encode (length of content should be multiple of 16)'''
        newLen = len(string) + (16 - len(string) % 16) % 16
        return string.ljust(newLen)

    def addWatermark(self, originalContent, password):
        waterMark = "#" + password + "\n" + "#" + str(len(originalContent)) + "\n"
        return waterMark + originalContent

    def checkPasswordMatch(self, stringWithMark, password):
        #non greedy match for first line
        #although greedy match also works because . won't match newline unless in DOTALL mode
        pattern = re.compile(r"#(.*?)\n")
        match = pattern.match(stringWithMark)
        return match is not None and match.group(1) == password

    def removeWatermark(self, stringWithMark):
        pattern = re.compile(r"#.*?\n#(\d*?)\n")
        match = pattern.match(stringWithMark)
        if match is not None:
            waterMark = match.group()
            originalLength = int(match.group(1))
            return stringWithMark[len(waterMark):len(waterMark) + originalLength]
        else:
            return stringWithMark

#start file encrypter
print("starting file encrypter...")
runner = Encrypter()
runner.main()





