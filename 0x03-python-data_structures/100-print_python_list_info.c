#include "python.h"

/**
 * print_python_list_info - A Function
 * @p: A Python Object
*/

void print_python_list_info(pyobject *p)
{
	int size, alloc, i;
	pyobject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size fo the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
