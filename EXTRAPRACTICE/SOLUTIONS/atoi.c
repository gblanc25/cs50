// Practice writing recursive function
// More practice with strings

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int convert(string input);

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("%i\n", convert(input));
}

int convert(string input)
{
    if (strlen(input) == 0)
    {
        return 0;
    }

    // Get index of right most char
    int last_idx = strlen(input) - 1;

    // Convert this char to int
    int value = input[last_idx] - '0';

    // Remove last char from string
    input[last_idx] = '\0';

    // Sum this value with next place value * 10
    return value + 10 * convert(input);
}
