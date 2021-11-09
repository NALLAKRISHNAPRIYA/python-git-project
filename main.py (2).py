def palindrome(str1):
  if str1[::-1]==str1:
     return True
  return False
str1=input()
if palindrome(str1)==True:
  print( "It is  a palindrome")
else:
  print( "It is not palindrome")