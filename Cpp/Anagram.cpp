#include <iostream>
#include <string.h>
#include <cctype>
#include <cstdio>

using namespace std;

string anagram(string word1,string word2){
	int a = word1.length();
	int b = word2.length();
	for (int i=0;i<a-1;i++){
		cout<<"\n\n";
		while (true){
			if (word1[i]== 32 || isdigit(word1[i])){
				for (int j=0; j<a;j++){
					cout<<"zmieniamy "<<word1[i+j]<<" na "<<word1[i+j+1]<<endl;
					word1[i+j] = word1[i+j+1];
				}
				a--;
			}
			else break;
		}
		}
	if (word1[a-1]==32 || isdigit(word1[a-1])){
		a--;
	}
	
	
	for (int i=0;i<b-1;i++){
		cout<<"\n\n";
		while (true){
			if (word2[i]== 32 || isdigit(word2[i])){
				for (int j=0; j<b-1;j++){
					cout<<"zmieniamy "<<word2[i+j]<<" na "<<word2[i+j+1]<<endl;
					word2[i+j] = word2[i+j+1];
				}
				b--;
			}
			else break;
		}
		}
	if (word2[b-1]==32 || isdigit(word2[b-1])){
		b--;
	}
	
	
	if (a != b) return "No\n";
	int count;
	
	for (int i =0; i<a;i++){
		for (int j =0; j<a;j++){
		count = 0;
			if (word1[i] == word2[j]){
				word2[j] = '@';
				count++;
				break;
			}
			
		}
	if (count == 0) return "NO\n";
	}
	return "Yes!";
	
}

int main() {
	string a,b;
	while (true){
		cout<<"Wprowad\253 znak: ";
		getline(cin,a);
		getline(cin,b);
		cout<<anagram(a,b)<<endl;
	}
	
	
	system("pause");
	return 0;
}
