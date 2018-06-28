# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 13:49:21 2018
@author: Joel Velez
"""
import encode
import decode
        
class stenograPy():
    def __init__(self):
        self.e = encode.Encode()
        self.d = decode.Decode()
    def main(self):
        a = input("Would you like to encode(E) or decode(d) \n press x to exit \n")
        if a == "e" or a == "E":
            string = input("Enter text to hide \n")
            inputFile = input("Enter input file name with extension \n")
            outPutFile = input("Enter output file name with extension \n")
            string = bytes(string, "ascii")
            self.e.encodeMain(string, inputFile, outPutFile)
        elif a == "d" or a == "D":
            inputFile = input("Enter file to decode with extension \n")
            self.d.decodeMain(inputFile)

if __name__ == '__main__':
    s = stenograPy()
    s.main()
            