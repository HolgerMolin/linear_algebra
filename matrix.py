from __future__ import annotations
from random import normalvariate
from random import uniform

class MatrixShapeException(Exception):
    def __init__(self, message = "Matrix shape mismatch") -> None:
        self.message = message
        super().__init__()

def fill_matrix(shape: tuple[int], value: int | float):
    if not isinstance(shape, tuple):
        raise TypeError("Requires tuple")
    if len(shape) != 2:
        raise ValueError("Shape tuple should be length 2")
    output_matrix = []
    for _ in range(shape[1]):
        output_column = []
        for __ in range(shape[0]):
            output_column.append(value)
        output_matrix.append(output_column)
    return Matrix(output_matrix)

def rand_matrix(shape: tuple[int], random_type: str = "uniform" or "normal", min: float = 0, max: float = 1, mean: float = 0, stddev: float = 1):
    if not isinstance(shape, tuple):
        raise TypeError("Requires tuple")
    if len(shape) != 2:
        raise ValueError("Shape tuple should be length 2")
    if random_type == 'unform':
        output_matrix = []
        for _ in range(shape[1]):
            output_column = []
            for __ in range(shape[0]):
                output_column.append(normalvariate(mean, stddev))
            output_matrix.append(output_column)
        return Matrix(output_matrix)
    elif random_type == 'normal':
        output_matrix = []
        for _ in range(shape[1]):
            output_column = []
            for __ in range(shape[0]):
                output_column.append(uniform(min, max))
            output_matrix.append(output_column)
        return Matrix(output_matrix)
    else:
        raise ValueError(f"Unsupported random_type: {random_type}")


def hadamard(A: Matrix, B:Matrix):
    if A.shape != B.shape:
        raise MatrixShapeException()
    output_matrix = []
    for column_index in range(len(A.elements)):
        output_column = []
        for element_index in range(len(A.elements[column_index])):
            output_column.append(A[column_index, element_index] * B[column_index, element_index])
        output_matrix.append(output_column)
    return Matrix(output_matrix)

class Matrix:
    def __init__(self, elements: list[list[float]] | list[list[int]]):
        self.elements = elements
        self.shape = (len(elements), len(elements[0]))

    def __add__(self, matrix: Matrix):
        if matrix.shape != self.shape:
            raise MatrixShapeException(f"Cannot add matrices of shape {self.shape} and {matrix.shape}")
        output_matrix = []
        for column_index, column in enumerate(matrix.elements):
            output_column = []
            for element_index, element in enumerate(column):
                output_column.append(element + self.elements[column_index][element_index])
            output_matrix.append(output_column)
        return Matrix(output_matrix)

    def __mul__(self, factor: float | int | Matrix):
        if isinstance(factor, (float, int)):
            output_matrix = []
            for column in self.elements:
                output_column = []
                for element in column:
                    output_column.append(factor * element)
                output_matrix.append(output_column)
            return Matrix(output_matrix)

        if isinstance(factor, Matrix):
            if self.shape[1] != factor.shape[0]:
                raise MatrixShapeException("Matrix shapes are not compatible for multiplication")
            output_matrix = []
            for column_index in range(self.shape[0]):
                output_column = []
                for element_index in range(factor.shape[1]):
                    output_column.append(sum(self[column_index, i] * factor[i, element_index] for i in range(self.shape[1])))
                output_matrix.append(output_column)
            return Matrix(output_matrix)

    def __rmul__(self, factor: float | int):
        output_matrix = []
        for column in self.elements:
            output_column = []
            for element in column:
                output_column.append(factor * element)
            output_matrix.append(output_column)
        return Matrix(output_matrix)
    
    def __getitem__(self, index: tuple(int, int)):
        return self.elements[index[0]][index[1]]
    
    def __str__(self):
        pass

    def transpose(self):
        output_matrix = []
        for column_index in range(self.shape[1]):
            output_column = []
            for element_index in range(self.shape[0]):
                output_column.append(self[element_index, column_index])
            output_matrix.append(output_column)
        return Matrix(output_matrix)

    def trace(self):
        if self.shape[0] != self.shape[1]:
            raise MatrixShapeException("Matrix is not square")
        return sum(self.elements[i][i] for i in range(self.shape[0]))
    
    def map(self, function):
        output_matrix = []
        for column in self.elements:
            output_column = []
            for element in column:
                output_column.append(function(element))
            output_matrix.append(output_column)
        return Matrix(output_matrix)

    
        
            
