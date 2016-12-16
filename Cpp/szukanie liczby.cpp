#include <iostream>

using namespace std;

int tab[100];

int szukaj(int l, int p, int szukana)
{
	int half;
	while(l<=p)
	{
		half=(l+p)/2;
		
		if(tab[half]==szukana) return half;
		
		if(tab[half]<szukana) l=half+1;
		
		else p=half+1;
	}
	
	return -1;
}

int main()
{
	int n, szukana;
	srand(time(NULL));
	cout<<"Rozmiar tablicy: "
	cin>>n;
	cout<<"\nElementy tablicy\n";
	tab[0]=rand()%n;
	for(int i=0; i<n;i++)
	{
		tab[i] = tab[i-1]+1+rand()%(10/n+1);
		cout<<tab[i]<<endl;
	}
	cout<<"Szukana liczba ";
	cin>>szukana;
	int pozycja = szukaj(0,n-1,szukana);
	
	
	
	system("PAUSE");
	return 0;
}
