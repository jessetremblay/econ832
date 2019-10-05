import random
import numpy as np
from scipy.optimize import minimize

class housekeeping:
    random.seed()


#class world: this will be our environment space where we define different variables

class world:
    pool = 1
# number of firms, 6? in the paper
    period = 5
# generations, 50 in the paper
    genes = 3
# 40 in the paper
    λ = 0.22
    a = 2.3
    d = 0.25
# a, d = parameters
    η = np.random.normal(0,0.5)
    epsilon  = η / d
# λ = supply parameter, η = demand shock

class prob:
#    p_sampled = Ei/sum(Ej) , probability to be sampled from old population
    p_cross = 0.6
    p_unchanged = 1 - p_cross
    p_mut = 0.025
    election = 0.05

class GA:
    def string(length):        
        strings = []
    
        while len(strings) < length:
            strings.append(random.randint(0,1))
# in holmes and lux they defined the first half of the string as α = 
# in holmes and lux they defined the second half of the string as β =             
        return strings

    firm = []

    def firm_gen():
        while len(GA.firm) < world.pool:
            firms = GA.string(world.genes)
            GA.firm.append(firms)
        return GA.firm

    def fitness(profit):
        return profit
# placeholder function as part of my pseudocode, will update later
    def reproduction():
        pass

    def crossover():
        pass

    def mutation():
        # mutation working properly
        mutated_firms = []
        for i in GA.firm:
            temp_firm = []
            for x in i:
                chance = random.uniform(0,1)
                if x == 0:
                    if chance < prob.p_mut:
                        x = 1
                        temp_firm.append(x)
                    else:
                        temp_firm.append(x)
                elif x == 1:
                    if chance < prob.p_mut:
                        x = 0
                        temp_firm.append(x)
                    else:
                        temp_firm.append(x)
            mutated_firms.append(temp_firm)
        GA.firm = mutated_firms
        return GA.firm

    def election():
        pass
# placeholder function as part of my pseudocode, will update later
# this will rely on the string function of the parent to create a mutation


class schedule:
    # def cobweb():
    #     E = -1*minimize(1300-260*(schedule.price()-schedule.price0())**2,)
    #     return E
    # needs heavy debugging
# the demand schedule, prices, etc
    def supply():
        supply_schedule = np.tanh(world.λ*(schedule.price()-6))+1
        return supply_schedule
    def demand():
        demand = world.a-world.d*(schedule.price())+world.η
        return demand
    def equilibrium():
        summation = []
        for i in range(0, world.pool):
            summation.append((schedule.supply()))
        total = 0
        for i in summation:
            total += i
        equilibrium_star = (1 / world.pool)*total
        return equilibrium_star
    def price():
# recursion depth error, need to program for different periods so that price is given by price in last period
#        price = (world.a - (1/world.pool)*schedule.supply()) / world.d +  epsilon
        return 3
    def price0():
        # what is price0?
        return 2

#
# def simulation():
#     GA.reproduction()
#     GA.crossover()
#     GA.mutation()
#     GA.election()
#
#     results = schedule.price()
#     return results