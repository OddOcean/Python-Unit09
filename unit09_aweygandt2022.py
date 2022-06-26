############################################################
#     Aidan Weygandt                        06.11.21       #
#     Unit 9 Problems                                      #
#     String in a String, Longest common prefix,           #
#     password checker, phone keypad convertor             #
#     reverse a word, string encrypt/decrypt               #
############################################################


########################## PROB 1 ##########################

def prob1():
  def findStr(lookFor, lookIn): #compares short string with same length of long string. The moves over one on long string and continues
    return lookIn.count(lookFor)

  print("Problem #1 - Occurances Of A String In A String\n")
  inpStr = (input("Enter a long string: "))
  inpSer = (input("Enter a short string: "))
  print("Your string", ("\"" + inpSer + "\""), "was in", ("\"" + inpStr + "\""), findStr(inpSer, inpStr), "times")

#prob1()


########################## PROB 2 ##########################

def prob2():
  def prefix(word1, word2): #finds longest prefix between two words
    prefix = ""
    for each in range(min(len(word1), len(word2))): #searches for shortest word length so it doesnt go out of range
      if word1[each] == word2[each]: #for every letter that matches save it
        prefix += word1[each]
      else: break
    return prefix #returns all matching letters

  print("Proble #2 - Longest Common Prefix\n")
  word1 = input("Enter word 1: ")
  word2 = input("Enter word 2: ")
  print("The longest common prefix is", prefix(list(word1), list(word2)))

#prob2()


########################## PROB 3 ##########################

def prob3():
  alpha = ["0" ,"1" ,"2" ,"3" ,"4" ,"5" ,"6" ,"7" ,"8" ,"9"]

  for num in range(97, 123): #adds alphabet to the list of numbers
    alpha.append(chr(num))

  print("Problem #3 - Check Password\n")
  print("Password must have:\n","eight characters\n", "only letters\n", "at least 3 digits\n")

  while 1:
    password = list(input("Enter a password: "))

    if len(password) >= 8: #requires user to have a password that is 8 characters long
      count = 0
      for each in password: #checks if there are more than 3 numbers
        if each.isdigit(): count += 1
      if all(x in alpha for x in password) and count >= 3: break #if theres only letters and number too then break loop
    
    print("Your password does not meet requirments")
  print("Your password is valid")

#prob3()


########################## PROB 4 ##########################

def prob4():
  def getNumber(let):
    alpha = []
    num = [2 ,2 ,2 ,3 ,3 ,3 ,4 ,4 ,4 ,5 ,5 ,5 ,6 ,6 ,6 ,7 ,7 ,7 ,7 ,8 ,8 ,8 ,9 ,9 ,9 ,9]
    nums = ""

    for a in range(97, 123): #makes list of letters so i dont have to
      alpha.append(chr(a))

    for each in let: #finds equivalent index of letter in num and concatenates it with new string
      if each.isalpha(): #only changes letters
        nums = nums + str(num[alpha.index(each)])
      else: #incase number is put in
        nums = nums + str(each)
    
    return str(nums)
  
  def phoneConvert(phoneNum):
    noHyph = ""

    for each in phoneNum: #removes all hyphens from phone number
      if each != "-":
        noHyph += str(each)

    if len(noHyph) == 7: return getNumber(noHyph)[:3] + "-" + getNumber(noHyph)[3:] #uses length to find were the hyphens should go
    elif len(noHyph) == 10: return getNumber(noHyph)[:3] + "-" + getNumber(noHyph)[3:6] + "-" + getNumber(noHyph)[6:]
    elif len(noHyph) == 11: return getNumber(noHyph)[:1] + "-" + getNumber(noHyph)[1:4] + "-" + getNumber(noHyph)[4:7] + "-" + getNumber(noHyph)[7:]
    else: return "Phone number was invalid"

  print("Problem #4 - Phone Keypad Converter\n")
  phoneNum = input("Enter a phone number with letters: ")
  print(phoneConvert(phoneNum))

prob4()


########################## PROB 5 ##########################

def prob5():
  def reverse(string): #outputs string but backwards
    return string[::-1]

  print("Problem #5 - Reverse A Word\n")
  userInp = input("Enter string to be reversed: ").lower()
  print("Your string reversed is:", reverse(userInp).capitalize())

#prob5()


########################## PROB 6 ##########################

def prob6():
  from encryptor import encryptor
  dab = encryptor()
  print("Problem #6 - Encryptor\n")
  userInp = input("Input something to encrypt: ")
  print()
  print("Your message encrypted is:", dab.encrypt(userInp))
  print("Your message decrypted is:", dab.decrypt(dab.encrypt(userInp)))

#prob6()