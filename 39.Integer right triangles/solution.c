#include <stdio.h>
#include <stdlib.h>

int main(){

    int p;
    scanf("%d",&p);
    int largestcount=0;
    int largep=0;
    int i=12;
    while (i<=p){
        int count=0;
        //printf("%d\n",i);
        for (int a=1;a<i;a++){
            for (int b=a;b<i;b++){
                int c;
                c=i-a-b;
                if(c*c==a*a+b*b){
                    count+=1;
                    //printf("%d %d %d\n",a,b,c);
                }
            }
        }
        if (count>=largestcount){
            largestcount=count;
            largep=i;
        }
    i+=1;
    }
    printf("%d %d\n",largep,largestcount);
    return 0;
}
/*
buddhi@DESKTOP-IQ34BAB:/mnt/d/ProjectEuler/39.Integer right triangles$ ./solution
1000
840 8
*/