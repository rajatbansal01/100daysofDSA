# Declaring a function which is using for Binary Search.
# array is a list of numbers.
# element is the element which we have to find.
# left is the starting index of list.
# right is the ending index of the list.
def binary_search(array, left, right, element):
    # Base codition.
    if left <= right:
        

        # finding the mid value.
        mid = left + (right - left) // 2

        # Check the mid value with element to find
        if array[mid] == element:
            return mid
        
        # discarding all elements from right space of array.
        # including the middle element
        elif element < array[mid]:
            return binary_search(array, left, mid - 1, element)

        # discarding all elements from left space of array.
        # including the middle element
        else:
            return binary_search(array, mid + 1, right, element)
    else:
        return -1

if __name__ == '__main__':
 
    n = int(input("Enter The Size of the array :- "))
    print("Enter the elements of the list")
    array = []
    for i in range(n):
        ele = int(input())
        array.append(ele)
    array.sort()
    print(array)
    element  = int(input("Enter the element you want to search in the array :- "))
 
    (left, right) = (0, len(array) - 1)
    index = binary_search(array, left, right, element)
 
    if index == -1:
        print('Element not found in the list')
        
    else:
        print('Element found at index', index)
       
