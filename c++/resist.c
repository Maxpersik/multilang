#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    float S = 0;
    for (int i = 1; i < argc; i++){
       float r = atof(argv[i]);
       S = S + 1/r;
      
    }
    float R = 1/S;
    printf("%s: %f %s\n", "Общее сопротивление равно" ,R, "Ом");
    
}   

