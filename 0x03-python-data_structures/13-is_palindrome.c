#include "lists.h"

int is_palindrome_util(listint_t **left, listint_t *right);

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	return (is_palindrome_util(head, *head));
}

/**
 * is_palindrome_util - Utility function for palindrome check using recursion.
 * @left: A pointer to the left node in the linked list.
 * @right: A pointer to the right node in the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome_util(listint_t **left, listint_t *right)
{
	int isp;

	/* Base case */
	if (right == NULL)
		return (1);

	isp = is_palindrome_util(left, right->next);

	if (isp == 0)
		return (0);

	isp = (right->n == (*left)->n);

	*left = (*left)->next;

	return (isp);
}
