'''Q1.Write a python prog to check if given variable is type
int or float'''
var = 10.5  # Change this value to test
if isinstance(var, int):
    print("Integer")
elif isinstance(var, float):
    print("Float")
else:
    print("Neither int nor float")


#Q2.create a python prog list containing the names of 5 city
#then append the names of new city. 
city=['solapur','pune','hydrabad','mumbai','nagpur']
city.append('jaipur')
print(city)


#Q3.write a python prog to convert a given string to uppercase
Str="Razzaque shaikh"
print(Str.lower())
print(Str.upper())



#Create a Python dictionary containing the names and ages of
#3 people. Then, update the age of one person.
d={"a":12,'b':23,'c':34}
print(d)
d.update({'a':76})
print(d)



#Q4.Write a Python program to check if a given string contains a specific substring.
a='shaikh razzaq'
b='shaikh'
if b in a:
    print('founded')
else:
    print('sub string not  founded')



#Q6.Create a Python tuple containing the names of 3 fruits.
#Then, try to modify the tuple.
fruits=('mnago','banana','apple')
t=list(fruits)
t[0]='cheery'
fruits=tuple(t)
print(fruits)



#Q7 Write a Python program to convert a given list to a set.
city=['solapur','pune','mumbai']
new_cityadd=set(city)
print(type(new_cityadd))


#Q8. Create a Python set containing the names of 3 animals.
#Then, add a new animal to the set.'''
animal={'tiger','cat','dog'}
animal.add('fish')
print(animal)



#Q9.Write a Python program to check if a given variable is of type list 
check_type=[12,234,4567,2345,'sameer',234,'akash']
if type(check_type)== tuple:
    print('its a tuple type')
elif type(check_type) == list:
    print('its a list type')
else:
    print('Other veriable')



#Q10. Create a Python dictionary containing the names and ages of 3 people. 
#Then, delete one person's record.'''
name_ages={'sameer':34, 'rahul':35, 'onkar':26, 'rakesh':29}
name_ages.pop('sameer')
print(name_ages)
print(name_ages.items())



#Q11: Write a function to reverse a given string.
string_name = 'shaikh'
st=string_name[::-1]
print(st)nnnn   


#Q12: Write a function to count the number of vowels in a string.
Name = "Shaikh RazzAque"
vowels = "aeiouAEIOU"
count = {i: Name.count(i) for i in vowels if i in Name}
print(count)





#Q13: Write a function to check if a string is a palindrome (same forward and backward

#please slove this



#Q14: Write a function to count the number of words in a string.
def count_words(s):
    return len(s.split())
    
text = "Hello how are you doing today?"
print("Word count:", count_words(text))



#Q15: Write a function to convert a given string into title case (capitalize the first letter of each word).
def captalize_word(s):
 return (s.title())
text = "razzaque shaikh i am good person"
print("Title case: " , captalize_word(text))


#Q16: Write a function to remove duplicate characters from a string.


#Slove this mam


#Q17: Write a function to reverse each word in a given string.


#solve this mam


#Q18: Write a function to extract only the digits from a given string.

#solve this mam

