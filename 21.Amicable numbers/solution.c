#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int sumdev(int n){
    int sum=1;
    int stop;
    stop=pow(n,0.5);
    //printf("%d %d\n",n,stop);
    for (int i=2;i<stop+1;i++){
        if(n%i==0){
            if (i*i==n){
                sum+=n/i;
            }
            else{
                sum+=i+(n/i);
                //printf("%d %d\n",i,sum);
            }
        }
        }
    //printf("%d %d\n",n,sum);
    return sum;
}


int main(){
    int test;
    scanf("%d",&test);
    for (int i=0;i<test;i++){
        int n;
        int ans=0;
        scanf("%d",&n);
        for (int j=10;j<n+1;j++){
            int sum1=0;
            sum1=sumdev(j);
            //printf("%d\n",sum1);
            int sum2;
            sum2=sumdev(sum1);
            if (sum2==j && sum1!=j){
                ans+=j;
                //printf("%d %d\n",j,ans);
            }
        }
        printf("%d\n",ans);
    }
    return 0;
}