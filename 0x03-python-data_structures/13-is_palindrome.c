#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    int length = 0, i = 0;
    int *arr;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (current != NULL)
    {
        length++;
        current = current->next;
    }

    arr = malloc(sizeof(int) * length);
    if (arr == NULL)
        return (0);

    current = *head;
    while (current != NULL)
    {
        arr[i] = current->n;
        i++;
        current = current->next;
    }

    for (i = 0; i < length / 2; i++)
    {
        if (arr[i] != arr[length - i - 1])
        {
            free(arr);
            return (0);
        }
    }

    free(arr);
    return (1);
}
