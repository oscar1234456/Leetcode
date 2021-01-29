#include <iostream>
using namespace std;

void divide(int num, int numArray[], int &cnt){
    for(cnt=0;num!=0;cnt++){
        numArray[cnt] = num%10;
        num /= 10;
    }
}

int main(){
    int input_num1,input_num2;

    while (cin>>input_num1>>input_num2)
    {
        if(!input_num1&&!input_num2){break;}
        int num1[11]={}, num2[11]={};
        int lenA,lenB;
        int sum[12]={};
        divide(input_num1, num1, lenA);
        divide(input_num2, num2, lenB);
        int len = max(lenA, lenB);
        int ans=0;
        for(int i=0;i<len;i++){
            int temp = num1[i]+num2[i];
            if(temp>=10){
                ans+=1;
                num1[i+1]+=1;
            }
        }
        if(ans==0){
            cout<<"No carry operation."<<endl;
        }else if(ans==1){
            cout<<1<<" carry operation."<<endl;
        }else{
            cout<<ans<<" carry operations."<<endl;
        }
        
    }
    

    return 0;
}