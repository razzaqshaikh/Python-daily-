#Write a Python program to check if a given variable is of type list 




check_type=[12,234,4567,2345,'sameer',234,'akash']

if type(check_type)== tuple:
	print('its a tuple type')

elif type(check_type) == list:
	print('its a list type')

else:
	print('Other veriable')