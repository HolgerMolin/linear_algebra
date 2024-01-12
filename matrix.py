from __future__ import annotations

class MatrixShapeException(Exception):
    def __init__(self, message = "Matrix shape mismatch") -> None:
        self.message = message
        super().__init__()

class Matrix:
    def __init__(self, elements: list[list[float]] | list[list[int]]) -> None:
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
        return output_matrix

    def __mul__(self, factor: float | int | Matrix):
        if isinstance(factor, (float, int)):
            output_matrix = []
            for column in self.elements:
                output_column = []
                for element in column:
                    output_column.append(factor * element)
                output_matrix.append(output_column)
            return output_matrix

        if isinstance(factor, Matrix):
            if self.shape[1] != factor.shape[0]:
                raise MatrixShapeException("Matrix shapes are not compatible for multiplication")
            output_matrix = []
            for column_index in range(self.shape[0]):
                output_column = []
                for element_index in range(factor.shape[1]):
                    output_column.append(sum())

    def __rmul__(self, factor: float | int):
        output_matrix = []
        for column in self.elements:
            output_column = []
            for element in column:
                output_column.append(factor * element)
            output_matrix.append(output_column)
        return output_matrix

    def transpose(self):
        pass

    def trace(self):
        if self.shape[0] != self.shape[1]:
            raise MatrixShapeException("Matrix is not square")
        return sum(self.elements[i][i] for i in range(self.shape[0]))
        
            
