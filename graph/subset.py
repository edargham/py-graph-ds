class Subset():
    def __init__(self, parent_idx: int, vrtx_idx: int, weight: float | int):
        self.parent_idx = parent_idx
        self.vrtx_idx = vrtx_idx
        self.weight = weight
    # endinit

    def get_parent_idx(self):
        return self.parent_idx
    # endmethod

    def set_parent_idx(self, parent_idx):
        self.parent_idx = parent_idx
    # endmethod

    def get_vrtx_idx(self):
        return self.vrtx_idx
    # endmethod

    def set_vrtx_idx(self, vrtx_idx):
        self.vrtx_idx = vrtx_idx
    # endmethod

    def get_weight(self):
        return self.weight
    # endmethod

    def set_weight(self, weight):
        self.weight = weight
    # endmethod

    def __gt__(self, el):
        return self.weight > el.weight
    # endoverload

    def __gte__(self, el):
        return self.weight >= el.weight
    # endoverload

    def __lt__(self, el):
        return self.weight < el.weight
    # endoverload

    def __lte___(self, el):
        return self.weight <= el.weight
    # endoverload

    def __eq__(self, el):
        return self.weight == el.weight
    # endoverload

    def __ne__(self, el):
        return self.weight != el.weight
    # endoverload
# endclass