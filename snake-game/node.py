"""
Node Class - Node for Linked List
Yılan oyununda yılanın her bir segmentini temsil eder.
Her düğüm bir konum (satır, sütun) ve bir sonraki düğüme işaret eder.
"""
class Node:
    def __init__(self, row, col):
        """
        Node constructor
        
        Args:
            row (int): Node's row position in the grid
            col (int): Node's column position in the grid
        """
        self.row = row  # Node's row coordinate
        self.col = col  # Node's column coordinate
        self.next = None  # Pointer to the next node
