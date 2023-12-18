#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Pointer to a Python object
 */
void print_python_bytes(PyObject *p)
{
	int i;
	char *byte_data = PyBytes_AsString(p);

	Py_ssize_t size = PyBytes_Size(p);

	if (p == NULL)
	{
		printf("Error: Null pointer provided.\n");
		return;
	}

	if (!PyBytes_Check(p))
	{
		printf("Error: Object is not a bytes object.\n");
		return;

		printf("Total size of the bytes object: %zd\n", size);

		printf("Byte data as a string (attempt):\n");
		if (byte_data != NULL)
		{
			printf("%.*s\n", (int)size, byte_data);
		}
		else
		{
	printf("Error: Byte data is not valid ASCII or UTF-8 string.\n");
		}
		printf("First few bytes in hexadecimal format:\n");

		for (i = 0; i < size && i < 10; ++i)
		{
			printf("%02x ", (unsigned char)byte_data[i]);
		}
		printf("\n");
}

/**
 * print_python_list - print python things
 * @p: pointer to PyObject p
 */
void print_python_list(PyObject *p)
{
	size_t a, size, i;
	const char *t;
	PyListObject *list;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (PyList_Check(p) == 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	list = (PyListObject *)p;
	size = PyList_GET_SIZE(p);
	a = list->allocated;
	printf("[*] Size of the Python List = %ld\n[*] Allocated = %li\n", size, a);
	for (i = 0; i < size; i++)
	{
		t = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %li: %s\n", i, t);
		!strcmp(t, "bytes") ? print_python_bytes(list->ob_item[i]) : (void)t;
		!strcmp(t, "float") ? print_python_float(list->ob_item[i]) : (void)t;
	}
}

/**
 * print_python_float - print python things
 * @p: pointer to PyObject p
 */
void print_python_float(PyObject *p)
{
	char *str;
	double f;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (PyFloat_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	f = ((PyFloatObject *)(p))->ob_fval;
	str = PyOS_double_to_string(f, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}
