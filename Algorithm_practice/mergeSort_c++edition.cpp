#include <iostream>
using namespace std;

void mergeSort(int[], int, int);
void merge(int[], int ,int ,int);
int counts = 0;
int main() {
    cout << "Hello World!\n";
    int a[] = {7,3,1,5,2,6,4};
    cout<<"enteer:" <<sizeof(a)<<endl;
    mergeSort(a,0,6);
    // merge(a,0,3,6);
    for(int i=0;i<7;i++){
        cout<<"a(finnal):"<<a[i]<<endl;
    }
}

void mergeSort(int* A, int p, int q){
    if(p<q){
        int m = (p+q)/2;
        mergeSort(A, p, m);
        mergeSort(A, m+1, q);
        merge(A,p,m,q);
    }
}

void merge(int* A, int p, int m, int q){
    int n0 = m-p+1;
    int n1 = q-(m+1)+1;
    int *L = new int[n0+1];
    int *R = new int[n1+1];
    for(int i=p; i<=m;i++){
        L[i-p] = A[i];
    }
    for(int i=m+1; i<=q;i++){
        R[i-(m+1)] = A[i];
    }
    L[n0] = 100000000000;
    R[n1] = 100000000000;
    // for(int i=0;i<n0+1;i++){
    //     cout<<"L:"<<L[i]<<endl;
    // }
    // for(int i=0;i<n1+1;i++){
    //     cout<<"R:"<<R[i]<<endl;
    // }
    int i = 0;
    int j = 0;
    for(int k=p;k<=q;k++){
        if (L[i]<=R[j]){
            A[k] = L[i];
            i+=1;
            cout<<"i:"<<i<<endl;
        }else{
            A[k] = R[j];
            j+=1;
            cout<<"j:"<<j<<endl;
        }
    } 
    
    for(int i=0;i<7;i++){
        cout<<"a(merge):"<<counts<<"//"<<A[i]<<endl;
    }
    counts++;
    
}