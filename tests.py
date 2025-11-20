import unittest

# Функции для тестирования
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, x):
        self.result += x
        return self.result
    
    def reset(self):
        self.result = 0

# Тестовый класс
class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        """Выполняется перед каждым тестом"""
        self.calc = Calculator()
    
    def tearDown(self):
        """Выполняется после каждого теста"""
        self.calc.reset()
    
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(0, 0), 0)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)
    
    def test_subtract_numbers(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
    
    def test_divide_numbers(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(1, 3), 0.333333, places=6)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)
    
    def test_calculator_add(self):
        self.assertEqual(self.calc.add(5), 5)
        self.assertEqual(self.calc.add(3), 8)
    
    def test_calculator_reset(self):
        self.calc.add(10)
        self.calc.reset()
        self.assertEqual(self.calc.result, 0)

# Запуск тестов
if __name__ == '__main__':
    unittest.main()
