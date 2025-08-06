#include <stdio.h>
#include <stdlib.h>

/* This function returns a string after allocating memory
 * dinamically with a malloc function. */
char *ps_create(char *s, int len) {
    char *str = (char *)malloc(1+len);
    unsigned char *lenptr = (unsigned char *)str;
    *lenptr = len;
    for (int i = 0; i < *lenptr; i++) {
        str[i+1] = s[i];
    }
    return str;
}


/* This function initialize a string with prefixed length in the first
 * position.
 * Warning: does not check buffer overflow. */
void ps_init(char *s, char *init, int len) {
    unsigned char *lenptr = (unsigned char *)s;
    *lenptr = len;
    for (int i = 0; i < len; i++) {
        s[i+1] = init[i];
    }
}


/* Show the string on the screen. */
void ps_print(char *buf) {
    unsigned char *lenptr = (unsigned char *)buf;
    for (int i = 0; i < *lenptr; i++) {
        putchar(buf[i+1]);
    }
    printf("\n");
    for (int i = 0; i < *lenptr; i++) {
        printf("%d ", buf[i+1]);
    }
    printf("\n");
}


int main(void) {
    char *str = ps_create("Hello World", 11);
    ps_print(str);
    free(str);
    return 0;
}

