class EdgeList():
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight
    # endinit

    def get_u(self):
        return self.u
    # endmethod

    def set_u(self, u):
        self.u = u
    # endmethod

    def get_v(self):
        return self.v
    # endmethod

    def set_v(self, v):
        self.v = v
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