#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the list
 * Return: 1 if there is a cycle, 0 if no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slower, *faster;

	if (list == NULL)
		return (0);

	slower = list;
	faster = list;

	while (faster != NULL && faster->next != NULL)
	{
		slower = slower->next;
		faster = faster->next->next;

		if (slower == faster)
			return (1);
	}

	return (0);
}
