# Questions 2-5

def convert(val = ''):
	if "." in val:
		try:
    		x = float(val)
		except ValueError:
			x = val
	else:
		try:
			x = int(val)
		except ValueError:
			x = val
	return x

def elegant():
	abc = ['dog', 'Fido', 10]
	keys = ['animal', 'name', 'age']
	dictionary = dict(zip(keys, abc))
	print('{name} the {animal} is {age} years old'.format(name = dictionary['name'], animal = dictionary['animal'], age = dictionary['age']))'

def min3(first, second, third):
	listItems = [first, second, third]
	listItems.sort()
	return listItems[0]

def apply_operation(left_operand, right_operand, operator): 
	return eval(str(left_operand) + str(operator) + str(right_operand))

