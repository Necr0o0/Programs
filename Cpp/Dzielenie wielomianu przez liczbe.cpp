#include <iostream>

using namespace std;

void horner(int n, int c, int t[])
{
	int tab[21];
	tab[0] = t[0];
	for(int i=1;i<=n;i++)
	{
		tab[i]= c * tab[i-1] +t[i];
	}
	
	for(int i=0;i<=n;i++)
	{
		t[i]=tab[i];
	}
}


int main() {
	int n, c, tab[20];
	while (true)
	{
	cout<<"Podaj maksymalny wspolczynnik: ";
	cin>>n;
	cout<<"Podaj dwumian: x-";
	cin>>c;
	cout<<"Podaj wsspolczynniki: ";
	
	for(int i=0;i<=n;i++)
	{
		cin>>tab[i];
	}
	horner(n,c,tab);
	cout<<"\n\nWielomian:\n";
	
	for(int i=0;i<n;i++)
	{
		if(i==n-1)
		{
			cout<<tab[i];
			break;
		}
		cout<<tab[i]<<"x^"<<n-1-i<<" + ";
	}
	cout<<"\nReszta: "<<tab[n]<<"\n\n\n";
	}
	
	system("pause");
	return 0;
}

