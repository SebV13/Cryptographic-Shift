# word = input()
print("Enter a Key all upper case")
key = input()
print("Enter a Word all upper case")
word = input()
#word = 'SENDMONKEYS'
#key = 'ACM'
tempstring = key + word
keyLen = len(key)
wordLen = len(word)
shortWord = tempstring[:-keyLen]

for i in range(wordLen):
  print(shortWord[i],word[i])
list = []
for i in range(wordLen):
  list.append(chr(ord(shortWord[i]) + (ord(word[i])-65)))

print(list)
print(ord(list[5]))
for i in range(wordLen):
  if ord(list[i]) > 90:
    list[i] = chr(ord(list[i])-26)

print(list)
cipherT = ''.join(list)
print(cipherT)
