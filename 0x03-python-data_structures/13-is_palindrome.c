#include "lists.h"

/**
 * is_palindrome - A Function To Check if Linked List is Palindrom
 * @head: The Head of The Linked List
 * Return: 1 or 0
*/

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palind(head, *head));
}

/**
 * aux_palind - A Recursive Function
 * @head: The Head of The List
 * @end: The Tail of The List
 * Return: 1 or 0
*/

int aux_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
