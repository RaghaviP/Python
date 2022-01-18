class TopTwenty:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.num <= 10:
            val = self.num
            self.num += 1

            return val

        else:
            raise StopIteration

values = TopTwenty()

for A in values:
    print(A)

