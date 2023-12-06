#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyListObject *list;

	size = PyList_Size(p);
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	PyBytesObject *bytes;
	unsigned char *string;

	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	bytes = (PyBytesObject *)p;
	string = (unsigned char *)bytes->ob_sval;

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
