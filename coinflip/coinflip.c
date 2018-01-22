#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main(void){
    srand(time(NULL));
    int r = rand() % 2;

    if (r==0) {
        puts("Heads");
    } else {
        puts("Tails");
    }

	return 0;
}
