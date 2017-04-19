#include<iostream>
using namespace std;
#include<sys/shm.h>
#include<unistd.h>
#include<sys/types.h>
#include<stdlib.h>
#define KEY 1234
#define SIZE_H 1024


int method_one(int num)
{
	int n1,n2;
	n1=num-10;
	n2=(n1+num)*10+(n1*n1);
	return n2;
	
}
int method_two(int num)
{
	int n1,n2;
	n1=num/10;
	n2=num%10;
	int square=(n1*n1*100)+(n1*n2*2*10)+(n2*n2);
	return square;
}

int main()
{
	int shm_id;
	key_t key=KEY;
	shm_id=shmget(key,SIZE_H,IPC_CREAT|0666);
	
	if(shm_id<0)
	{
		cout<<"error occured!!!"<<endl;
		exit(0);
	}
	
	int *addr;
	
	addr=(int *)shmat(shm_id,NULL,0);
	int *int_addr=(addr+1);
	
	*addr=-10;
	while(*addr!=-20)
	{
		sleep(1);
	}
	int ch,square;
	cout<<"ENTER THE TYPE : 1.METHOD 1\n\t2.METHOD 2\n";
	cin>>ch;
	if(ch==1)
	{
		cout<<"method 1 is calling....."<<endl;
		square=method_one(*int_addr);
	}
	else if(ch==2)
	{
		cout<<"method 2 is calling....."<<endl;
		square=method_two(*int_addr);	
	}
	*int_addr=square;
	*addr=-10;
	return 0;
}
		
	
