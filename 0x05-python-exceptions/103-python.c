#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>

/**
 * print_python_list - Prints information about a Python list object
 * including its size, allocated space, and element types
 * @p: PyObject pointer representing the Python list object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
	printf("[*] Python list info\n  [ERROR] Invalid List Object\n");
	return;
	}

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; ++i)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Inspects a Python bytes object, printing its size
 * @p: Python object to inspect
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	unsigned char *str;

	if (!PyBytes_Check(p))
	{
	printf("[.] bytes object info\n  [ERROR] Invalid Bytes Object\n");
	return;
	}

	size = PyBytes_Size(p);
	str = (unsigned char *)PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: ");

	for (i = 0; i < size && i < 10; ++i)
	{
		printf("%c", str[i]);
	}
	printf("\n  first 10 bytes:");

	for (i = 0; i < size && i < 10; ++i)
	{
		printf(" %02x", str[i]);
	}
	printf("\n");
}

/**
 * print_python_float - Inspects a Python float object, retrieving its
 * value and printing it as a string
 * @p: Python object to inspect
 */
void print_python_float(PyObject *p)
{
	double val;

	if (!PyFloat_Check(p))
	{
	printf("[.] float object info\n  [ERROR] Invalid Float Object\n");
	return;
	}

	val = PyFloat_AsDouble(p);
	printf("[.] float object info\n  value: %f\n", val);
}

