class CountFromBy:
    def __init__(self, v: int=0, i: int=1) -> None:
        self.val = v
        self.incur = i
    def increase(self) -> None:
        self.val += self.incur
    def __repr__(self) -> str:
        return str(self.val)
