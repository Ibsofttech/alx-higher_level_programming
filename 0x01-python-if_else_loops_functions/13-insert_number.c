#include "list.h"

/**
 * insert_node - a function that add a new node
 * @head: head of the previous nodes
 * @number: number to be inserted
 * Return: a pointer to the new node
*/


listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = *head, *current;

	current = malloc(sizeof(listint_t));
	if (current == NULL)
	{
		return (NULL);
	}

	current->n = number;
	current->next = NULL;

	if (new_node == NULL || new_node->n >= number)
	{
		current->next = new_node;
		*head = current;
		return (current);
	}

	while (new_node && new_node->next && new_node->next->n < number)
	{
		new_node = new_node->next;
	}

	current->next = new_node->next;
	new_node->next = current;

	return (current);
}
