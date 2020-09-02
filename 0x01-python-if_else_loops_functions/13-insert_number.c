#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Head of list.
 * @number: Number to store in new node.
 * Return: Address of new node or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head, *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;

	while (tmp->next->n < number)
		tmp = tmp->next;

	new->next = tmp->next;
	tmp->next = new;

	return (new);
}
