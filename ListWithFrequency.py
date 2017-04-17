#Question 1

class ListWithFrequency:
	listItems = dict()

	def store(*listOfItems):
		for(x in listOfItems):
			if(x in listItems.keys()):
				listItems[x]+=1
			else:
				listItems[x]=1

	def returnUnique():		
		return listItems.keys()

	def returnItemsFrequency():
		return listItems

	def appendNewItem(x):
		if(x in listItems.keys()):
				listItems[x]+=1
			else:
				listItems[x]=1