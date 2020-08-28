
## Algorithm that encrypts and/or decrypts the pixels of an images

![encrypted](https://storage.googleapis.com/replit/images/1565024778487_ea4eb68fa01a55580e756e58a4b9216a.png)

![key](https://storage.googleapis.com/replit/images/1565023198329_93bdd1eafc0a613ab590210ca9563c64.png)

###   How it works
First, a list of 256 random numbers is created. It is saved and later used to decrypt the PNG.
  Encryption is simple: an 'x' number is replaced by the number with index 'x' in the previously created list. 

 #### Example: 
we have the following random key:

```py
key = [1, 3, 70, 10, 25, 101]
# key contains 256 elements.
# I did not put all to make understanding easier
  ```

And the following pixel:

```py
pixel = (5, 0, 2)
```

Encrypting the pixel:

```py
for i in range(0, 3):
    pixel[i] = key[ pixel[i] ]
print (pixel) # >>> (101, 1, 70)
```

This process is done on all pixels. Decryption occurs by doing the reverse process. 


