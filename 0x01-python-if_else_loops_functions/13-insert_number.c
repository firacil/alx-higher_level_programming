#include <stdio.h>
#include <stdlib.h>
#include <lists.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to the first node.
 * @number: number to be inserted.
 * Return: address of new node or NULL.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr;
