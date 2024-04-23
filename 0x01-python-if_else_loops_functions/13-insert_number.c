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

new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);

new->n = number;
if (*head == NULL)
{
add_nodeint_end(head, number);
return (new);
}
for (ptr = *head; ptr->next != NULL; ptr = ptr->next)
{
if (number < ptr->next->n)
break;
}

if (ptr == *head)
{
new->next = ptr;
*head = new;
}
else
{
new->next = ptr->next;
ptr->next = new;
}

return (new);
}
