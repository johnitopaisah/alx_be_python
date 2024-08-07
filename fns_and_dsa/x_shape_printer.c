#include "header.h"

int main() {
    char text[256];
    printf("Enter a text (less than 256 characters): ");
    fgets(text, 256, stdin);
    text[strcspn(text, "\n")] = 0; // Remove the newline character if it exists

    printXShape(text);
    return 0;
}


void printXShape(char *text) {
    int n = strlen(text);
    if (n == 0)
        return;

    int mid = n / 2;  // Middle index for both even and odd lengths

    for (int i = 0; i < mid; i++) {
        // Print leading spaces
        for (int j = 0; j < i; j++)
            printf(" ");

        // Print the first character
        printf("%c", text[i]);

        // Print spaces between characters
        for (int j = 0; j < 2 * (mid - i) - 1; j++)
            printf(" ");

        // Print the second character
        printf("%c\n", text[n - i - 1]);
    }

    // Print the middle line for odd lengths
    if (n % 2 != 0) {
        for (int i = 0; i < mid; i++)
            printf(" ");
        printf("%c\n", text[mid]);
    }

    // Print the bottom half of the X shape
    for (int i = mid - 1; i >= 0; i--) {
        // Print leading spaces
        for (int j = 0; j < i; j++)
            printf(" ");

        // Print the first character
        printf("%c", text[i]);

        // Print spaces between characters
        for (int j = 0; j < 2 * (mid - i) - 1; j++)
            printf(" ");

        // Print the second character
        printf("%c\n", text[n - i - 1]);
    }
}
