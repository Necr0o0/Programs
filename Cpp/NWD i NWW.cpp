#include <iostream>

using namespace std;

int NWD (int a, int b){
	
	if (a==b) return a;
	else if (a<b) return NWD(a,b-a);
	else return NWD(a-b,b);	
	
}

int NWW(int a, int b){
	
	int la[a],lb[b],d=1,c=0,e=0;
	
	for(int i=2;i<=a+1;i++)
	{
		while (true)
		{
			if (a%i==0)
			{
				la[c] = i;
				c++;
				a /= i;
			}
			else break;
		}
	}
	
	
	for(int i=2;i<=b+1;i++)
	{
		while (true)
		{
			if (b%i==0)
			{
				lb[e] = i;
				e++;
				b /= i;
			}
			else break;
		}
	}
	

	
	int c1 = min(c,e);
	int e1 = max(c,e);
	int z=0;
	
	for(int i=0;i<=c1;i++)
	{
		for(int j=z;j<=e1;j++)
		{
			if(la[i]==lb[j])
			{
				la[j]=1;
				z=j+1;
				break;
			}
		}
	}
	
	

	
	
	for(int i=0;i<c;i++){
		d *=la[i];
	}
	
	for(int i=0;i<e;i++){
		d *=lb[i];
	}
	
	return d;
}


int main() {
	
	int a,b;
	
	while (true){
		cin>>a>>b;
		cout<<"Najwiekszy wspolny dzielnik wynosi "<<NWD(a,b)<<"\nNajmniejsza wspolna wielokrotnosc wynosi: "<<NWW(a,b)<<"\n\n";
	}
	
	system("pause");
	return 0;
}



/*
	cout<<endl;
	for(int i=0;i<c;i++){
		cout<<la[i]<<"   ";
	}
	cout<<endl;
	for(int i=0;i<c;i++){
		cout<<lb[i]<<"   ";
	}
	cout<<endl;
*/
