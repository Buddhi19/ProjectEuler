#include <stdio.h>

int gcd(int a,int b){
    if(a==0){
        return b;
    }
    return gcd(b%a,a);
}

int lcm(int a, int b){
    return(a/gcd(a,b))*b;
}

int main(){
    int input1,input2;
    scanf("%d %d",&input1,&input2);
    int prelcm=1;
    for (int a=input1;a<input2+1;a++){
        prelcm= lcm(prelcm,a);
    }
    printf("%d\n",prelcm);

    return 0;
}