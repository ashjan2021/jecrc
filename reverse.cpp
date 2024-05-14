// Given a signed 32-bit integer x, return x with its digits reversed.
// If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
// then return 0.

#include<iostream>
using namespace std;
int num,reverse,rem;
int main(){
cout<<"Enter the number"<<endl;
cin>>num;
reverse=0;
while(num!=0){
    rem = num % 10;
    reverse = (10 * reverse) + rem;
    num = num / 10;
}
return reverse;
}