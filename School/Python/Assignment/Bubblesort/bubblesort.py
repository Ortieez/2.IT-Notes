import random
def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

array = [random.randint(0,100) for i in range(10)]
print(bubblesort(array))