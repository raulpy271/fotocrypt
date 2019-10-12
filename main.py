# -*- coding: utf-8 -*-
# How it works -> https://repl.it/talk/share/FOTOCRYPT-Encrypting-pixels-in-a-photo/17845

import cv2
l = []
key=[]
for i in range(0, 256):
    l.append(i)


dir=str(input('Enter the path of the photo to encrypt (filetype:png)\n > '))
dir_save=str(input('Enter path to save new photo\n > '))
dir_key=str(input('enter the path where you want to save or load the key\n > '))
dcrpt = int(input('\n    0) encrypt \n    1) decrypt\n  > '))
imagem = cv2.imread(dir)


def key_new(key):
    from random import choice  #creating and saving new key
    for i in range(0, 256):
        number = choice(l)
        l.pop(l.index(number))
        key.append(number)
    key_write=open(dir_key, 'w')
    keyout= ' '
    for i in key:
        keyout = str(keyout) + str(i) + ' '
    key_write.writelines(keyout)
    key_write.close()


def key_read(): #read key
    key_write = open(dir_key, 'r')
    keyout = key_write.readlines()
    keyout = keyout[0]
    keyout = keyout.split()
    for i in range(0, len(keyout)):
        keyout[i]=int(keyout[i])  
    key_write.close()
    for i in range(0, 256):
        l[i] = keyout.index(i)
    return l # 'key' will receive 'l'
    


if dcrpt == 1:
    dcrpt = True
    key = key_read()
    print('\ndecrypting ... ')
else:
    dcrpt = False
    key_new(key)
    print('\nencrypting ... ')


def cript(pixel): #encrypting | decrypting   pixels
    new_pixel=[0, 0, 0]
    for i in range(0, 3):
        new_pixel[i] = key[pixel[i]]
    return new_pixel


for x in range (0, (imagem.shape[0] ) ): #traversing all pixels
    for y in range (0, (imagem.shape[1] ) ):
        imagem[x, y] = cript(  imagem[x, y]  )


cv2.imwrite(dir_save, imagem)
print('finished! \nImage saved in {}'.format(dir_save))
#cv2.imshow("Imagem", imagem)
#cv2.waitKey(0)

