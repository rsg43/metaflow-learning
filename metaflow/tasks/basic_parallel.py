from metaflow import FlowSpec, step


class BasicExample(FlowSpec):

    @step
    def start(self):
        self.vals = [1, 2, 3, 4, 5]
        self.next(self.cube, foreach="vals")

    @step
    def cube(self):
        self.val_cubed = self.input**3
        self.next(self.join)

    @step
    def join(self, inputs):
        self.total = [input.val_cubed for input in inputs]
        self.next(self.end)

    @step
    def end(self):
        print(f"All calculated cubes: {self.total}")


if __name__ == "__main__":
    BasicExample()
