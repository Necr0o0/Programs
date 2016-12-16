#include <iostream>

using namespace std;

int a,b,c,d;

void pro(){
	cout<<"Wysokosc:"<<endl;
	cin>>a;
	cout<<endl<<"Szerokosc"<<endl;
	cin>>b;
	cout<<endl<<"Oto twoj prostokat:"<<endl;
	for (int i=0;i<a;i++){
		for (int j=0;j<b;j++){
			cout<<"X";
		}
		cout<<endl;
	}
	cout<<endl;
}

void tro(){
	cout<<"Wysokosc:"<<endl;
	cin>>c;
	cout<<endl<<"Szerokosc"<<endl;
	cin>>d;
	cout<<endl<<"Oto twoj trojkat:"<<endl;
	for (int i=0;i<c;i++){
		for (int j=0;j<=i;j++){
			cout<<"X";
		}
	cout<<endl;
	}
	cout<<endl;
}

int main(){
	cout<<"Prosze podac wymiary prostokata:"<<endl;
	pro();
	cout<<"Prosze podac wymiary trojkata:"<<endl;
	tro();
	if ((c<=a)&&(d<=b)||(c<=b)&&(d<=a)){
		cout<<"Ten trojkat zmiesci sie w tym prostokacie."<<"\n\n";
	}
	else{
		cout<<"Ten trojkat nie zmiesci sie w tym prostokacie."<<"\n\n";
	}
	
	system("pause");
	return 0;
}
