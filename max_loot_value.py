items = [ 
{ "weight": 5, "value": 10 }, 
{ "weight": 4, "value": 40 }, 
{ "weight": 6, "value": 30 }, 
{ "weight": 4, "value": 50 }
]

napsackLimit = 10

def getMaximumValue(items, napsackLimit):
	## Sort the list by weight. This is very important as it reduces on the number of checks to perform!
	# A sorted list is always computationally optimized than unsorted list
	items = sorted(items, key = lambda i: i['weight'])

	# keep track of the maximum value, total minimum weight and the individual selected entries as we traverse the list
	maxValue = 0
	runningWeight = 0
	selectedEntries = []

	## keep track of the least valued entry to minimize iterations
	leastValuedSelected, leastItemWeight, leastItemValue = expandItem(items[0])
	leastValuedSelectedIndex = 0  # the index will help in deleting the entry from our {$selectedEntries} list

	for item in items:
		itemWeight, itemValue = item["weight"], item["value"]
		if((itemWeight + runningWeight) <= napsackLimit):
			selectedEntries.append(item)
			runningWeight += itemWeight
			maxValue += itemValue

			# If the new entry has lower value then set it as the current least valued entry 
			# We use the ratio of value/weight to determine the most valued entry
			if(itemValue/itemWeight < leastItemValue/leastItemWeight):
				leastValuedSelected, leastItemWeight, leastItemValue = expandItem(item)
				leastValuedSelectedIndex = len(selectedEntries) - 1
		else:
			# if the weight of the current entry plus the total minimum weight is more than {napsackLimit}, 
			# then eliminate the least valued from the list if it fits the requirement
			isOfHigherValue = itemValue/itemWeight >= leastItemValue/leastItemWeight
			weightFitsIfLeastValuedRemoved = (runningWeight+itemWeight - leastItemWeight) <=napsackLimit
			
			if(isOfHigherValue and weightFitsIfLeastValuedRemoved):
				# remove the least valued from the {selectedEntries} list and decrement {maxValue} and total minimum weight
				del selectedEntries[leastValuedSelectedIndex]
				maxValue -= leastItemValue
				runningWeight -= leastItemWeight

				# Add the new entry to the {selectedEntries} list and update {runningWeight} and {maxValue} 
				selectedEntries.append(item)
				runningWeight += itemWeight
				maxValue += itemValue

				# Here is where things get a little tricky. Since we have eliminated our least 
				# valued entry, we need to find a new one! How? The only option if to go back to the 
				# list of our selected entries and look for that least valued entry.
				# This is of complexity O(n). Need a better way!
				
				# We first select an entry from our {selectedEntries} and assume that to be our least valued entry
				leastValuedSelected, leastItemWeight, leastItemValue = expandItem(selectedEntries[0])

				# We then iterate through the list looking for any other entry that might be of lesser value than our assumed entry!
				for index, entry in enumerate(selectedEntries):
					if(entry["value"]/entry["weight"] < leastItemValue/leastItemWeight):
						leastValuedSelected, leastItemWeight, leastItemValue = expandItem(entry)
						leastValuedSelectedIndex = index
			elif(itemWeight <= napsackLimit and itemValue > maxValue):
				# If the current entry has a value that is more than all the {selectedEntries} entries combined and 
				# that its weight is within the requirements, then replaced everything with this new entry
				selectedEntries = [item]
				leastValuedSelected, leastItemWeight, leastItemValue = expandItem(item)
				leastValuedSelectedIndex = 0
				maxValue = itemValue
				runningWeight = itemWeight

	print("selected entries: ", selectedEntries)
	return maxValue

def expandItem(item):
	return (item, item["weight"], item["value"])

if __name__ == '__main__':
	print(getMaximumValue(items, napsackLimit))
