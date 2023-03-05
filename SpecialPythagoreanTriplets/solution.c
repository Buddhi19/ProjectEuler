#include <stdio.h>

int main(){
    int a,b;
    for(a=1;a<1000;a++){
        for(b=a;b<1000;b++){
            int c = 1000-a-b;
            int newa=a*a;
            int newb=b*b;
            if (newa + newb ==c*c){
                int product;
                product=a*b*c;
                printf("%d\n",product);
                break;
            }
        }
    }
    return 0;
}

/*
buddhi@DESKTOP-IQ34BAB:/mnt/d/ProjectEuler/SpecialPythagoreanTriplets$ ./solution
31875000
*/