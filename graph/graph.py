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
            if self.adj_mat.shape[0] != self.adj_mat.shape[1] and self.adj_mat.shape[0] != self.vertices.shape[0] and len(self.vertices.shape) != 1:
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

    def bfs(self, initial_node_idx:int=0, callback=None):
        # Initialize queue and set enqueue the initial node's index.
        bfs_queue = []
        bfs_queue.append(initial_node_idx)

        if (type(out:=callback(self.vertices[initial_node_idx])) != NoneType):
            self.vertices[initial_node_idx].set_mark(1)
            return out
        # endif

        self.vertices[initial_node_idx].set_mark(1)

        while bfs_queue != 0:
            idx: int = bfs_queue.pop(0)


        # endwhile

        return
    # endmethod

    def bfs_all(self, callback=None):
        return
    # endmethod

    def dfs(self, callback=None):
        return
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