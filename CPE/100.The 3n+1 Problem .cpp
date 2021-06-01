#include <iostream>
#include <fstream>
using namespace std;
int lazz(int n){
    int count=1;
    if(n==1){return 1;}
    do{
        count++;
        if (n%2==0){
            //not odd
            n /= 2;
        }else{
            //odd
            n = 3*n+1;
        }
    }while(n!=1);

    return count++;
}

int main(){
    int input_num1, input_num2;
    // fstream file;
    // file.open("Reader.txt",ios_base::out|ios_base::trunc);
    while(cin>>input_num1>>input_num2){
        int maxResult=0;
        
        int mix = input_num1+input_num2;
    
        int maxNum = max(input_num1,input_num2);
        int minNum = mix - maxNum;
       
        for(;minNum<=maxNum;minNum++){
            int tempRes = lazz(minNum);
            
            if(tempRes>maxResult){
                maxResult = tempRes;
            }
        }
        // cout<<"Lazz:"<<lazz(input_num1)<<endl;
    //    file<<input_num1<<" "<<input_num2<<" "<<maxResult<<endl;
    cout<<input_num1<<" "<<input_num2<<" "<<maxResult<<endl;
    
    }
    // file.close();
    // cout<<input_num1<<" "<<input_num2<<" "<<maxResult;
    return 0;
}