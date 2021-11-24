#include <stdio.h>
#include <stdlib.h>

int solve(int heads, int legs)
{
    int x = 0, y = 0;
    y = (legs - (2 * heads)) / 2;
    x = (legs - (4 * y)) / 2;
    if (x < 0 || y < 0)
    {
        printf("\nWrong numbers entered, cannot calculate.");
    }
    else
    {
        printf("\nChickens = %d, Cows = %d", x, y);
    }
}

int main(void)
{
    int h, l;
    printf("Enter number of heads: ");
    scanf("%d", &h);
    printf("\nEnter number of legs: ");
    scanf("%d", &l);

    solve(h, l);
}