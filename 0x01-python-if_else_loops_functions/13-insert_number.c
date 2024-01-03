#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to the first node.
 * @number: number to be inserted.
 * Return: address of new node or NULL.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *mynod = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (mynod == NULL || mynod->n >= number)
	{
		new->next = mynod;
		*head = new;
		return (new);
	}

	while (mynod && mynod->next && mynod->next->n < number)
		mynod = mynod->next;

	new->next = mynod->next;
	mynod->next = new;

	return (new);
}
