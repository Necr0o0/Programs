#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <windows.h>
#include <time.h>
#include <conio.h>


using namespace std;

void Map (int n, char matrix[][50],int P[2], int l)
{
	system("cls");
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			cout<<matrix[i][j]<<" ";
		}
		cout<<endl;
	}
	cout<<"Ruch: "<<l<<endl;

}

bool 

void MakeMap(int size, char matrix[][50],int P[2],int bombs[][2])
{
	int x1,x2,y1,y2;
	for(int i=0;i<size;i++)
	{
		for(int j=0;j<size;j++)
		{
			matrix[i][j]='-';
		}
	}
	cout<<endl;
	x1=rand()%size, x2=rand()%size;
	matrix[x1][x2]='x';
	do{
		y1=rand()%size;
		y2=rand()%size;
	}while(y1==x1 && y2==x2);
	matrix[y1][y2]='0';
	P[0]=x1;
	P[1]=x2;
	for(int i=0;i<size;i++)
	{
		do{
			bombs[i][0]=rand()%size;
			bombs[i][1]=rand()%size;
		}while(bombs[i][0]==x1 && bombs[i][1]==x2 || bombs[i][0]==y1 && bombs[i][1]==y2);
	}
	for(int i=0;i<size;i++)
	{
		matrix[bombs[i][0]][bombs[i][1]]='B';
	}
}


void MoveBot(int n, char matrix[][50],int P[2],int &l,bool &q)
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
	if(P[0]==(n-1))
	{
		if(x==1) x=4;
	}
	if(P[1]==(n-1))
	{
		if(x==2) x=4;
	}


	switch(x)
	{
		case 0:
			matrix[P[0]][P[1]]='-';
			P[1]--;
			if (matrix[P[0]][P[1]]=='0') q=false;
			else matrix[P[0]][P[1]] = '+';
			l++;
			Map(n,matrix,P,l);
			break;
		case 1:
			matrix[P[0]][P[1]]='-';
			P[0]++;
			if (matrix[P[0]][P[1]]=='0') q=false;
			else matrix[P[0]][P[1]] = '+';
			l++;
			Map(n,matrix,P,l);
			break;
		case 2:
			matrix[P[0]][P[1]]='-';
			P[1]++;
			if (matrix[P[0]][P[1]]=='0') q=false;
			else matrix[P[0]][P[1]] = '+';
			l++;
			Map(n,matrix,P,l);
			break;
		case 3:
			matrix[P[0]][P[1]]='-';
			P[0]--;
			if (matrix[P[0]][P[1]]=='0') q=false;
			else matrix[P[0]][P[1]] = '+';
			l++;
			Map(n,matrix,P,l);
			break;

	}
}


void MovePlayer(int n, char matrix[][50],int P[2],int &l,bool &q, int bombs[][2])
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
	if(P[1]==(n-1))
	{
		if(k==77)
		{
			cout<<"Nie mozesz tego zrobic!\n";
			return;
		}
	}
	if(P[0]==(n-1))
	{
		if(k==80)
		{
			cout<<"Nie mozesz tego zrobic!\n";
			return;
		}
	}


	if(k==72)
	{
		matrix[P[0]][P[1]]='-';
			P[0]--;
			if (matrix[P[0]][P[1]]=='0') q=false;
			else matrix[P[0]][P[1]] = '+';
			l++;
			Map(n,matrix,P,l);
	}
	else if(k==77)
	{
		matrix[P[0]][P[1]]='-';
			P[1]++;
			if (matrix[P[0]][P[1]]=='0') q=false;
			else matrix[P[0]][P[1]] = '+';
			l++;
			Map(n,matrix,P,l);
	}
	else if(k==80)
	{
		matrix[P[0]][P[1]]='-';
			P[0]++;
			if (matrix[P[0]][P[1]]=='0') q=false;
			else matrix[P[0]][P[1]] = '+';
			l++;
			Map(n,matrix,P,l);
	}
	else if(k==75){
		matrix[P[0]][P[1]]='-';
			P[1]--;
			if (matrix[P[0]][P[1]]=='0') q=false;
			else matrix[P[0]][P[1]] = '+';
			l++;
			Map(n,matrix,P,l);
	}
}




int main()
	{
	srand( time(NULL) );
	bool q=true;
	int n, P[2], l=0;
	char k='1';
	do{
		cout<<"\nWprowadz liczbe od 3 do 50:  ";
		cin>>n;
	}while (n<3 || n>50);
	char matrix [n+1][50];
	int bombs [n][2];

	while (k=='1')
	{
  
		MakeMap(n,matrix,P,bombs); 
		Map(n,matrix,P,l); 
		cout<<"Start?\n";
		while(q)
		{
			MovePlayer(n,matrix,P,l,q,bombs);
		}
		cout<<"\nWygrales!\nJesli chcesz grac dalej wcisnij 1 jesli nie wcisnij cos innego.\n";
		q=true;
		l=0;
		k=getch();
	}

	system("pause");
	return 0;
}
