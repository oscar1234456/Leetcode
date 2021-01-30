#include <iostream>
#include<string>
using namespace std;
int main(){
    string n;
    long long int sum[2]={0, 0};
    while(cin>>n and n!="0"){
        for(int i=0;i<n.length();i++){
            sum[i%2]+=n[i]-'0';
        }
        if((sum[0]-sum[1])% 11 == 0){
            cout<<n<<" is a multiple of 11."<<endl;
        }else{
            cout<<n<<" is not a multiple of 11."<<endl;
        }
        sum[0] = 0;
        sum[1] = 0;
    }
    return 0;
}