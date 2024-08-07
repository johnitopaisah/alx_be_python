#include "header.h"


/**
 * main - Entry point of the program.
 *
 * Opens a file, extracts integers from it, and prints them.
 *
 * Return: 0 on success, 1 on failure.
 */
int main(void)
{
    const char *filename = "file.txt";  /* Name of the file to read */
    FILE *file = fopen(filename, "r");  /* Open the file for reading */

    if (!file)
    {
        printf("Failed to open file %s\n", filename);
        return (1);
    }

    int num_count;
    int *numbers = getInts(file, &num_count);

    if (numbers)
    {
        printf("Numbers extracted: \n");
        for (int i = 0; i < num_count; i++)
        {
            printf("%d\n", numbers[i]);
        }
        printf("\n");
        free(numbers);  /* Free the allocated memory */
    }
    else
    {
        printf("No numbers extracted or memory allocation failed.\n");
    }

    fclose(file);  /* Close the file */
    return (0);
}

/**
 * getInts - Extract integers from a file and return them in a dynamically
 *           allocated array.
 *
 * @f: Pointer to the file to read from.
 * @nbr: Pointer to an integer to store the count of extracted numbers.
 *
 * Return: A pointer to the dynamically allocated array of integers,
 *         or NULL if memory allocation fails or no numbers are found.
 */
int *getInts(FILE *f, int *nbr)
{
    char line[101];  /* Buffer to hold each line of the file */
    int *numbers = NULL;  /* Array to hold all integers found */
    int count = 0;  /* Count of integers found */

    while (fgets(line, sizeof(line), f))
    {
        char *ptr = line;

        while (*ptr)
        {
            /* Skip non-digit characters */
            while (*ptr && !isdigit(*ptr))
            {
                ptr++;
            }

            if (*ptr)
            {
                /* Convert the number from string to integer */
                int num = strtol(ptr, &ptr, 10);

                /* Reallocate memory to hold the new number */
                int *temp = realloc(numbers, (count + 1) * sizeof(int));
                if (!temp)
                {
                    /* Handle memory allocation failure */
                    free(numbers);
                    *nbr = 0;
                    return (NULL);
                }
                numbers = temp;
                numbers[count++] = num;
            }
        }
    }

    *nbr = count;  /* Update the count of numbers found */
    return (numbers);
}
