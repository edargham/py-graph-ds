import numpy as np

class DisjointSet():
    def __init__(self, vertices: np.ndarray):
        if len(vertices.shape) != 1:
            raise Exception('Only 1-D vectors are acceptable for the vertex collection.')
        # endif
        self.vertices = vertices
        self.parent_idxs = np.arange(self.vertices.shape[0])
        self.rank = np.ones_like(self.parent_idxs)
    # endinit

    def find_set(self, idx_vtx: int) -> int:
        if self.parent_idxs[idx_vtx] == idx_vtx:
            return idx_vtx
        # endif

        self.parent_idxs[idx_vtx] = self.find_set(self.parent_idxs[idx_vtx])
        return self.parent_idxs[idx_vtx]                            
    # endmethod

    def union_set(self, idx_u: int, idx_v: int) -> None:
        p_idx_u = self.find_set(idx_u)
        p_idx_v = self.find_set(idx_v)

        if p_idx_u == p_idx_v:
            return
        # endif

        if self.rank[p_idx_u] < self.rank[p_idx_v]:
            self.parent_idxs[p_idx_u] = p_idx_v
        # endif
        elif self.rank[p_idx_u] > self.rank[p_idx_v]:
            self.parent_idxs[p_idx_v] = p_idx_u
        # endelif
        else:
            self.parent_idxs[p_idx_v] = p_idx_u
            self.rank[p_idx_u] += 1
    # endmethod

    def display(self) -> None:
        # Create a dictionary to hold the disjoint sets
        disjoint_sets = {}
        
        # Iterate over all vertices to populate the dictionary
        for i, vertex in enumerate(self.vertices):
            root = self.find_set(i)
            if root not in disjoint_sets:
                disjoint_sets[root] = []
            # endif
            disjoint_sets[root].append(vertex)
        # endfor

        # Print the disjoint sets
        print("Disjoint Sets:")
        for root, members in disjoint_sets.items():
            print(f"Set rooted at {self.vertices[root]}: {members}")
        # endfor
    # endmethod
# endclass