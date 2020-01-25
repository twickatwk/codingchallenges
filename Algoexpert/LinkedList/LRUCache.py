
# Doubly Linked List Node
class ListNode:
	def __init__(self, key, value):
		self.prev = None
		self.next = None
		self.key = key
		self.value = value
	def removeBindings(self):
		if self.prev is not None:
			self.prev.next = self.next
		if self.next is not None:
			self.next.prev = self.prev

# Doubly Linked List Class
class DoublyLinkedList():
	def __init__(self):
		self.head = None
		self.tail = None
	
	def setHeadTo(self, node):
		if self.head == node:
			return
		elif self.head is None:
			self.head = node
			self.tail = node
		elif self.head == self.tail:
			self.tail.prev = node
			self.head = node
			self.head.next = self.tail
		else:
			if self.tail == node:
				self.removeTail()
			node.removeBindings()
			self.head.prev = node
			node.next = self.head
			self.head = node
		
	def removeTail(self):
		if self.tail is None:
			return
		if self.tail == self.head:
			self.head = None
			self.tail = None
			return
		# Original: [head ... tail]
		# Modified: [head .. tail]
		self.tail = self.tail.prev
		self.tail.next = None
		
		
class LRUCache:
    def __init__(self, maxSize):
		self.cache = {}
        self.maxSize = maxSize or 1
		self.currentSize = 0
		self.listOfMostRecent = DoublyLinkedList()
	
    # Time: O(1) | Space: O(1)
    def insertKeyValuePair(self, key, value):
        # Write your code here.
		
		if key not in self.cache:
			# check whether if its the maximum size
			if self.currentSize == self.maxSize:
				# evict the last recently used node
				self.evictLeastRecent()
			else:
				self.currentSize += 1
			self.cache[key] = ListNode(key, value)
		else:
			self.replaceKey(key, value)
		
		self.updateMostRecent(self.cache[key])
			
        return
	
    # Helper Methods
	def evictLeastRecent(self):
		keyToRemove = self.listOfMostRecent.tail.key
		self.listOfMostRecent.removeTail()
		del self.cache[keyToRemove]
	
    # Helper Methods
	def updateMostRecent(self, node):
		self.listOfMostRecent.setHeadTo(node)
    
	# Helper Methods
	def replaceKey(self, key, value):
		if key not in self.cache:
			raise Exception("The provided key isnt in the cache")
		self.cache[key].value = value

    # Time: O(1) | Space: O(1)
    def getValueFromKey(self, key):
		
		if key not in self.cache:
			return None
		# Before you return the key with the value, you have to update it to be the most recent
		self.updateMostRecent(self.cache[key])
		
        return self.cache[key].value

    # Time: O(1) | Sapce: O(1)
    def getMostRecentKey(self):
        # Write your code here.
        return self.listOfMostRecent.head.key