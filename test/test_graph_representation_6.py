import pytest

@pytest.fixture
def graph():
    from student_graph import VersatileDigraph
    return VersatileDigraph()

def test_add_edge_with_new_nodes(graph):
    graph.add_edge("A", "B", start_node_value=10, end_node_value=20, edge_name="edge1", edge_value=5)
    assert graph.get_node_value("A") == 10
    assert graph.get_node_value("B") == 20
    assert graph.get_edge_wt("A", "B") == 5
