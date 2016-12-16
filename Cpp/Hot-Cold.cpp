#include <iostream>
#include <conio.h>
#include <time.h>
#include <stdlib.h>
#include <windows.h>

using namespace std;

int i=1,j=0,mi,ma,s,p;
string g,win;
char d,p1,l;

void LoD(){
	cout<<"Choose difficult level:\n1 - ridiculous\n2 - easy\n3 - normal\n4 - hard\n5 - impossible\n";
	d = getch();
	switch(d){
		case '1':
			if (i <= (p/20)+1) win="That wasn't hard, was it?\nMaybe it's time to go level higher?\n";
			else win = "Really?\nYou can do better\n";
			break;
		case '2':
			if (i <= (p/15)+1) win = printf("You needed only %d guesses\nMaybe it's time to go level higher?\n", i);
			else win = printf("You needed %d guesses\n", i);
			break;
		case '3':
			if (i <= (p/13)+1) win = printf("You needed only %d guesses\nMaybe it's time to go level higher?\n", i);
			else win = printf("You needed %d guesses\n", i);
			break;
		case '4':
			if (i <= (p/10)+1) win = printf("You needed only %d guesses\n", i);
			else win = printf("You needed %d guesses\n", i);
			break;
		case '5':
			win = "Cheater";
			break;
	}}
	
void SoB(){
	cout<<"\nChoose size of board:\n1 - small (50)\n2 - normal (100)\n3 - big (150)\n4 - very big (200)\n5 - custom\n";
	p1 = getch();
	switch (p1){
		case '1':
			p = 50;
			break;
		case '2':
			p = 100;
			break;
		case '3':
			p = 150;
			break;
		case '4':
			p = 200;
			break;
		case '5':
			cout<<"Enter number:\n";
			cin>>p;
			cout<<endl; 
			break;
	}
	
}

string los(int a,int b,int p){
	switch(d){
		case '1':
			g=printf("You are about %d point away from target\n",abs(a-b)/(p/20)*(p/20));
			break;
		case '2':
			if (abs(a-b) <=0.05*p) g="Burning!\n";
			else if(abs(a-b) <=0.11*p) g="Hot\n";
			else if(abs(a-b) <=0.23*p) g="Warm\n";
			else if(abs(a-b) <=0.36*p) g="Cold\n";
			else if(abs(a-b) <=0.65*p) g="Freeze\n";
			else g="Blizzard!\n";
			Sleep(1000);
			break;
		case '3':
			if(abs(a-b) <=0.11*p) g="Hot\n";
			else if(abs(a-b) <=0.23*p) g="Warm\n";
			else if(abs(a-b) <=0.36*p) g="Cold\n";
			else if(abs(a-b) <=0.65*p) g="Freeze\n";
			else g="Blizzard!\n";
			Sleep(1000);
			break;
		case '4':
			if(abs(a-b) <=0.23*p) g="Hot\n";
			else if(abs(a-b) <=0.36*p) g="Warm\n";
			else if(abs(a-b) <=0.65*p) g="Cold\n";
			else g="Blizzard!\n";
			Sleep(1000);
			break;
		case '5':
			g="Nope";
			a = rand()%p+1;
			break;
	}
	return g;
}

void quiz(){
	j++;
	int a,b;
	srand(time(NULL));
	a = rand()%p+1;
	cout<<a<<endl;
	printf("This is your %d game\n", j);
	Sleep(2000);
	while (a!=b){
		cout<<"Write your guess: ";
		cin>>b;
		Sleep(1000);
		if (a!=b){
			cout<<los(a,b,p);
		i++;
		}
	}
	cout<<"\nYou win!\n";
	Sleep(1000);
	cout<<win<<endl;
}

int main() {
	cout<<"Here you have the most fantastic game in the world!\n\n";
	Sleep(2000);
	LoD();
	SoB();
	quiz();
	mi=ma=s=i;
	i=1;
	cout<<"What do you want to do now?\nTo play again press 1\nTo exit press 0\nTo change difficult press 2\nAnd to change press 3\n\n";
	bool q=true;
	while(q==true){
		l=getch();
		switch(l){
			case '1':
				cout<<"\nOK. Here you go";
				Sleep(2000);
				system("cls");
				quiz();
				if (mi>i) mi=i; if (ma<i) ma=i; s+=i; i=1;
				cout<<"What do you want to do now?\nTo play again press 1\nTo exit press 0\nTo change difficult press 2\nAnd to change press 3\n\n";
				break;
			case '0':
				q=false;
				break;
			case '2':
				LoD();
				cout<<"What now?";
				break;	
			case '3':
				SoB();
				cout<<"What now?";
				break;	
			default:
				cout<<"\nPress diffrent number\n";
				break;
		}
	}
	printf("\nYou have played %d games\nYour best score is: %d \nYour worst score is: %d\nYour average score is: %d\n", j,mi,ma,s/j);
	system("pause");
	return 0;
}
