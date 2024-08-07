#ifndef HEADER_H
#define HEADER_H

#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <ctype.h>
#include <stdlib.h>


void printXShape(char *text);
int hexCharToDecimal(char c);
int hexa2decimal(char *str);
int *getInts(FILE *f, int *nbr);


#endif

