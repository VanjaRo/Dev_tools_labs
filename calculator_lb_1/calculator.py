"""@package docstring
Documentation for this module.
 
More details.
"""


class Calculator:

    def __init__(self):
        """Class initializer.
        """
        self.last_result = 0

    def command_parser(self, command, a, b):
        """Command selctor

        Args:
            command (str): describes a command to operate
            a (float): 1st oprand
            b (float): 2nd oprand
        Returns:
            float: result of the operation if the command was valid
            None: if the command was invalid

        """

        if command == '+':
            return self.add(a, b)
        elif command == '-':
            return self.sub(a, b)
        elif command == '*':
            return self.mult(a, b)
        elif command == '/':
            return self.div(a, b)
        else:
            raise ValueError

    def add(self, a, b):
        """Summation

        Args:
            a (float): 1st oprand
            b (float): 2nd oprand

        Returns:
            float: summ of the operands
        """
        self.last_result = a + b
        return self.last_result

    def sub(self, a, b):
        """Difference

        Args:
            a (float): 1st oprand
            b (float): 2nd oprand

        Returns:
            float: difference between two operands
        """
        self.last_result = a - b
        return self.last_result

    def mult(self, a, b):
        """Multiplication

        Args:
            a (float): 1st oprand
            b (float): 2nd oprand

        Returns:
            float: result of multiplication of two operands
        """
        self.last_result = a * b
        return self.last_result

    def div(self, a, b):
        """Division

        Args:
            a (float): 1st oprand
            b (float): 2nd oprand

        Raises:
            ValueError: raises whenever the "b" operand is zero

        Returns:
            float: result of the devision of two operands
        """
        if b == 0:
            raise ValueError
        self.last_result = a / b
        return self.last_result

    def start(self):
        """Initializing user comand line interaction

        Returns:
            int: returns 0 whenever user decides to exit the calculator
        """
        loop = True
        while loop:
            a = 0
            b = 0
            print('If you\'d like to exit input "ext"')
            while True:
                numb = input(
                    'Type operands A and B, both must be numbers: ')
                if numb == 'ext':
                    return 0
                try:
                    a, b = map(float, numb.split())
                except:
                    print('Both operands should be numbers!')
                    continue
                else:
                    break
            while True:
                command = input('Operation type: +, -, *, /: ')
                if command == '/' and b == 0:
                    print('This operation is not suitable for these operands!')
                    continue
                elif command == 'ext':
                    return 0
                elif command == '+' or command == '-' or command == '*' or command == '/':
                    break
                else:
                    print('Enter correct operation!')
                    continue

            print(self.command_parser(command, a, b))

            inpt = input('Input "continue" if you\'d like to continue: ')
            if inpt == 'continue':
                continue
            return 0

    def get_last_res(self):
        """Getting last result

        Returns:
            float: last result
        """
        return self.last_result


if __name__ == '__main__':
    calc = Calculator()
    calc.start()
