#define PY_SSIZE_T_CLEAN
#include <Python.h>

#define MAX_IT 10000

typedef struct {
    int x;
    int y;
} Vertex;

void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

double distance(Vertex a, Vertex b) {
    double dx = a.x - b.x;
    double dy = a.y - b.y;
    return sqrt(dx*dx + dy*dy);
}

double total_distance(Vertex *path, int size) {
    double sum = 0;
    for (int i = 0; i < size; i++) {
        sum += distance(path[i], path[(i+1) % size]);
    }
    return sum;
}

void two_opt(Vertex *path, int i, int j) {
    while (i < j) {
        Vertex tmp = path[i];
        path[i] = path[j];
        path[j] = tmp;
        i++;
        j--;
    }
}

Vertex* simulated_annealing(Vertex *path, int size) {
    for (int i = 100; i >= 1; i--) {
        double t = 0.001 * i * i;
        for (int it = 0; it < MAX_IT; it++) {
            int a = rand() % size;
            int b = rand() % size;
            if (b < a) {
                swap(&a, &b);
            }

            Vertex* path_new = malloc(size * sizeof(Vertex));
            memcpy(path_new, path, size * sizeof(Vertex));

            two_opt(path, a, b);

            if(total_distance(path_new, size) < total_distance(path, size)) {
                memcpy(path, path_new, size * sizeof(Vertex));
            } else {
                double r = (double) rand() / RAND_MAX;
                if (r < exp(- (total_distance(path_new, size) - total_distance(path, size)) / t)) {
                    memcpy(path, path_new, size * sizeof(Vertex));
                }
            }
            free(path_new);
        }
    }
    return path;
}

// Define the function
static PyObject* graph_simulated_annealing(PyObject* self, PyObject* args)
{
    PyObject* input;
    if (!PyArg_ParseTuple(args, "O", &input)) {
        return NULL;
    }

    if (!PyList_Check(input)) {
        PyErr_SetString(PyExc_TypeError, "Input must be a list");
        return NULL;
    }

    Py_ssize_t size = PyList_Size(input);
    Vertex* path = malloc(size * sizeof(Vertex));
    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject* item = PyList_GetItem(input, i);
        if (!PyTuple_Check(item)) {
            PyErr_SetString(PyExc_TypeError, "Items in the list must be tuples");
            return NULL;
        }

        Py_ssize_t tuple_size = PyTuple_Size(item);
        if (tuple_size != 2) {
            PyErr_SetString(PyExc_ValueError, "Tuples in the list must have length 2");
            return NULL;
        }
        
        int x, y;
        if (!PyArg_ParseTuple(item, "ii", &x, &y)) {
            PyErr_SetString(PyExc_TypeError, "Tuple values must be integers");
            return NULL;
        }
        path[i].x = x;
        path[i].y = y;
    }

    path = simulated_annealing(path, (int) size);    

    PyObject* output = PyList_New(size);
    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject* tuple = PyTuple_New(2);
        PyTuple_SetItem(tuple, 0, PyLong_FromLong(path[i].x));
        PyTuple_SetItem(tuple, 1, PyLong_FromLong(path[i].y));
        PyList_SetItem(output, i, tuple);
    }

    free(path);
    return output;
}

// Define the methods in the module
static PyMethodDef graph_methods[] = {
    {"simulated_annealing", graph_simulated_annealing, METH_VARARGS, "Simulated annealing algorithm."},
    {NULL, NULL, 0, NULL}
};

// Define the module's initialization function
static struct PyModuleDef graph_module = {
    PyModuleDef_HEAD_INIT,
    "graph",
    "Custom graph module.",
    -1,
    graph_methods
};

PyMODINIT_FUNC PyInit_graph(void)
{
    // Create the module object
    PyObject* module = PyModule_Create(&graph_module);

    return module;
}