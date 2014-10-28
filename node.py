import random

class Node(object):
  def __init__(self, parent, latency_percentiles, default_latency=1):
    self.parent = parent
    self.children = []
    if self.parent:
      self.parent.children.append(self)
    self.latency_percentiles = latency_percentiles
    if default_latency:
      self.default_latency = default_latency

  def get_self_latency(self):
    this_percentile = 10*random.randint(0,9)
    if this_percentile in self.latency_percentiles.keys():
      return self.latency_percentiles[this_percentile]
    else:
      return self.default_latency
