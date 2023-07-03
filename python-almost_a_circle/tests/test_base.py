import unittest
from unittest.mock import patch
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_create_square(self):
        # Test creating a square instance
        square = Square(5, 1, 2, 10)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)
        self.assertEqual(square.id, 10)

    def test_area(self):
        # Test calculating the area of a square
        square = Square(5)
        self.assertEqual(square.area(), 25)


    def test_display(self):
        square = Square(3, 0, 0)
        expected_output = "###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as output:
            square.display()
            self.assertEqual(output.getvalue(), expected_output)


    def test_display(self):
        square = Square(3, 1, 1)
        expected_output = "\n ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as output:
            square.display()
            self.assertEqual(output.getvalue(), expected_output)

    def test_update(self):
        # Test updating a square's attributes
        square = Square(5)
        square.update(10, 3, 2, 1)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 1)

    def test_to_dictionary(self):
        # Test converting a square to a dictionary
        square = Square(5, 1, 2, 10)
        expected_dict = {
            'id': 10,
            'x': 1,
            'size': 5,
            'y': 2
        }
        self.assertEqual(square.to_dictionary(), expected_dict)

    def test_zero_size(self):
        with self.assertRaises(ValueError):
            square = Square(0)

    def test_negative_size(self):
        with self.assertRaises(ValueError):
            square = Square(-1)

    def test_negative_position(self):
        with self.assertRaises(ValueError):
            square = Square(2, -1, -2)

    def test_update_with_invalid_arguments(self):
        square = Square(4)
        with self.assertRaises(TypeError):
            square.update("invalid")
        with self.assertRaises(TypeError):
            square.update(5, "invalid")
        with self.assertRaises(TypeError):
            square.update(5, 3, "invalid")
        with self.assertRaises(TypeError):
            square.update(5, 3, 2, "invalid")

    def test_to_dictionary(self):
        square = Square(3, 4, 5, 6)
        dictionary = square.to_dictionary()
        self.assertEqual(dictionary, {'id': 6, 'x': 4, 'size': 3, 'y': 5})

    def test_create(self):
        dictionary = {'id': 1, 'x': 2, 'size': 3, 'y': 4}
        square = Square.create(**dictionary)
        self.assertIsInstance(square, Square)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 4)
        self.assertEqual(square.size, 3)


if __name__ == '__main__':
    unittest.main()