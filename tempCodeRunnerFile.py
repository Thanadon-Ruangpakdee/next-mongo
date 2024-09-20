class TestReadGraphFromFile(unittest.TestCase):
    def test_read_graph_from_file(self):
        test_filename = 'test_graph.txt'
        with open(test_filename, 'w') as f:
            f.write("0 1 10\n")
            f.write("0 2 6\n")
            f.write("0 3 5\n")
            f.write("1 3