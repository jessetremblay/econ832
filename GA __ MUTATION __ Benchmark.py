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
  

# finished code

def mutation(mutation_probability):
    firm = [[1,0,1,1,0,1,1,0,0,1,1,0,1,1,1,0,1,1,0,1],[1,0,1,1,0,1,1,0,0,1,1,0,1,1,1,0,1,1,0,1],[1,0,1,1,0,1,1,0,0,1,1,0,1,1,1,0,1,1,0,1],[1,0,1,1,0,1,1,0,0,1,1,0,1,1,1,0,1,1,0,1],[1,0,1,1,0,1,1,0,0,1,1,0,1,1,1,0,1,1,0,1],[1,0,1,1,0,1,1,0,0,1,1,0,1,1,1,0,1,1,0,1]]
    mutated_firms = []
    for i in firm:
        temp_firm = []
        for x in i:
            chance = random.uniform(0,1)
            if chance > mutation_probability:
                temp_firm.append(x)
            elif chance < mutation_probability and x == 0:
                x = 1
                temp_firm.append(x)
            elif chance < mutation_probability and x == 1:
                x = 0
                temp_firm.append(x)
        mutated_firms.append(temp_firm)
    firm = mutated_firms
    return firm

def mut_bm():
    firm = [[1,0,1,1,0,1,1,0,0,1,1,0,1,1,1,0,1,1,0,1],[1,0,1,1,0,1,1,0,0,1,1,0,1,1,1,0,1,1,0,1],[1,0,1,1,0,1,1,0,0,1,1,0,1,1,1,0,1,1,0,1],[1,0,1,1,0,1,1,0,0,1,1,0,1,1,1,0,1,1,0,1],[1,0,1,1,0,1,1,0,0,1,1,0,1,1,1,0,1,1,0,1],[1,0,1,1,0,1,1,0,0,1,1,0,1,1,1,0,1,1,0,1]]
    mutated_firms = []
    for i in firm:
        temp_firm = []
        for x in i:
            chance = random.uniform(0,1)
            if chance > 0.25:
                temp_firm.append(x)
            elif chance < 0.25 and x == 0:
                x = 1
                temp_firm.append(x)
            elif chance < 0.25 and x == 1:
                x = 0
                temp_firm.append(x)
        mutated_firms.append(temp_firm)
    firm = mutated_firms
    return firm

Benchmark.run(mut_bm)
