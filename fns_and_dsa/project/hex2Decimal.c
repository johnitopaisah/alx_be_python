#include "header.h"


/**
 * main - Entry point of the program.
 *
 * Prompts the user to enter a hexadecimal number, validates the input,
 * converts it to a decimal integer, and prints the result.
 *
 * Return: 0 on success, 1 on failure.
 */
int main(void)
{
    char hex[100];
    printf("Enter a hexadecimal number: ");
    scanf("%99s", hex);

    /* Validate the input to ensure it's a valid hexadecimal number */
    for (int i = 0; i < strlen(hex); i++)
    {
        if (!isxdigit(hex[i]))
        {
            printf("Invalid input. Please enter a valid hexadecimal number.\n");
            return (1);
        }
    }

    int decimalValue = hexa2decimal(hex);
    if (decimalValue != -1)
    {
        printf("Decimal value: %d\n", decimalValue);
    }
    return (0);
}



/**
 * hexCharToDecimal - Convert a hexadecimal digit to a decimal value.
 *
 * @c: The hexadecimal character to be converted.
 *
 * Return: The decimal value of the hexadecimal character, or -1 if
 *         the character is not a valid hexadecimal digit.
 */
int hexCharToDecimal(char c)
{
    if (c >= '0' && c <= '9')
        return (c - '0');
    else if (c >= 'a' && c <= 'f')
        return (c - 'a' + 10);
    else if (c >= 'A' && c <= 'F')
        return (c - 'A' + 10);
    return (-1);  /* Return -1 for invalid hexadecimal characters */
}


/**
 * hexa2decimal - Convert a hexadecimal string to a decimal integer.
 *
 * @str: The hexadecimal string to be converted.
 *
 * Return: The decimal integer value of the hexadecimal string, or -1
 *         if an error occurs (invalid character or overflow).
 */
int hexa2decimal(char *str)
{
    int result = 0;
    while (*str)
    {
        int decimalValue = hexCharToDecimal(*str++);
        if (decimalValue == -1)
        {
            printf("Error: Invalid hexadecimal character detected.\n");
            return (-1);
        }
        if (result > (INT_MAX - decimalValue) / 16)
        {
            printf("Error: Integer overflow detected.\n");
            return (-1);
        }
        result = result * 16 + decimalValue;
    }
    return (result);
}
