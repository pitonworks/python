"""
Snake Sınıfı - Linked List kullanarak yılanı temsil eder
Yılan, bağlı liste (linked list) veri yapısı kullanılarak implement edilmiştir.
Her düğüm yılanın bir segmentini temsil eder.
"""
from node import Node

class Snake:
    def __init__(self, start_row, start_col):
        """
        Snake constructor - Creates snake at starting position
        
        Args:
            start_row (int): Snake's starting row position
            start_col (int): Snake's starting column position
        """
        first = Node(start_row, start_col)  # Create first node
        self.head = first  # Head node (snake's head)
        self.tail = first  # Tail node (same as head at start)
        self.grow_next_move = False  # Flag to grow on next move

    def add_head(self, row, col):
        """
        Adds new node to the head of the snake (used when snake moves)
        
        Args:
            row (int): New head node's row position
            col (int): New head node's column position
        """
        new_head = Node(row, col)  # Create new head node
        new_head.next = self.head  # New head points to old head
        self.head = new_head  # Set new node as head

    def remove_tail(self):
        """
        Removes tail of the snake (used when snake moves)
        If grow_next_move is True, tail is not removed (snake grows)
        """
        # If snake will grow, do not remove tail
        if self.grow_next_move:
            self.grow_next_move = False
            return

        # Traverse linked list to find tail
        current = self.head
        while current.next != self.tail:
            current = current.next
        # Remove tail from list
        current.next = None
        self.tail = current  # Set new tail

    def move(self, new_row, new_col):
        """
        Moves snake to new position
        Adds new node to head and removes tail
        Adds new node to head and removes tail
        
        Args:
            new_row (int): New head position's row
            new_col (int): New head position's column
        """
        self.add_head(new_row, new_col)  # Add new head
        self.remove_tail()  # Remove old tail

    def grow(self):
        """
        Allows snake to grow on next move
        This flag is checked in remove_tail() method
        """
        self.grow_next_move = True

    def collision_with_self(self, row, col):
        """
        Checks if given position collides with snake's body
        
        Args:
            row (int): Row position to check
            col (int): Column position to check
            
        Returns:
            bool: True if position is on snake's body, False otherwise
        """
        current = self.head
        # Check all nodes
        while current is not None:
            if current.row == row and current.col == col:
                return True  # Collision found
            current = current.next
        return False  # No collision

    def get_positions(self):
        """
        Returns all positions of the snake's segments as a list
        
        Returns:
            list: List of (row, column) tuples
        """
        coords = []
        current = self.head
        # Traverse all nodes and collect positions
        while current is not None:
            coords.append((current.row, current.col))
            current = current.next
        return coords

    def get_length(self):
        """
        Returns length of the snake (number of segments)
        
        Returns:
            int: Length of the snake
        """
        return len(self.get_positions())
