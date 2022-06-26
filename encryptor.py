import random

class encryptor:
  def __init__(self):
    self.__codes = []
    for x in range(20, 127): #creates list of random ascii codes
      rand = random.randint(20, 126)
      while rand in self.__codes:
        rand = random.randint(20, 126)
      self.__codes.append(rand)

  def reverse(self, string): #outputs string but backwards
    return string[::-1]

  def encrypt(self, encrypt):
    encrypted = ""
    for x in self.reverse(encrypt):
      encrypted += chr(self.__codes[ord(x) - 20]) #gets rand code at x's ascii and adds character of rand code to string
    return encrypted

  def decrypt(self, decrypt):
    decrypted = ""
    for x in decrypt:
      decrypted += chr(self.__codes.index(ord(x)) + 20) #gets index of random code and adds character of index to string
    return self.reverse(decrypted)