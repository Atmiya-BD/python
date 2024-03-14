# 7 Ask user to fill array with string. Give two facilities: 
# i). Allow user to search for an element from the string, 
# ii). Also give the position at which the search element was found.

# prompt user to enter array of strings
arr = input("Enter array of strings separated by spaces: ").split()

# prompt user to enter search element
search = input("Enter search element: ")

# search for element in array and return position
if search in arr:
    position = arr.index(search)
    print("Element found at position:", position)
else:
    print("Element not found in array.")





