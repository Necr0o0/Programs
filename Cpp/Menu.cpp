#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <windows.h>
#include <time.h>
#include <conio.h>

using namespace std;
string menu[10],settings[10];
bool q1=false;
int size=5;//rozmiar tablicy

void MoveMenu(int &n,int &p, bool &q);


void DisMenu(string sth[],int n,int p)
{
	for(int i=0;i<n;i++)
		{
			if(i==p) cout<<"[*]  ";
			cout<<sth[i]<<endl;
		}
}

void MakeMenu()
{
	menu[0]="New Game";
	menu[1]="Settings";
	menu[2]="Credits";
	menu[3]="End";
}

void MakeSettings ()
{
	settings[0]="Size of board";
	settings[1]="return";
}

bool Credits()
{
	system("cls");
	cout<<"Ta gre zrobil w calosci Dorian Cichoszewski\nCala chwala, czesc i uwielbienie dla niego!\nJezeli go wielbisz wcisnij D\n";
	char glory = getch();
	system("cls");
	if (glory == 'D') return true;
	else return false;
}

void Settings()
{
	system("cls");
	int p=0,n=2;
	bool q=true;
	while(q)
	{
		DisMenu(settings,n,p);
		MoveMenu(n,p,q);
	}
}

bool ChooseMenu(int &n, int p)
{
     switch(p)
     {
              case 0:
                   //RunGame
                   return false;
                   break;
              case 1:
                   Settings();
                   return false;
                   break;
              case 2:
                   Credits();
                   return false;
                   break;
              case 3:
                   return true;
                   break;
     }
}

bool ChooseSettings(int p)
{
	switch(p)
	{
		
		case 0:
			system("cls");
			cout<<"Wpisz rozmiar tablicy: ";
			cin>>size;
			system("cls");
            return false;
            break;
        case 1:
        	system("cls");
            return true;
        	break;
    }
}


void MoveMenu(int &n,int &p, bool &q){
	int k;
	while (true)
	{		
		k=getch();
		if(k==13)
		{
			if(n==4) if(ChooseMenu(n,p)){
				q=false;
				return;
			}
			if(n==2) if(ChooseSettings(p)){
				q=false;
				return; 
			}
		}
		if(k!=224) return;
		k=getch();
		if (k==72)
		{
			p--;
			if(p==-1) p=n-1;
			system("cls");
			break;
		}
		else if (k==80)
		{
			p++;
			p=p%n;
			system("cls");
			break;
		}
	}
}



int main()
{
	
	int n=4;    //elementy menu
	int p=0;
	bool q=true;
	
	MakeMenu();
	MakeSettings();
	while (q)
	{
		DisMenu(menu,n,p);
		MoveMenu(n,p,q);
	}
}
