// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

string replace(string word);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./novowels word\n");
        return 1;
    }

    printf("%s\n", replace(argv[1]));
}

string replace(string word)
{
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        switch (toupper(word[i]))
        {
            case 'A':
                word[i] = '6';
                break;
            case 'E':
                word[i] = '3';
                break;
            case 'I':
                word[i] = '1';
                break;
            case 'O':
                word[i] = '0';
                break;
        }
    }
    return word;
}
