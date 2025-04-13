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


#Please check this mam


#Q17: Write a function to reverse each word in a given string.


#Please check this mam


#Q18: Write a function to extract only the digits from a given string.

#Please check this mam



print('-------------------------------------------------------------------------')


x = 5; y = 2; print(x + y) #What's the output?  Ans = o/p=7
a = 10; b = 3; print(a % b) #What's the output?  Ans =  o/p=1
x = 5; y = 2; print(x * y) #What's the output?   Ans =  o/p=10
a = 10; b = 2; print(a / b) #What's the output?  Ans = o/p=5.0
x = 5; y = 2; print(x - y) #What's the output?   Ans = o/p=3
a = 10; b = 3; print(a > b) #What's the output?  Ans = o/p=true
x = 5; y = 5; print(x == y) #What's the output?  Ans = o/p=true
a = 10; b = 2; print(a <= b) #What's the output? Ans = o/p=False
x = 5; y = 0; print(x and y) #What's the output? Ans = o/p=0  
a = 10; b = 0; print(a or b) #What's the output?  Ans = o/p=10


print('-------------------------------------------------------------------------')

#Equality Operators
#1. What is the output of 5 == 5?
print(5==5)  #O/P = true

#2. What is the output of 5 == "5"?5 
print(5 == '5') #o/p = false

#3. What is the output of "hello" == "hello"?
print('hello' == "hello") #true

print('-------------------------------------------------------------------------')

#Identity Operators
#1. What is the output of a = 5; b = 5; a is b?
a=5
b=5    #true
print(a is b)

#2. What is the output of a = [1, 2, 3]; b = [1, 2, 3]; a is b?

a = [1, 2, 3]
b = [1, 2, 3]    #o/p= False
print(a is b)

#3. What is the output of a = "hello"; b = "hello"; a is b?


a = "hello" 
b = "hello"   #True
print(a is b)


print('-------------------------------------------------------------------------')

#1. What is the output of 5 in [1, 2, 3, 4, 5]?

a=[1,2,3,4,5]
b=a.index(5)
print(b)

#2.what is the output of "hello" in ['hi','hello', world]

a=['hi','hello', 'world']
b=a.index('hello')
print(b)


#3. What is the output of `5 not in [1, 2, 3, 4, 5]




print('-------------------------------------------------------------------------')


#1. What is the output of 
print(True and True)   #o/p True

#2. What is the output of
print(True or False)   #o/p True

#3. What is the output of `
print(not True)  #o/p False

#4. What is the output of `
x = 5; y = 3; print(x > 2 and y < 5)  #o/p true

#5. What is the output of `
x = 5; y = 3; print(x > 2 or y < 5)#o/p true

#6. What is the output of 
x = 5; y = 3; print(not x > 2)  #o/p false

#7. What is the output of 
x = 0; y = 3; print(x and y)  #o/p 0

#8. What is the output of `
x = 5; y = 0; print(x or y)   #o/p 5


#9. What is the output of `
x = True; y = False; print(x and not y)  #o/p  true

#10. What is the output of `
x = True; y = False; print(x or not y)  #o/p  true



print('-------------------------------------------------------------------------')


#1.
my_list = [1, 2, 3, 4, 5]
print( my_list[1:3])    #[2, 3]

#2.
my_list = [1, 2, 3, 4, 5] 
print(my_list[-2:])         #[4, 5]

#3.
my_list = [1, 2, 3, 4, 5] 
print(my_list[::2])    #[1, 3, 5]

#4.
my_list = [1, 2, 3, 4, 5]
print( my_list[:3])     #[1, 2, 3]

#5.
my_list = [1, 2, 3, 4, 5] 
print(my_list[::-1])      #[5, 4, 3, 2, 1] 

#6.
my_list = [1, 2, 3, 4, 5]
print(my_list[2:])  #[3, 4, 5] 

#7
my_list = [1, 2, 3, 4, 5]
print( my_list[:2])    #[1, 2]

#8.
my_list = [1, 2, 3, 4, 5]
print(my_list[1::2])    #[2, 4]   

#9.
my_list = [1, 2, 3, 4, 5] 
print(my_list[-1:])     #[5]

#10.
my_list = [1, 2, 3, 4, 5]
print(my_list[:-1])   #[1, 2, 3, 4]




print('------------------------------For Loop que-------------------------------------------')


#1.Write a for loop to iterate over the numbers 1 to 5 and print each number.

my_list = [1,2,3,4,5]

for i in my_list:
    print(i)

#2.Use a for loop to calculate the sum of the numbers in the list [1, 2, 3, 4, 5].

my_list2 = [1,2,3,4,5]

cal = 4

for i in my_list2:
    cal += i

print(cal)


#3.Write a for loop to iterate over the characters in the string "hello" and print each character.

str = "hello"

for i in str :
    print(i)


#4.Use a for loop to find the maximum value in the list [1, 5, 3, 2, 4].

my_list3 = [1,3,5,7,4,32]

max_value = my_list3[0]

for i in my_list3:
    if i> max_value:
        max_value=i
print(max_value)


#5.Write a for loop to iterate over the range 10 to 1 (inclusive) and print each number

for i in range(1 , 10):
    print(i,end=" ")


#6.Use a for loop to iterate over the keys in the dictionary {"a": 1, "b": 2, "c": 3} and print each key.
 #please this quetion explain


#7.Write a for loop to iterate over the values in the dictionary {"a": 1, "b": 2, "c": 3} and print each value.
#please this quetion explain

#8. Use a for loop to iterate over the items in the dictionary {"a": 1, "b": 2, "c": 3} and print each key-value pair.
#9. Write a for loop to iterate over the numbers 1 to 10 and print each number that is even.
#10. Use a for loop to iterate over the numbers 1 to 10 and print each number that is odd.




#function questions
#1. Write a function to find the square of a number.

def square_ofnumber(square):
    return square**2
result = square_ofnumber(10)
print(result)


#Create a function that takes two numbers and returns their sum, difference, product, and quotient
#please this solve this


#Write a function to check if a given string is a palindrome.

def palindrome_check(name):
    if name == name[::-1]:
        print(f"{name} it's a palindrome " )

palindrome_check('madam')


#Define a function that counts the vowels in a string.

def count_vowels(x):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in x:
        if char in vowels:
            count += 1
    return count       
text = "hey this razzaque"
number_of_vowels = count_vowels(text)
print("Number of vowels:", number_of_vowels)


   #Write a function that accepts a list of numbers and returns the largest and smallest numbers.
    # solve this


#Create a function that checks if a number is prime.
#solve this
    





