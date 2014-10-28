from node import Node
from tree import *
import sys

latency_percentiles = {90:1000}
default_latency = 1

nodes = int(sys.argv[1])
total_call_time = 0

for i in range(1000):
  root = Node(parent=None, latency_percentiles=latency_percentiles, default_latency=default_latency)
  build_binary_tree(root, nodes=nodes, latency_percentiles=latency_percentiles, default_latency=1)
  total_call_time += call_time(root)
  
print total_call_time / 1000
