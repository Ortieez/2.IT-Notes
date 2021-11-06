#include <stdio.h>
#include <stdlib.h>

#define array_size 10

int main()
{
    int arrayToSort[array_size] = {10, 5, 6, 8, 9, 15, 3, 7, 32, 42};

    for (int i = 0; i < array_size - 1; i++)
    {
        for (int j = 0; j < array_size - i - 1; j++)
        {
            if (arrayToSort[j] < arrayToSort[j + 1])
            {
                int temp = arrayToSort[j];
                arrayToSort[j] = arrayToSort[j + 1];
                arrayToSort[j + 1] = temp;
            }
        }
    }

    for(int i = 0; i < array_size; i++) {
        printf("%d ", arrayToSort[i]);
    }
}