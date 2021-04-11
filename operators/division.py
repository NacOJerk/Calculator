from operators import operator


@operator.Operator.register_operator
class Division(operator.Operator):
    """
        The addition operator, this operator allows us to divide one number in the other
    """
    def __init__(self):
        super().__init__('+')

    def act(self, x: int, y: int) -> int:
        return x // y