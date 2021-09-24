
import os
import time
#os.system("cp shells/mainshell.py shells/shell.py")
import pathlib
import argparse
parser = argparse.ArgumentParser()



text = input(" > ")
words = text.split()
print(words)

data = input('Enter a word to delete: ')
status = False

for word in words:
    if word == data:
        words.remove(word)
        status = True

if status:
    text = ' '.join(words)
    s = text.replace(" ", "+")
    print('String after deletion:',s)
else:
    print('Word not present in string.')
