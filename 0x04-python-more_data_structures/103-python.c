#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list - Prints information about a Python list
 * @p: A pointer to a Python object (PyObject) that should represent a list
 *
 * Return: None
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		printf("[*] Python list info\n");
		printf("[!] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: pointer to a Python object (PyObject) that should
 * represent a bytes object.
 * Return: None
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	unsigned char *string;

	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyObject_Size(p);
	string = (unsigned char *)PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", (char *)string);

	printf("  first %ld bytes: ", (size > 10) ? 10 : size);
	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02x", string[i]);
		if (i < size - 1 && i < 9)
		{
			printf(" ");
		}
	}
	printf("\n");
}
