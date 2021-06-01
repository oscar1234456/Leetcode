using namespace std;
int main() {
    int a[2][3] = {{1,2,3},{4,5,6}};
    int b[3][2] = {{1,2},{3,4},{5,6}};
    int c[2][2] ={{0,0},{0,0}};
    
    for(int i=0;i<2;i++){
        for(int j=0;j<2;j++){
            for(int k=0;k<3;k++){
                c[i][j]+=a[i][k]*b[k][j];
            }
        }
    }
    
    for(int i=0;i<2;i++){
        for(int j=0;j<2;j++ ){
            cout<<"["<<i<<"]"<<"["<<j<<"]="<<c[i][j]<<endl;
        }
    } 
}