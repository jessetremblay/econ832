import sys
import statistics
import time
import random

class Benchmark:
  @staticmethod
  def run(function):
      timings = []
      for i in range(100):
          startTime = time.time()
          function()
          seconds = time.time() - startTime
          timings.append(seconds)
          mean = statistics.mean(timings)
          print("{0} {1:3.2f} {2:3.2f}".format(
              1 + i, mean,
              statistics.stdev(timings, mean)
              if i > 1 else 0))


firm = []
def string(length):        
    strings = []
    while len(strings) < length:
        strings.append(random.randint(0,1))
    return strings

def firm_gen(pool, genes):
    while len(GA.firm) < pool:
        firms = GA.string(genes)
        GA.firm.append(firms)
    return GA.firm


def firm_bm():
    while len(firm) < 6:
        firms = string(40)
        firm.append(firms)
    return firm

Benchmark.run(firm_bm)

# Great benchmarks, this is finished code unless you see improvements.
