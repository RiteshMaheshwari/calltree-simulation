from node import Node

def build_binary_tree(root, nodes, latency_percentiles, default_latency):
  if nodes <= 1:
    return

  left_nodes = nodes
  if left_nodes % 2 == 0:
    left_tree_length = right_tree_length = left_nodes / 2
  else:
    left_tree_length = (left_nodes - 1) / 2
    right_tree_length = (left_nodes + 1) / 2

  node1 = Node(parent=root, latency_percentiles=latency_percentiles, default_latency=default_latency)
  node2 = Node(parent=root, latency_percentiles=latency_percentiles, default_latency=default_latency)

  build_binary_tree(node1, left_tree_length, latency_percentiles, default_latency)
  build_binary_tree(node2, right_tree_length, latency_percentiles, default_latency)

def call_time(root):
  child_times = []
  for child in root.children:
    child_times.append(call_time(child))
  total_time = max(child_times) if len(child_times) > 0 else 0
  total_time += root.get_self_latency()
  return total_time

