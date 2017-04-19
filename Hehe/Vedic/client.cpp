#include<iostream>
#include<stdlib.h>
#include<sys/types.h>
#include<sys/shm.h>
#include<unistd.h>
#define KEY 1234
#define size_h 1024 
using namespace std;
int main()
{
	int shm_id;
	key_t key=KEY;
	
	shm_id=shmget(key,size_h,IPC_CREAT | 0666);
	
	if(shm_id<0)
	{
		cout<<"error has occured!!!"<<endl;
		exit(0);
	}
	
	int *addr;
	addr=(int *)shmat(shm_id,NULL,0);
	int *int_addr=(addr+1);
	cout<<"Enter the number "<<endl;
	cin>>*int_addr;
	*addr=-20;
	while(*addr!=-10)
	{
		sleep(1);
	}
	cout<<"square number is : "<<*int_addr<<endl;
	return 0;
}
	
	
	
