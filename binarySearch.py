import math

myList = [10,15,9,4,7,16,200,220,9,5,231,456,78,34,23,6,4,87,88] #list could be changed to be random
userC = int(input("Please enter a number that you would like to check for: ")) #user entry
def binarySearch(lists,choice):#function
    if choice in lists: #will make sure the users choice exists
        notFound = True #flag which will keep searching until value is found
        lists.sort() #sort lists
        print("This is the sorted list: " +str(lists))
        start = 0 #start of list
        end = len(lists)-1 #gets end of list
        while notFound: #while value not found will keep searching
            middle = (start + end)/2 #will find the mid point
            middle = math.floor(middle) #if uneven numbers used will go to the lower one
            if choice < lists[middle]: #if choice is less than middle number
                end = lists.index(lists[middle])-1 #will set end value to mid less 1
                print(end)
            elif choice > lists[middle]: #if choise is greater than middle number
                start = lists.index(lists[middle])+1 #sets start to mid + 1, disregarding first half
                print(start)
            else:
                print("Your number " +str(choice)+ " was found at the "+str(lists.index(lists[middle])+1)+ " index") #when found will include where found in lists
                notFound = False
    else: #if chosen number does not exist
        print("The chosen number " +str(choice)+ " does not exist in the list.")

binarySearch(myList,userC)
