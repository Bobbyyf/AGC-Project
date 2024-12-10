class Node:
    def __init__(self, expression, result):
        self.expression = expression
        self.result = result
        self.next = None

class CalculatorHistory:
    def __init__(self):
        self.head = None
    
    def add_calculation(self, expression, result):
        new_node = Node(expression, result)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def display_history(self):
        if not self.head:
            print("\nNO CLACULATIONS IN HISTORY")
            return
        
        print("\nCALCULATION HISTORY:")
        current = self.head
        while current:
            print(f"{current.expression} = {current.result}")
            current = current.next

def calculate(num1, num2, op):
    try:
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            if num2 == 0:
                raise ValueError("DONT DIVIDE BY 0")
            return num1 / num2
        else:
            raise ("INVALID OPERATER")
    except Exception as e:
        raise ValueError(str(e))

