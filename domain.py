class Domain:
    """Represents a numerical domain with start, end, and step."""

    def __init__(self, start=0.0, end=1.0, step=1.0):
        start = float(start)
        end = float(end)
        step = float(step)
        if step == 0:
            raise ValueError("step cannot be zero")
        if (end - start) * step <= 0:
            raise ValueError("end must be greater than start for positive step")
        self.start = start
        self.end = end
        self.step = step

    def values(self):
        count = int((self.end - self.start) / self.step) + 1
        return [self.start + i * self.step for i in range(count)]
