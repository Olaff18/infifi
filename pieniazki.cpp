#include <iostream>

using namespace std;

int main()
{
    int k,n;
    cin>>n>>k;
    bool tak = 0;
    for(int i=0; i<=k/5; i++){
        for(int j=0; j<=(k-i*5); j++){
            for(int l=0; l<= (k-i*5)-(j*2); l++){
                if(i*5+j*2+l==k && i+j+l==n){
                    cout<<i << " monet/y 5zl, "<<j<<" monet/y 2zl " << l << " monet/y 1zl"<<endl;
                    tak=1;
                }
            }
        }
    }
    if(tak==0){
        cout<<"niemozliwe";
    }
    return 0;
}
