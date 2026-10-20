#1.Python program to reverse a string

text="Python"
reversed_text=text[::-1]
print("reveresed text is : ", reversed_text)


#2.Python program to check whether the given string id Palindrome or not

word=input("Enter a word to check Palindrome :")
reversed_word=word[::-1]

if word == reversed_word :
    print("Palindrome")
else:
    print("Not palindrome")


#3.Count the number of Vowels ina string


text="Hellow World"
count=0
for i in text.lower():
    if i in "aeiou":
        count+=1;
print("Vowels:",count)


#4.Remove duplicate characters from the string

text="programming"
result=""
for char in text:
    if char not in result:
        result+=char
print(result)


#5.Python program to find frequency of characters

text="banana"
frequency ={}
for char in text:
    #if character Already exist
    if char in frequency:
        frequency[char]+=1
    #First occurence
    else:
        frequency[char]=1
print(frequency)

#6.Check whether two strings are anagram

word1="listen"
word2="earth"
#sorts both strings
if sorted(word1)==sorted(word2):
    print("Anagram")
else:
    print("Not Anagram")


#7.Program to find the first non - repeated characters that occurs only once.

text="swiss"
#count frequency
frequency= {}

for char in text:
    frequency[char]=frequency.get(char,0)+1
#Find first character with count 1

for char in text:
    if frequency[char]==1:
        print("First Non - repeated character:",char)
        break
