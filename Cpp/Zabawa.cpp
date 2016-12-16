#include<iostream>
#include<windows.h>

using namespace std;

int main(){
	int wylacz;
	cout<<"Masz, poczestuj sie ";
	cin>>wylacz;
	cout<<"aaa, Kuhhwa"<<endl;
	Sleep(4000);
	cout<<"NIE DLA PSA CHROME"<<endl;
	Sleep(2000);
	system("Taskkill /F /IM chrome.exe");
	Sleep(2000);
	cout<<"NIE DLA SMIECIA WINDOWS";
	Sleep(2000);
	system("shutdown -L");
	
	system("pause");
}
