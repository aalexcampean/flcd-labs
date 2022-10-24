import copy

from Constants import INITIAL_CAPACITY
from Node import Node


class HashTable:
    def __init__(self):
        self.capacity = INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        hashsum = 0

        # For each character in the key
        for character in key:
            hashsum += ord(character)

        return hashsum % self.capacity

    def rehash(self):
        self.capacity *= 2

        new_buckets = [None] * self.capacity
        for index in range(self.size):
            node = self.buckets[index]
            while node is not None:
                # Compute hash value of key
                new_index = self.hash(node.key)

                # Go to the node corresponding to the hash
                new_node = new_buckets[new_index]

                # If bucket is empty
                if new_node is None:
                    # Create node, add it, return
                    new_buckets[new_index] = Node(node.key, node.value)
                else:
                    # Otherwise, we have a collision
                    # Iterate to the end of the linked list at provided index
                    new_prev = new_node
                    while node is not None:
                        new_prev = new_node
                        new_node = new_node.next

                    # Add a new node at the end of the list with provided key/value
                    new_prev.next = Node(node.key, node.value)

                node = node.next

        self.buckets = new_buckets

    def insert(self, key, value):
        # Compute hash value of key
        index = self.hash(key)

        # Go to the node corresponding to the hash
        node = self.buckets[index]

        # If bucket is empty
        if node is None:
            # Create node, add it, return
            self.buckets[index] = Node(key, value)
            # Increment the size
            self.size += 1
        else:
            # Otherwise, we have a collision
            # Iterate to the end of the linked list at provided index
            prev = node
            while node is not None:
                # If the key already exists we don't do anything
                if prev.key == key:
                    return
                prev = node
                node = node.next

            # Add a new node at the end of the list with provided key/value
            prev.next = Node(key, value)

            # Increment the size
            self.size += 1

        if self.size / self.capacity >= 0.7:
            self.rehash()

    def remove(self, key):
        # Compute hash value of key
        index = self.hash(key)
        node = self.buckets[index]
        prev = None

        # Go to the first node in list at the computed index
        while node is not None and node.key != key:
            prev = node
            node = node.next

        # Now the node is either the requested key/value pair or None
        if node is None:
            # The given key was not found
            return None
        else:
            # The given key was found
            self.size -= 1
            result = node.value

            # Delete this element from the linked list
            if prev is None:
                # The element is the head of the linked list
                self.buckets[index] = None
            else:
                # The element is inside the linked list
                prev.next = node.next

            # Return the deleted value
            return result

    def __contains__(self, key):
        # Compute hash value of key
        index = self.hash(key)

        # Go to the first node in list at the computed index
        node = self.buckets[index]

        # Parse the linked list at this node
        while node is not None and node.key != key:
            node = node.next

        # Now the node is either the requested key/value pair or None
        return node is not None

    def find(self, key):
        # Compute hash value of key
        index = self.hash(key)

        # Go to the first node in list at the computed index
        node = self.buckets[index]

        # Parse the linked list at this node
        while node is not None and node.key != key:
            node = node.next

        # Now the node is either the requested key/value pair or None
        if node is None:
            # Not found
            return None
        else:
            # Found - return the data value
            return node.value
