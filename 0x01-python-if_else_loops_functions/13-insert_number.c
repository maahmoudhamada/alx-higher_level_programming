#include "lists.h"

/**
* insert_node - Function to insert node into linked list
*
* @head: Head of linked list
* @number: Data of inserted node
*
* Return: Address of new node
*/

listint_t *insert_node(listint_t **head, int number)
{
listint_t *ptr, *new;

if (*head == NULL || head == NULL)
return (NULL);

new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);

for (ptr = *head; ptr->next != NULL; ptr = ptr->next)
{
if (number < ptr->next->n)
break;
}

new->n = number;
new->next = ptr->next;

if (ptr == *head)
*head = new;
else
ptr->next = new;

return (new);
}
