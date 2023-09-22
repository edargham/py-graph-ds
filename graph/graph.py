import numpy as np

from vertex import Vertex
from edge_list import EdgeList
from mst_list import MstList

from types import *

class Graph():
    def __init__(self, vertices: np.ndarray, adj_mat: np.ndarray=None, directed: bool=False):
        self.vertices: np.ndarray = vertices
        self.directed: np.ndarray = directed
        self.adj_mat: np.ndarray = adj_mat

        if (self.adj_mat is not None):
            if (
                self.adj_mat.shape[0] != self.adj_mat.shape[1] 
                and self.adj_mat.shape[0] != self.vertices.shape[0] 
                and len(self.vertices.shape) != 1
            ):
                raise Exception('Mismatch between edge dims and/or vertex dims.')
            # endif

            if not directed:
                for i in range(self.adj_mat.shape[0]):
                    for j in range(i+1, self.adj_mat.shape[1]):
                        if self.adj_mat[i][j] != self.adj_mat[j][i]:
                            raise Exception('Expected undirected graph, got directed graph.')
                        # endif
                    # endfor
                # endfor
            # endif
        # endif
        else:
            self.adj_mat = np.zeros(self.vertices.shape)
        # endelse

        for i in range(self.vertices.shape[0]):
            self.vertices[i].set_order(i)
        # endfor
    # endinit

    # def _bfs_get_neigbors()

    def _find_neighbors(self, v_idx: int) -> np.ndarray:
        nbs: list[int] = []

        if (v_idx > self.adj_mat.shape[0]):
            raise Exception('Index specified exeeds graph width')
        # endif

        for i in range(self.adj_mat[v_idx].shape[0]):
            if self.adj_mat[i] != 0:
                nbs.append(i)
            # endif
        # endfor

        return np.array(nbs)
    # endmethod

    def _is_neighbor(self, fringe: np.ndarray) -> int:
        for i in range(fringe.size):
            if fringe[i] != 0 and self.vertices[i].get_mark() == 0:
                return i
            # endif
        # endfor
        return None
    # endmethod

    def bfs(self, initial_node_idx:int=0, callback=None):
        bfs_queue = []
        bfs_queue.append(initial_node_idx)

        if (
            callback is not None 
            and type(out:=callback(self.vertices[initial_node_idx])) != NoneType
        ):
            self.vertices[initial_node_idx].set_mark(1)
            return out
        # endif

        self.vertices[initial_node_idx].set_mark(1)

        while bfs_queue:
            idx: int = bfs_queue.pop(0)
            neighs: list[int] = self._find_neighbors(idx)

            for n in neighs:
                if self.vertices[n].get_mark() == 0:
                    bfs_queue.append(n)
                    
                    if (
                        callback is not None 
                        and type(out:=callback(self.vertices[n])) != NoneType
                    ):
                        self.vertices[n].set_mark(1)
                        return self.vertices[n], out
                    # endif

                    self.vertices[n].set_mark(1)
                # endif
            # endfor
        # endwhile

        return None
    # endmethod

    def bfs_all(self, callback=None):
        for vtx in self.vertices:
            vtx.set_mark(0)
        # endfor

        last = None

        for i in range(self.vertices.shape[0]):
            last = self.bfs(i, callback)
        # endfor

        return last
    # endmethod

    def dfs(self, initial_node_idx=0, pre_callback=None, post_callback=None):
        dfs_stack=[]
        dfs_stack.append(initial_node_idx)
        
        self.vertices[initial_node_idx].set_mark(1)

        while dfs_stack:
            current_idx = dfs_stack[0]
            next_idx = self._is_neighbor(self.adj_mat[current_idx])

            if next_idx is not None:
                self.vertices[next_idx].set_mark(1)
                dfs_stack.insert(0, next_idx)

                if (
                    pre_callback is not None 
                    and type(pre_out:=pre_callback(self.vertices[next_idx])) != NoneType
                ):
                    return self.vertices[next_idx], pre_out
                # endif
            # endif
            else:
                popped_idx = dfs_stack.pop(0)
                if (
                    post_callback is not None 
                    and type(post_out:=post_callback(self.vertices[popped_idx])) != NoneType
                ):
                    return self.vertices[popped_idx], post_out
                # endif
            # endelse
        # endwhile
    # endmethod

    def dfs_all(self, pre_callback=None, post_callback=None):
        for vtx in self.vertices:
            vtx.set_mark(0)
        # endfor

        last = None

        for i in range(self.vertices.shape[0]):
            last = self.dfs(i, pre_callback, post_callback)
        # endfor

        return last
    # endmethod

    def ucs(self):
        return
    # endmethod

    def _find_set(self, parent, u):
        return
    # endmethod

    def _union_set(self, parent, rank, u):
        return
    # endmethod

    def dsu(self):
        return
    # endmethod
# endclass