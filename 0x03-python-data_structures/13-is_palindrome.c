#include "lists.h"

/**
* list_len - Function to get length of linked list
*
* @h: Head of linked list
*
* Return: Length of list (integer)
*/
int list_len(listint_t *h)
{
listint_t *pt;
int len = 0;

for (len = 0, pt = h; pt; pt = pt->next, len++)
;
return (len);
}

/**
* split_list - Function to split and reverse linked list
*
* @head: Head of the linked list
* @idx: Index of where to start spliting
*
* Return: pointer to the new splitted list
*/

listint_t *split_list(listint_t **head, int idx)
{
listint_t *head2, *before, *ptr, *nextnode;
int i = 0;

before = *head;
for (i = 0; i < idx - 1; i++)
before = before->next;

ptr = before->next;
before->next = NULL;
before = NULL;

for (; ptr->next;)
{
nextnode = ptr->next;
ptr->next = before;
before = ptr;
ptr = nextnode;
}
ptr->next = before;
head2 = ptr;

return (head2);
}
/**
* is_palindrome - Function to scan if a list is plaindrome or not
*
* @head: Head of linked list
*
* Return: One (1) if it's plaindrome Zero (0) otherwise
*/

int is_palindrome(listint_t **head)
{
listint_t *h2, *p1, *p2;
int len = list_len(*head), i = 0;

if (head == NULL || *head == NULL || len == 1)
return (1);

h2 = split_list(head, len / 2);
p1 = *head, p2 = h2;

for (i = 0; i < len / 2; i++)
{
if (p1->n != p2->n)
return (0);
p1 = p1->next, p2 = p2->next;
}
return (1);
}

