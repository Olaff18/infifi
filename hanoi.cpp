#include <iostream>

using namespace std;

int krazki(int n){
    if(n==1){
        return 1;
    }
    else{
        return krazki(n-1)+1+krazki(n-1);
    }
}


int main()
{
    int n;
    cout<<"Podaj liczbe krazkow: "<<endl;
    cin>>n;
    cout<<krazki(n);
    return 0;
}
