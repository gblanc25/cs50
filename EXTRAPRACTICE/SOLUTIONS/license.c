#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    // Check for command line args
    if (argc != 2)
    {
        printf("Usage: ./read infile\n");
        return 1;
    }

    // Create buffer to read into
    char buffer[7];

    // Create array to store plate numbers
    char *plates[8];

    FILE *infile = fopen(argv[1], "r");

    int idx = 0;

    while (fread(buffer, 1, 7, infile) == 7)
    {
        // replace '\n' with '\0'
        buffer[6] = '\0';

        // Allocate memory each string
        plates[idx] = malloc(7);
        strcpy(plates[idx], buffer);

        // Increment index
        idx++;
    }

    for (int i = 0; i < 8; i++)
    {
        printf("%s\n", plates[i]);
    }

    // Close file
    fclose(infile);

    // Free memory
    for (int i = 0; i < 8; i++)
    {
        free(plates[i]);
    }
}
