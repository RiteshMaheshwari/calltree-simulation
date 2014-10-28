from node import Node
from tree import *
import sys

# dict with key being percentile value (10, 20, 30... 90) and value being the latency at that percentile
latency_percentiles = {90:1000}
# This is returned if dict above does not specify the percentile
default_latency = 1

nodes = int(sys.argv[1])
total_call_time = 0

for i in range(1000):
  root = Node(parent=None, latency_percentiles=latency_percentiles, default_latency=default_latency)
  build_binary_tree(root, nodes=nodes, latency_percentiles=latency_percentiles, default_latency=1)
  total_call_time += call_time(root)
  
print total_call_time / 1000
