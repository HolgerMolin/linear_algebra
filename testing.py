from matrix import Matrix 
import unittest
import torch
from random import uniform
import matrix

def tensor_to_matrix(tensor: torch.Tensor) -> Matrix:
    if tensor.dim() != 2:
        raise ValueError("Input tensor must be a 2D tensor")

    elements = tensor.tolist()
    return Matrix(elements)

NUM_SAMPLES = 10

class MatrixTests(unittest.TestCase):
    def test_matrix_trace(self):
        shapes = [(i, i) for i in range(1,10)]
        passed = True
        for shape in shapes:
            for _ in range(NUM_SAMPLES):
                A_torch = torch.rand(shape)
                A_mat = tensor_to_matrix(A_torch)
                torch_trace = A_torch.trace().item()
                matrix_trace = A_mat.trace()
                self.assertAlmostEqual(torch_trace, matrix_trace, delta=1e-6)

        print("Passed matrix trace test")

    def test_matrix_addition(self):
        shapes = [(i, j) for j in range(1, 10) for i in range(1, 10)]
        for shape in shapes:
            for _ in range(NUM_SAMPLES):
                A_torch = torch.rand(shape)
                B_torch = torch.rand(shape)
                A_mat = tensor_to_matrix(A_torch)
                B_mat = tensor_to_matrix(B_torch)

                C_torch = A_torch + B_torch
                C_mat = A_mat + B_mat
                for i in range(shape[0]):
                    for j in range(shape[1]):
                        self.assertAlmostEqual(C_torch[i, j].item(), C_mat[i, j], delta=1e-6)

        print("Passed matrix addition test")
    def test_matrix_scalar_multiplication(self):
        shapes = [(i, j) for j in range(1, 10) for i in range(1, 10)]
        for shape in shapes:
            for _ in range(NUM_SAMPLES):
                A_torch = torch.rand(shape)
                A_mat = tensor_to_matrix(A_torch)
                alpha = uniform(-100.0, 100.0)

                A_torch = alpha * A_torch
                A_mat = alpha * A_mat

                for i in range(shape[0]):
                    for j in range(shape[1]):
                        self.assertAlmostEqual(A_torch[i, j].item(), A_mat[i, j], delta=1e-5)
        print("Passed matrix scalar multiplication test")

    def test_matrix_multiplication(self):
        shapes = [(i, j, k) for i in range(1, 10) for j in range(1, 10) for k in range(1, 10)]
        for shape in shapes:
            for _ in range(NUM_SAMPLES):
                A_torch = torch.rand((shape[0], shape[1]))
                A_mat = tensor_to_matrix(A_torch)
                B_torch = torch.rand((shape[1], shape[2]))
                B_mat = tensor_to_matrix(B_torch)
                C_torch = torch.matmul(A_torch, B_torch)
                C_mat = A_mat * B_mat
                for i in range(C_mat.shape[0]):
                    for j in range(C_mat.shape[1]):
                        self.assertAlmostEqual(C_torch[i, j].item(), C_mat[i, j], delta=1e-6)
        print("Passed matrix multiplication test")

    def test_hadamard(self):
        shapes = [(i, j) for j in range(1, 10) for i in range(1, 10)]
        for shape in shapes:
            for _ in range(NUM_SAMPLES):
                A_torch = torch.rand(shape)
                B_torch = torch.rand(shape)
                A_mat = tensor_to_matrix(A_torch)
                B_mat = tensor_to_matrix(B_torch)

                C_torch = A_torch * B_torch
                C_mat = matrix.hadamard(A_mat, B_mat)
                for i in range(shape[0]):
                    for j in range(shape[1]):
                        self.assertAlmostEqual(C_torch[i, j].item(), C_mat[i, j], delta=1e-6)
        print("Passed hadamard test")


test = MatrixTests()
test.test_matrix_trace()
test.test_matrix_addition()
test.test_matrix_scalar_multiplication()
test.test_matrix_multiplication()
test.test_hadamard()
