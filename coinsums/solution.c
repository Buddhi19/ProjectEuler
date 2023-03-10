#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int solution(int n){
    int arr[8]={1,2,5,10,20,50,100,200};
    int l=n+1;
    int* dp=(int*)malloc(l*sizeof(int));
    if(n==0){
        return 0;
    }
    dp[0]=1;
    for (int j=0;j<8;j++){
        for (int i=arr[j];i<l;i++){
            if((i-arr[j])>=0){
                dp[i]+=dp[i-arr[j]];
            }
        }
    }
    return dp[n];
}

int main(){
    int n;
    scanf("%d",&n);
    int ans;
    ans=solution(n);
    printf("%d\n",ans);
    return 0;
}