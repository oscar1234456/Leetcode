using namespace std;
int* find(int* a, int len){
    int *result = new int[2];
    int max = -10000;
    int secondMax = -10000;
    for(int i=0;i<len;i++){
        if(a[i]>max){
            secondMax = max;
            max = a[i];
        }else if(a[i]>secondMax){
            secondMax = a[i];
        }
    }
    result[0] = max;
    result[1] = secondMax;
    return result;
}
int main() {
    cout << "Hello World!\n";
    int a[]={-1,-36,-23,100,-603,124,16,19,-32,-6};
    int *b = find(a,10);
    for(int i=0;i<2;i++){
        cout<<b[i]<<endl;
    }
}

