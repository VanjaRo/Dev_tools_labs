import unittest
import calculator as c


class TestCases(unittest.TestCase):
    def test_pars_command(self):
        calc = c.Calculator()
        self.assertEqual(6, calc.command_parser('+', 4, 2))
        self.assertEqual(2, calc.command_parser('-', 4, 2))
        self.assertEqual(8, calc.command_parser('*', 4, 2))
        self.assertEqual(2, calc.command_parser('/', 4, 2))
        self.assertRaises(ValueError, calc.command_parser, 'ext', 4, 2)

    def test_summ(self):
        calc = c.Calculator()
        self.assertEqual(3, calc.add(1, 2))
        self.assertEqual(4, calc.add(4, 0))
        self.assertEqual(3, calc.add(4, -1))

    def test_sub(self):
        calc = c.Calculator()
        self.assertEqual(-1, calc.sub(1, 2))
        self.assertEqual(4, calc.sub(4, 0))
        self.assertEqual(5, calc.sub(4, -1))

    def test_mult(self):
        calc = c.Calculator()
        self.assertEqual(2, calc.mult(1, 2))
        self.assertEqual(0, calc.mult(4, 0))
        self.assertEqual(-4, calc.mult(4, -1))
        self.assertEqual(4, calc.mult(-4, -1))
        self.assertEqual(8, calc.mult(4, 2))

    def test_div(self):
        calc = c.Calculator()
        self.assertEqual(0.5, calc.div(1, 2))
        self.assertRaises(ValueError, calc.div, 4, 0)
        self.assertEqual(-4, calc.div(4, -1))
        self.assertEqual(4, calc.div(-4, -1))
        self.assertEqual(4, calc.div(8, 2))


if __name__ == '__main__':
    unittest.main()
