from metaflow import FlowSpec, step


class BasicExample(FlowSpec):

    @step
    def start(self):
        self.val = 2
        self.next(self.square, self.cube)

    @step
    def square(self):
        self.val_squared = self.val**2
        self.next(self.join)

    @step
    def cube(self):
        self.val_cubed = self.val**3
        self.next(self.join)

    @step
    def join(self, inputs):
        self.total = inputs.square.val_squared + inputs.cube.val_cubed
        self.next(self.end)

    @step
    def end(self):
        print(f"Sum of squares and cubes: {self.total}")


if __name__ == "__main__":
    BasicExample()
