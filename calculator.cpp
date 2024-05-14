#include<iostream>
using namespace std;

int add_integers(int x,int y)
{
    int addition = x+y;
    return addition;
}

int subtraction(int x,int y)
{
    int subtraction = x-y;
    return subtraction;
}

int multiply(int x,int y) {
    int multiplication = x*y;
    return multiplication;
}

int division(int x,int y)
{   if(y==0) {
        cout<<"Error: Division by Zero"<<endl;
        return 0;
    }
    int division = x/y;
    return division;
}

void user_input(int &Num1,int &Num2){
    cout<<"Enter The Value of Num1 : "<<endl;
    cin>>Num1;
    cout<<"Enter The Value of Num2 : "<<endl;
    cin>>Num2;    
}

int main() {
    char choice;
   
    do {
        cout<<"1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n"<<"Enter your choice : "<<endl;
        cin>>choice;
        
        if(choice=='1'||choice=='2'||choice=='3'||choice=='4') {
            int Num1,Num2;
            user_input(Num1,Num2);
            
            switch(choice) {
                case '1': {
                int sum = add_integers(Num1,Num2);
                cout<<"ADDITION"<<endl<<Num1<<" + "<<Num2<<" = "<<sum<<endl;
                break;
                }
            
                case '2': {
                int sub = subtraction(Num1,Num2);
                cout<<"SUBTRACTION"<<endl<<Num1<<" - "<<Num2<<" = "<<sub<<endl;
                break;
                }
            
                case '3': {
                int product = multiply(Num1,Num2);
                cout<<"MULTIPLICATION"<<endl<<Num1<<" x "<<Num2<<" = "<<product<<endl;
                break;
                }
            
                case '4': {
                int div = division(Num1,Num2);
                cout<<"DIVISION"<<endl<<Num1<<" / "<<Num2<<" = "<<div<<endl;
                break;
                }
                
                default:
                    cout<<"INVALID CHOICE"<<endl;
                }
                
        } else {
            cout<<"Invalid Choice"<<endl;
            continue;
        }    
                
                char cont;
                cout<<"Do you want to continue more operations : y/n ? : "<<endl;
                cin>>cont;
                
                if(cont != 'y' && cont != 'Y')
                break;
                
        
            } while(true);
        
        cout<<"GOODBYE !"<<endl;    
return 0;
}










// #include<iostream>
// using namespace std;
// int main(){
//     int a,b;
//     cout<<"Enter the value of a : "<<endl;
//     cin>>a;

//     cout<<"Enter the value of b : "<<endl;
//     cin>>b;

//     char op;
//     cout<<"Enter the operation to be performed : "<<endl;
//     cin>>op;
//     switch( op ){
//         case '+' : cout<<a+b<<endl;
//             break;

//         case '-' : cout<<a-b<<endl;
//             break;

//         case '*' : cout<<a*b<<endl;
//             break;

//         case '/' : cout<<a/b<<endl;
//             break;

//         case '%' : cout<<a%b<<endl;
//             break;

//         default : cout<<"Enter a valid operation"<<endl;
//     }

//     return 0;
// }