#include <iostream>
#include <math.h>
#include <conio.h>

using namespace std;


/*void entering(int ta[], int td[], int &a, int &d, char &cha)
{
	char ch;
	do
	{
    	for(int i=0;i<100;i++)
    	{
   		 	ch = getch();
  		  	if ((int)ch>=48 && (int)ch<=57) 
			{
				ta[i]=((int)ch-48);
				cout<<ch;
			}
    		else 
			{
				a=i;
				break;
			}
		}
		if (a==0)
		{
			cout<<"You must give correct something"<<endl;
			entering(ta, td, a, d, cha);
			return;
		} 
	}while(a=0);
	
	
	if (ch != '-' && ch != '*'  && ch != '+')
	{
		cout<<"You must give correct something"<<endl;
		entering(ta, td, a, d, cha);
		return;
	}
	cha=ch;
	cout<<cha;
	do
	{
    	for(int i=0;i<100;i++)
    	{
   			ch = getch();
  		  	if ((int)ch>=48 && (int)ch<=57) 
			{
				td[i]=((int)ch-48);
				cout<<ch;
			}
    		else 
			{
				d=i;
				break;
			}
		}
		if (d=0)
		{
			cout<<"You must give correct something"<<endl;
			entering(ta, td, a, d, cha);
			return;
		}
	}while(d=0);
    cout<<endl;
}*/

void entering(int ta[], int td[], int &a, int &d, char &cha)
{
	string ch;
	getline(cin,ch);
	for(int i=0;i<201;i++)
	{
		if(ch[i] == '-' || ch[i] == '*'  || ch[i] == '+')
		{
			cha=ch[i];
		}
		else if(cha=='/')
		{
			ta[i]=ch[i]-48;
			a=i;
		}
		else if ((int) ch[i]>=48 && (int)ch[i]<=57)
		{
			
			td[i-a-1]=ch[i]-48;
			d=i-a-1;
		}
		else break;
	}
}


void digit_sys(int a[], int b[], int base , int &k, int l){
	int w=0,j=0;
	while (j<=l)
	{
		w+=a[j];
    	while(w>=base)
    	{
    		b[k]=w%base;
    		k+=1;
    		w/=base;
		}
		if(j==l)
		{
			b[k]=w;
			k+=1;
		}
    	j++;
	}
	cout<<endl<<"k= "<<k<<endl;
    /*while(a>0){
    b[k]=a%base;
    k++;
    a/=base;
    }*/
}

int sum(int b[],int c[],int sum1[], int base, int l, int k){  //Dodawanie
    int g = max(l,k);
    for(int i=g-1;i>=0;i--)sum1[i]+=b[i]+c[i];
    
	for(int i=0; i<max(l,k); i++){
        int j=1;
        if (sum1[i]>=base){
           while(sum1[i+j]>=base-1){ 
           j++;
           }
        if(sum1[i+j]<base){ 
        	sum1[i+j]+=1;
        	for(int m=i+j-1;m>i;m--) sum1[m]=sum1[m]-base+1;
        	sum1[i]=sum1[i]-base;
            }
        }
   }
    
    return g+1;
}

int dif(int b[],int c[],int dif1[], int base, int l, int k){ //Odejmowanie
	for(int i=0; i<max(l,k)+1 ;i++) dif1[i]=(b[i]-c[i]);
    
    for(int i=max(l,k); i>0 ;i--){
        int j=1;
        if (dif1[i]<0){
           while(dif1[i+j]==0){ 
           j++;
           }
        if(dif1[i+j]>0){ 
        	dif1[i+j]-=1;
        	for(int m=i+j-1;m>i;m--) dif1[m]=base-1;
        		dif1[i]=base+dif1[i];
            }
        }
   }
	return max(l,k);
}

int multi(int b[],int c[],int multi1[], int base, int l, int k){  //Mnozenie
        
    for(int i=0; i<l;i++)
	{//b 
    	for(int j=0;j<k;j++)
		{//c
			multi1[i+j+1]+=(multi1[i+j]+b[i]*c[j])/base;
    		multi1[i+j]=(multi1[i+j]+b[i]*c[j])%base;
		}
	}
    
    return l+k;
}


int main(){
	char cha='/';
    int ta[100],td[100],a=0,d=0,base,i=0,k=0;
    int b[1000]={NULL};
    int c[1000]={NULL};
    int sum1[1001];
    int dif1[1001];
    int multi1[2000];
    string w("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ");
    
    cout<<"Enter operation (end it with ENTER):\n";
    
    entering(ta, td, a, d, cha);
    
    
    //cin>>a;
    //cin>>d;
    
    cout<<"Enter system: "; 
    cin>>base;
    
    digit_sys(ta, b, base, i, a);
    digit_sys(td, c, base, k, d); 
    
    cout<<"First digit Result: ";
    for(int j=i-1; j>=0;j--) cout<<w[b[j]];
    cout<<endl;
    
    cout<<"Second digit result: ";
    for(int j=k-1; j>=0;j--) cout<<w[c[j]];
    cout<<endl;
	
	if (cha == '+'){
		int z = sum(b, c, sum1, base, i, k);
		cout<<"Sum: ";
    	for(int j=z-1; j>=0;j--) cout<<w[sum1[j]];
    	cout<<endl;
    }
		
    else if (cha == '-'){
    	int z = dif(b,c,dif1,base,i,k);
 		cout<<"Difference: ";
    	for(int j=z-1; j>=0;j--) cout<<w[dif1[j]];
    	cout<<endl;
    }
		
    else if (cha == '*'){
    	int z = multi(b,c,multi1,base,i,k);
		cout<<"Multiplication : ";
		for(int j=z-1; j>=0;j--) cout<<w[multi1[j]];
    	cout<<endl;
    }


    system("pause");
    return 0;
}
