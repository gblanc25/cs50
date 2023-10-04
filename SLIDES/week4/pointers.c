// Pointer Syntax and Number Representation Exercises
// Created by Gabe LeBlanc

// usage: ./pointers QUESTION_NUMBER
// ex: ./pointers 3

// don't forget to run 'make pointers' before starting

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // check proper usage
    if (argc != 2)
    {
        printf("usage: ./pointers QUESTION_NUMBER");
        return 1;
    }

    // we'll store answers in an array for easy printing
    int answers[10];

    // exercise 0
    // think about the answer, THEN run ./pointers 0
    int x = 50;
    int *ptr = &x;
    answers[0] = *ptr;

    // exercise 1
    // keep in mind that the above lines of code still run!
    *ptr = 2;
    answers[1] = *ptr - 2;

    // exercise 2
    answers[2] = x;

    // exercise 3
    answers[3] = *&x;

    // exercise 4
    // don't forget, answers is an integer array
    // https://www.asciitable.com/
    char *name = "GABE123";
    answers[4] = name[1];

    // exercise 5
    answers[5] = *name;

    // exercise 6
    answers[6] = *(name + 2);

    // exercise 7
    int count = 0;
    for (char *strPtr = name; *name != '\0'; name++)
    {
        count++;
    }
    answers[7] = count;

    // exercise 8
    // Convert the binary number 10101 into decimal.

    // ignore this, just to conceal the answer ;)
    answers[8] = 9492 / 452;

    // exercise 9
    // Convert the hexadecimal number 0x2A into decimal.

    // ignore this, just to conceal the answer ;)
    answers[9] = 41454 / 987;

    // print out solution
    int problem = atoi(argv[1]);
    printf("Problem %i Answer: %i\n", problem, answers[problem]);
}

