#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Author : ortieez / Adam Lipert
// Minefield game

int minefield(int x, int y, int mines)
{
    // Initialize the minefield
    int grid[x][y];
    int i, j;
    for (i = 0; i < x; i++)
    {
        for (j = 0; j < y; j++)
        {
            grid[i][j] = 0;
        }
    }
    // Generate and place the mines
    srand(time(NULL));
    int mine_x, mine_y;
    for (i = 0; i < mines; i++)
    {
        mine_x = rand() % x;
        mine_y = rand() % y;
        grid[mine_x][mine_y] = 1;
    }

    // Print the minefield
    for (i = 0; i < x; i++)
    {
        for (j = 0; j < y; j++)
        {
            printf(" 0 ");
        }
        printf("\n");
    }
    return grid;
}

int main()
{
    // Take the grid from function
    int *grid = minefield(10, 10, 10);

    // Loop until the user dies
    int dead = 0;
    while (dead != 1)
    {
        int x, y;
        printf("Enter x and y coordinates: ");
        scanf("%d %d", &x, &y);
        if (*(grid + x * 10 + y) == 1)
        {
            printf("You died!\n");
            dead = 1;
        }
        else
        {
            printf("You survived!\n");
        }
    }
}