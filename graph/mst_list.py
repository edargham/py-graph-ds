class MstList:
    def __init__(self, mst, weight):
        self.mst = mst,
        self.weight = weight
    # endinit

    def get_mst(self):
        return self.mst
    # endmethod

    def set_mst(self, mst):
        self.mst = mst
    # endmethod

    def get_weight(self):
        return self.weight
    # endmethod

    def set_weight(self, weight):
        self.weight = weight
    # endmethod
# endclass