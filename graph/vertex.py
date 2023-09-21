import random

class Vertex():
    def __init__(self, datum, mark, idx):
        self.datum = datum
        self.mark = mark,
        self.idx = idx
        self.order = random.randint(0, 256)
    # endinit

    def get_datum(self):
        return self.datum
    # endmethod

    def set_datum(self, datum):
        self.datum = datum
    # endmethod

    def get_mark(self):
        return self.mark
    # endmethod

    def set_mark(self, mark):
        self.mark = mark
    # endmethod

    def get_idx(self):
        return self.idx
    # endmethod

    def set_idx(self, idx):
        self.idx = idx
    # endmethod

    def get_order(self):
        return self.order
    # endmethod

    def set_order(self, order):
        self.order = order
    # endmethod
# endclass