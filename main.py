import numpy as np

from graph.disjoint_set import DisjointSet

def test_disjoint_set():
    vertices = np.array([0, 1, 2, 3, 4])
    ds = DisjointSet(vertices)
    
    # Test find_set
    assert ds.find_set(0) == 0
    assert ds.find_set(1) == 1

    ds.display()
    
    # Test union_set
    ds.union_set(0, 1)
    assert ds.find_set(0) == ds.find_set(1)
    
    ds.union_set(2, 3)
    assert ds.find_set(2) == ds.find_set(3)
    
    ds.union_set(1, 3)
    assert ds.find_set(0) == ds.find_set(2)
    assert ds.find_set(1) == ds.find_set(3)
    
    print("All tests passed.")
    ds.display()
# endfunc

if __name__ == '__main__':
    test_disjoint_set()
# endmain
