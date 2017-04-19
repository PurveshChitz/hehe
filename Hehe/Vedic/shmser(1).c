#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
 

#define SHMSZ     27

int main()
{
    char c;
    int shmid,ch;
    key_t key;
    char *shm, *s;
	int i,n=52;
    /*
     * We'll name our shared memory segment
     * "5678".
     */
    key = 5678;

    /*
     * Create the segment.
      shmget() is used to obtain access to a shared memory segment. It is prottyped by:

int shmget(key_t key, size_t size, int shmflg);

The key argument is a access value associated with the semaphore ID. The size argument is the size in bytes of the requested shared memory. The shmflg argument specifies the initial access permissions and creation control flags.

When the call succeeds, it returns the shared memory segment ID. This call is also used to get the ID of an existing shared segment (from a process requesting sharing of some existing memory portion). 



    shm_id = shmget(
                   key_t     k,         the key for the segment         */
                   //int       size,     /* the size of the segment         */
                  // int       flag);    /* create/use flag                 

/*In the above definition, k is of type key_t or IPC_PRIVATE. It is the numeric key to be assigned to the returned shared memory segment. size is the size of the requested shared memory. The purpose of flag is to specify the way that the shared memory will be used. For our purpose, only the following two values are important:

    IPC_CREAT | 0666 for a server (i.e., creating and granting read and write access to the server)
    0666 for any client (i.e., granting read and write access to the client)*/

    
    if ((shmid = shmget(key, SHMSZ, IPC_CREAT | 0666)) < 0) {
        perror("shmget");
        return 1;
    }

    /*
     * Now we attach the segment to our data space.
         void *shmat(int shmid, const void *shmaddr, int shmflg);

 DESCRIPTION

    The shmat() function attaches the shared memory segment associated with the shared memory identifier specified by shmid to the address space of the calling process. The segment is attached at the address specified by one of the following criteria:

        If shmaddr is a null pointer, the segment is attached at the first available address as selected by the system.

        If shmaddr is not a null pointer and (shmflg&SHM_RND) is non-zero, the segment is attached at the address given by (shmaddr-((uintptr_t)shmaddr%SHMLBA)) The character % is the C-language remainder operator.

        If shmaddr is not a null pointer and (shmflg&SHM_RND) is 0, the segment is attached at the address given by shmaddr.

        The segment is attached for reading if (shmflg&SHM_RDONLY) is non-zero and the calling process has read permission; otherwise, if it is 0 and the calling process has read and write permission, the segment is attached for reading and writing. 
     */
    if ((shm = shmat(shmid, NULL, 0)) == NULL) {
        perror("shmat");
        return 1;
    }
    
   
     while (*shm != '*')
        sleep(1);
    
    printf("Enter your choice \n 1.Method_1 \n 2.Method_2\n");
    scanf("%d",&ch);
        
    s = shm;
    s++;
    char m=*s;
    int r;
    n=(int)m;
  
  if (ch == 1)
  {
    r=square(n);
  }
  
  if (ch == 2)
  {
    r=square_m2(n);
  }
    s=shm;
    s++;
    
    int a=1000;
    for (i=0;i<4;i++){
        *s = (char)(r/a+48);
        r=r%a;
        a=a/10;
        s++;
        }
    s = NULL;
    *shm='%';
   
    while (*shm != '$')
        sleep(1);

    return 0;
}

int square_m2(int n)
{
 	int dea , num;
 	dea = n - 10;
 	num = (n + dea)*10;
 	dea = dea*dea;
 	num = num + dea;
 	return num;
}
int square(int n){
	int a,b;
	a=n/10;
	b=n%10;
	int res=a*a*100+a*b*2*10+b*b;
	return res;
}
