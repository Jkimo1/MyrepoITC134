
#making an array for the sorting of the selection

array = [13,4,9,5,3,16,12]

def selectionSort(array):

    n = len(array)

    for i in range(n):#<---- however many items are in the loop is how many times the sort loops

        minimum = i 

        for j in range(i+1, n):

            if (array[j] < array[minimun]):

                minimum = j

        #this is the swapping portion that swaps the values n the array
        temp = arraay[i]
        array[i] = array[minimum]
        array[minimun] = temp
    
    return array

print(selectionSort(array))
