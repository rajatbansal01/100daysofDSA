# Python Program to implement
# Odd-Even / Brick Sort
 
def oddEvenSort(array, n):
    # Initially array is unsorted
    isSorted = 0
    while isSorted == 0:
        isSorted = 1
        temp = 0
        for i in range(1, n-1, 2):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                isSorted = 0
                 
        for i in range(0, n-1, 2):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                isSorted = 0
     
    return


if __name__ == "__main__":
    n = int(input("Enter the size of the array :- "))
    array = []
    for i in range(n):
        element = int(input("Enter the element :- "))
        array.append(element)
    
    oddEvenSort(array, n)
    for i in range(0, n):
        print(array[i], end = ' ')
