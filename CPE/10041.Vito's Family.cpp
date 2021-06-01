#include<iostream>
#include<algorithm>
#include <vector>
vector<int> mylist;
using namespace std;
int main() {
    int n;
    cin>>n; //load data
    while(n--){
        int s,t;
        cin>>s;
        mylist.clear();
        for(int i=0;i<s;i++){
            cin>>t;
            mylist.push_back(t);
        }
        sort(mylist.begin(), mylist.end());
        int mid = mylist[s/2], res=0;
        for(int i=0;i<s;i++){
            res+=abs(mylist[i]-mid);
        }
        cout<<res<<endl;
    }
}