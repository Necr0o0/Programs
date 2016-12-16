#include <iostream>
#include <math.h>

using namespace std;

float pole_kuli(float promien){
	float a = 4*M_PI*promien*promien;
	return a;
}

float pole_walca(float promien, float wysokosc){
	float a = 2*M_PI*promien*promien+2*M_PI*promien*wysokosc;
	return a;
}
void figura(float &pole, string a){
	int r;
	if (a == "kula"){
		cout<<"\nProsze podac promien: ";
		cin>>r;
		pole = pole_kuli(r);
		cout<<"\nPole kuli wynosi: "<<pole<<endl;
	}
	else if (a == "walec"){
		int h;
		cout<<"\nProsze podac promien i wysokosc: ";
		cin>>r>>h;
		pole = pole_walca(r,h);
		cout<<"\nPole walca wynosi: "<<pole<<endl;
		
	}
}


int main(){
	string a;
	float be;
	cout<<"Podac pole walca czy kuli?\n";
	cin>>a;
	figura(be,a);

system("PAUSE");
return 0;
}
