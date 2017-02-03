# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import sys

fname = sys.argv[1]

with open(fname) as f:
    content = f.readlines()
    
offset = 5
def caesar_encrypt(word):
    cword = list(word)
    for i in range(len(word)):
        intvalue = ord(word[i])
        if intvalue in range(65,91):
            intvalue += offset
            if intvalue > 90:
                intvalue -= 26
        if intvalue in range(97,123):
            intvalue += offset
            if intvalue > 122:
                intvalue -= 26       
        cword[i] = chr(intvalue)
    return ''.join(cword)

def caesar_decrypt(word):
    cword = list(word)
    for i in range(len(word)):
        intvalue = ord(word[i])
        if intvalue in range(65,91):
            intvalue -= offset
            if intvalue < 65:
                intvalue += 26
        if intvalue in range(97,123):
            intvalue -= offset
            if intvalue < 97:
                intvalue += 26       
        cword[i] = chr(intvalue)
    return ''.join(cword)


word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
word += " " + word.lower()
#word = "Hello"
e = caesar_encrypt(word)
d = caesar_decrypt(e)

print e
print d