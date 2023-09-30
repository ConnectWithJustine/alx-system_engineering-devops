#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
/**
 * infinite_while - Function thhat create infinite loop
 * Return: 0 on success
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - nothing
 * Return: 0 on success
 */

int main(void)
{
	pid_t child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
		else if (child_pid < 0)
		{
			perror("Fork failed");
			exit(1);
		}
	}

	infinite_while();
	return (0);
}
