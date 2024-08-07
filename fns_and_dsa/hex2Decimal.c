#include "header.h"


// Function to convert a hexadecimal digit to a decimal value
int hexCharToDecimal(char c) {
    if (c >= '0' && c <= '9')
        return c - '0';
    else if (c >= 'a' && c <= 'f')
        return c - 'a' + 10;
    else if (c >= 'A' && c <= 'F')
        return c - 'A' + 10;
    return -1;  // Return -1 for invalid hexadecimal characters
}

// Function to convert a hexadecimal string to a decimal integer
int hexa2decimal(char *str) {
    int result = 0;
    while (*str) {
        int decimalValue = hexCharToDecimal(*str++);
        if (decimalValue == -1) {
            printf("Error: Invalid hexadecimal character detected.\n");
            return -1;
        }
        if (result > (INT_MAX - decimalValue) / 16) {
            printf("Error: Integer overflow detected.\n");
            return -1;
        }
        result = result * 16 + decimalValue;
    }
    return result;
}

// Main program
int main() {
    char hex[100];
    printf("Enter a hexadecimal number: ");
    scanf("%99s", hex);

    // Validate the input to ensure it's a valid hexadecimal number
    for (int i = 0; i < strlen(hex); i++) {
        if (!isxdigit(hex[i])) {
            printf("Invalid input. Please enter a valid hexadecimal number.\n");
            return 1;
        }
    }

    int decimalValue = hexa2decimal(hex);
    if (decimalValue != -1) {
        printf("Decimal value: %d\n", decimalValue);
    }
    return 0;
}
