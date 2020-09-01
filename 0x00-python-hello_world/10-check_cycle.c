#include "lists.h"

/**
 * check_cycle - Checks for cycle in singly linked list.
 * @list: List to check.
 * Return: 0 if no cycle, else 1.
 */

int check_cycle(listint_t *list)
{
	listint_t *check, *head;

	head = list;
	check = list;

	while (check != NULL && check->next != NULL)
	{
		head = head->next;
		check = check->next->next;
		if (head == check)
			return (1);
	}
	return (0);
}
