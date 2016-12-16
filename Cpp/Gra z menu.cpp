#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <windows.h>
#include <time.h>
#include <conio.h>

using namespace std;
string menu[10],settings[10],logo[7];
bool q1=false;
int size=5;

int MoveMenu(int &n,int &p, bool &q);


void Map (int matrix[][50],int P[2], int l)
{
	system("cls");
	for(int i=0;i<size;i++)
	{
		for(int j=0;j<size;j++)
		{
			cout<<(char)matrix[i][j];
		}
		cout<<endl;
	}
	cout<<"Ruch: "<<l<<endl;
}

void MakeMap(int matrix[][50],int P[2])
{
	int x1,x2,y1,y2,b;
	for(int i=0;i<size;i++)
	{
		for(int j=0;j<size;j++)
		{
			matrix[i][j]=176;
		}
	}
	cout<<endl<<"Ile bomb?: ";
	cin>>b;
	cout<<endl;
	x1=rand()%size, x2=rand()%size;
	matrix[x1][x2]=43;
	do{
		y1=rand()%size;
		y2=rand()%size;
	}while(y1==x1 && y2==x2);
	P[0]=x1;
	P[1]=x2;
	if(abs(x1-y1)>0)
	{
		while(x1-y1<0)
		{
			x1++;
			matrix[x1][x2]=108;
		}
		while(x1-y1>0)
		{
			x1--;
			matrix[x1][x2]=108;
		}
	}
	if(abs(x2-y2)>1)
	{
		while(x2-y2<0)
		{
			x2++;
			matrix[x1][x2]=108;
		}
		while(x2-y2>0)
		{
			x2--;
			matrix[x1][x2]=108;
		}
		
	}
	matrix[y1][y2]=48;
	
	int b1,b2;
	for(int i=0;i<b;i++)
	{
		
		do{
			b1=rand()%size;
			b2=rand()%size;
		}while(matrix[b1][b2]!=176);
		matrix[b1][b2]=207;
	}
	for(int i=0;i<size;i++)
	{
		for(int j=0;j<size;j++)
		{
			if(matrix[i][j]==108) matrix[i][j]==176;
		}
	}
	
}

void MoveBot(int matrix[][50],int P[2],int &l,bool &q)
{
	int x=rand()%4;
	if(P[0]==0)
	{
		if(x==3) x=4;
	}
	if(P[1]==0)
	{
		if(x==0) x=4;
	}
	if(P[0]==(size-1))
	{
		if(x==1) x=4;
	}
	if(P[1]==(size-1))
	{
		if(x==2) x=4;
	}
	
	
	switch(x)
	{
		case 0:
			matrix[P[0]][P[1]]=178;
			P[1]--;
			if (matrix[P[0]][P[1]]==48) q=false;
			else matrix[P[0]][P[1]] = 43;
			l++;
			Map(matrix,P,l);
			break;
		case 1:
			matrix[P[0]][P[1]]=178;
			P[0]++;
			if (matrix[P[0]][P[1]]==48) q=false;
			else matrix[P[0]][P[1]] = 43;
			l++;
			Map(matrix,P,l);
			break;
		case 2:
			matrix[P[0]][P[1]]=178;
			P[1]++;
			if (matrix[P[0]][P[1]]==48) q=false;
			else matrix[P[0]][P[1]] = 43;
			l++;
			Map(matrix,P,l);
			break;
		case 3:
			matrix[P[0]][P[1]]=178;
			P[0]--;
			if (matrix[P[0]][P[1]]==48) q=false;
			else matrix[P[0]][P[1]] = 43;
			l++;
			Map(matrix,P,l);
			break;
			
	}
}

void MovePlayer(int matrix[][50],int P[2],int &l,bool &q)
{
	int k;
	k=getch();
	if(k!=224) return;
	k=getch();
	if(P[1]==0)
	{
		if(k==75)
		{
			cout<<"Nie mozesz tego zrobic!\n";
			return;
		}
	}
	if(P[0]==0)
	{
		if(k==72)
		{
			cout<<"Nie mozesz tego zrobic!\n";
			return;
		}
	}
	if(P[1]==(size-1))
	{
		if(k==77)
		{
			cout<<"Nie mozesz tego zrobic!\n";
			return;
		}
	}
	if(P[0]==(size-1))
	{
		if(k==80)
		{
			cout<<"Nie mozesz tego zrobic!\n";
			return;
		}
	}

	if(k==72)
	{
		matrix[P[0]][P[1]]=178;
		P[0]--;
		if (matrix[P[0]][P[1]]==48) q=false;
		else matrix[P[0]][P[1]]=43;
		l++;
		Map(matrix,P,l);
	}
	else if(k==77)
	{
		matrix[P[0]][P[1]]=178;
		P[1]++;
		if (matrix[P[0]][P[1]]==48) q=false;
		else matrix[P[0]][P[1]]=43;
		l++;
		Map(matrix,P,l);
	}
	else if(k==80)
	{
		matrix[P[0]][P[1]]=178;
		P[0]++;
		if (matrix[P[0]][P[1]]==48) q=false;
		else matrix[P[0]][P[1]]=43;
		l++;
		Map(matrix,P,l);
	}
	else if(k==75){
		matrix[P[0]][P[1]]=178;
		P[1]--;
		if (matrix[P[0]][P[1]]==48) q=false;
		else matrix[P[0]][P[1]]=43;
		l++;
		Map(matrix,P,l);
	}
}


void RunGame()
{
	srand(time(NULL));
	bool g=true;
	int P[2], l=0;
	int matrix [size+1][50];
	
	MakeMap(matrix,P);
	Map(matrix,P,l);
	cout<<"Start?\n";
	while(g)
	{
		MovePlayer(matrix,P,l,g);
	}
	cout<<"You win!";
	system("pause");
	system("cls");
}



void DisMenu(string sth[],int n,int p)
{
	cout<<"       "<<sth[0]<<"\n\n";
	for(int i=1;i<n;i++)
		{
			if(i==p) cout<<"\\*/  ";
			else cout<<"    ";
			cout<<sth[i]<<endl;
		}
}

void MakeIntro()
{
	logo[0]="    (                     ";
	logo[1]="  ( )\\               )    ";
	logo[2]="  )((_)  (    (     (     ";
	logo[3]=" ((_)_   )\\   )\\    )\\  ' ";
	logo[4]="  | _ ) ((_) ((_) _((_))  ";
	logo[5]="  | _ \\/ _ \\/ _ \\| '  \\() ";
	logo[6]="  |___/\\___/\\___/|_|_|_|  ";
}

void Intro(string sth[])
{
    for(int i=0;i<6;i++)
	{
        for(int j=7-i;j<7;j++)
		{
            cout<<sth[j]<<endl;
        }
        Sleep(150);
        system("CLS");
    }
    for(int i=0;i<7;i++)
	{
        cout<<sth[i]<<endl;
    }
    cout<<endl;
}


void MakeMenu()
{
	menu[0]="Menu";
	menu[1]="New Game";
	menu[2]="Settings";
	menu[3]="Credits";
	menu[4]="End";
}

void MakeSettings ()
{
	settings[0]="Settings";
	settings[1]="Size of board";
	settings[2]="return";
}

void LoadingScreen()
{
	system("cls");
	cout<<"Loading. . . /";
	MakeMenu();
	Sleep(300);
	system("cls");
	cout<<"Loading. . . \\";
	MakeSettings();
	Sleep(300);
	system("cls");
	cout<<"Loading. . . /";
	MakeIntro();
	Sleep(300);
	system("cls");
	cout<<"Loading. . . \\";
	Sleep(300);
	system("cls");
	cout<<"Loading. . . /";
	Sleep(300);
	system("cls");
	Intro(logo);
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
	int p=1,n=3;
	bool q=true;
	while(q)
	{
		DisMenu(settings,n,p);
		MoveMenu(n,p,q);
	}
}

bool ChooseMenu(int &n, int p)// zatwierdzanie opcji menu
{
    switch(p)
    {
		case 1:
            RunGame();
            return false;
            break;
        case 2:
            Settings();
            return false;
            break;
        case 3:
            Credits();
            return false;
            break;
        case 4:
            return true;
            break;
     }
}

bool ChooseSettings(int p)// zatwierdzanie opcji ustawien
{
	switch(p)
	{
		
		case 1:
			system("cls");
			cout<<"Set new board size(3-50): ";
			do{
				cin>>size;
				if(size<3 || size>50) cout<<"\nWrong number\n";
			}while (size<3 || size>50);
			system("cls");
            return false;
            break;
        case 2:
        	system("cls");
            return true;
        	break;
    }
}

int MoveMenu(int &n,int &p, bool &q)// zmiana pozycji w liscie
{
	int k;
		do{
			k=getch();
		}while(k!=13 && k!=224 &&k !=0 && k!=27);
		if(k==13)
		{
			if(n==5) if(ChooseMenu(n,p))
			{
				q=false;
				return 0;
			}
			if(n==3) if(ChooseSettings(p))
			{
				q=false;
				return 0; 
			}
		}
		else if(k==27)
		{
			system("cls");
			q=false;
			return 0;
		}
		
		if(kbhit()){
		k=getch();

		if (k==72)
		{
			p--;
			if(p==0) p=n-1;
			system("cls");
		}
		else if (k==80)
		{
			p=1+p%(n-1);
				system("cls");
		}
	}
}



int main()
{
	int n=5;
	int p=1;
	bool q=true;
	
	LoadingScreen();
	while (q)
	{
		DisMenu(menu,n,p);
		MoveMenu(n,p,q);
	}
	system("cls");
	cout<<"Thanks for playing with game\nPlease donate the author :)\n\n";
}
