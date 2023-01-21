import math

myList = [10,15,9,4,7,16,200,220,9,5,231,456,78,34,23,6,4,87,88]
userC = int(input("Please enter a number that you would like to check for: "))
def binarySearch(lists,choice):
    if choice in lists:
        notFound = True
        lists.sort()
        print("This is the sorted list: " +str(lists))
        start = 0
        end = len(lists)-1
        while notFound:
            middle = (start + end)/2
            middle = math.floor(middle)
            if choice < lists[middle]:
                end = lists.index(lists[middle])-1
                #print(lists.index(lists[middle]))
                print(end)
            elif choice > lists[middle]:
                start = lists.index(lists[middle])+1
                    #print(lists.index(lists[middle]))
                print(start)
            else:
                print("Your number was found at the "+str(lists.index(lists[middle])+1)+ " index")
                notFound = False
        #print(wrong)
    else:
        print("The chosen number " +str(choice)+ " does not exist in the list.")

binarySearch(myList,userC)
