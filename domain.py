class Domain:
    """Represents a numerical domain with start, end, and step."""

    def __init__(self, start=0.0, end=1.0, step=1.0):
        start = float(start)
        end = float(end)
        step = float(step)
        if step == 0:
            raise ValueError("step cannot be zero")
        if step > 0 and end < start:
            raise ValueError("end must be >= start for positive step")
        if step < 0 and end > start:
            raise ValueError("end must be <= start for negative step")
        self.start = start
        self.end = end
        self.step = step

    def values(self):
        if self.start == self.end:
            return [self.start]
        count = int((self.end - self.start) / self.step) + 1
        return [self.start + i * self.step for i in range(count)]
