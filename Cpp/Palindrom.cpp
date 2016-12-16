#include <iostream>
#include <string.h>

using namespace std;

bool palindrom(string b){
	int a;
	a = b.length();
	cout<<a<<endl;
	for (int i=0; i<a/2;i++){
		if (b[i] != b[a-i-1]){
		return false;
		}
	return true;
}}

int main(){
	string c;
	bool d = true;
	while (d){
	cin>>c;
	d = palindrom(c);
}
cout<<"falsz"<<endl;
}
