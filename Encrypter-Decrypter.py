#Encrypt and Decrypt
s= input('Enter message to encrpyt or decrypt: ')
lst = []
for i in range(len(s)):
  lst.append((ord('~') +ord(' ') - ord(s[i])))
en = ''
for i in range(len(lst)):
 en += chr(lst[i])
print(en)
input('Press Enter to exit:')