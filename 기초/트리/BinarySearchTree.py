# 노트 클래스 만들기
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

# 이진 탐색 트리에 데이터 넣기
class NodeMgmt:
  def __init__(self, head):
    self.head = head

  def insert(self, value):
    self.current_node = self.head
    while True:
      if value < self.current_node.value:
        if self.current_node.left != None:
          self.current_node = self.current_node.left
        else:
          self.current_node.left = Node(value)
          break
      else:
        if self.current_node.right != None:
          self.current_node = self.current_node.right
        else:
          self.current_node.right = Node(value)
          break

# Test1
head = Node(1)
BST = NodeMgmt(head)