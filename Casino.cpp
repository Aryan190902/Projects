#include <bits/stdc++.h>
#include <ctime>
using namespace std;
double money = 1000;
double bet;
char T;

int n, number;
double fmoney = 1000;
void chooseBet()
{
    
    switch(number)
    {
        case 1:
        bet = fmoney*0.1;
        break;
        case 2:
        bet = fmoney*0.25;
        break;
        case 3:
        bet = fmoney*0.5;
        break;
        case 4:
        bet = fmoney;
        break;
        default:
        cout << "Invalid entry. Try again!" << endl;
        cin>>number;
        chooseBet();
        break;

    }
}
int main()
{
    system("cls");
    do
{
    srand (time(NULL));
    int x = rand()%11;
    cout << endl;
    cout << "****Casino****" << endl;
    cout << endl;
    cout << "Khud ko champ samjhte ho? Then choose a number between 0 - 10:" << endl;
    
    cin>>n;
    
    
    
    cout << endl;
    cout << "You have $1000 currently..." << endl;
    cout << "Bet-" << endl;
    cout << "1. 10% of your money" << endl;
    cout << "2. 25% of your money" << endl;
    cout << "3. 50% of your money" << endl;
    cout << "4. Don't take me lightly, I will bet all of it!" << endl << endl;
    cout << "Choose how much you want to bet: ";
    cin>>number;
    chooseBet();
    if(x==n)
    {
        cout << "You won!" << endl;
        fmoney += bet;
        cout << "Current balance: $";
        cout << fmoney << endl;
    }
    else 
    {
        cout << "You lost... Wanna bet again?" << endl;
        cout << "The number was : " << x << endl; 
        fmoney -= bet;
        cout << "Current balance: $";
        cout << fmoney << endl;
    }
    cout << "Do you have the guts to play again? (Y/N) : ";
    cin>>T;
    if(T == 'Y' || T =='y')
    {
        if(fmoney>0)
        cout << "Great, Let's play again!" << endl;
        else 
        cout << "You ran out of money!" << endl;
    }
    else if(T=='N' || T == 'n')
    {
        cout << "What a loser..." << endl;
        break;
    }
    else 
    {
        cout << "Invalid entry... Try again";
        while (T!= 'Y' || T!= 'y' || T != 'N' || T!= 'n')
        {
            cin>>T;
        }
        
    }
}while(fmoney > 0);


    return 0;
}