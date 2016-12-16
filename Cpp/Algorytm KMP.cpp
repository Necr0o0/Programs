#include <iostream>
#include <string.h>

using namespace std;




int main()
{
	int licz = 0;
	int P[100];
	char slowo[100],tekst[100];
	int dl = strlen(slowo);
	P[0]=0;
	cin>>slowo;
	
	for(int i=1;i<dl;i++)
	{
		if (licz>0 && slowo[i] != slowo[licz]) licz = P[licz];
		
		if (slowo[i] == slowo[licz]) licz++;
		P[i]=licz;
	}
	int i=0,j=1;
	
	while(i<strlen(slowo)-dl+1)
	{
		i=P[i];
		while(slowo[i]==tekst[j+i-1] && i<dl) i++;
		if (i==dl) cout<<j-1<<endl;
		j+=max(i,i-P[i]);
	}
}
