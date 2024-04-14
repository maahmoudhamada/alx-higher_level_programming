#include "lists.h"

/**
* check_cycle - Function to check a loop in a linked list
*
* @list: Head of linked list
*
* Return: One (1) if loop detected Zero (0) otherwise
*/

int check_cycle(listint_t *list)
{
listint_t *t, *h;

t = list, h = list;

while (h && t && h->next)
{
t = t->next;
h = h->next->next;
if (t == h)
return (1);
}
return (0);
}

