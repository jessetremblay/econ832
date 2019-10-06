import random
import numpy as np
from scipy.optimize import minimize

class housekeeping:
    random.seed()


#class world: this will be our environment space where we define different variables

class world:
    pool = 1
# number of firms, 6? in the paper
    period = 200
# generations, 50 in the paper
    genes = 40
# 40 in the paper
    λ = 0.22

    a = 2.3
    d = 0.25
# a, d = parameters that remain the same throughout paper
    η = np.random.normal(0,0.5)
    epsilon = η / d
# λ = supply parameter, η = demand shock



class prob:
#    p_sampled = Ei/sum(Ej) , probability to be sampled from old population
    p_cross = 0.6
    p_unchanged = 1 - p_cross
    p_mut = 0.025
    election = 0.05


class GA:

    firm = []

    def string(length):        
        strings = []
    
        while len(strings) < length:
            strings.append(random.randint(0,1))
# in holmes and lux they defined the first half of the string (mother) as α =
# in holmes and lux they defined the second half of the string (father) as β =
# these are defined on page 12 of the paper and they are the link between strings and the market
 # its very important to code them correctly

        return strings


    def firm_gen():
        while len(GA.firm) < world.pool:
            firms = GA.string(world.genes)
            GA.firm.append(firms)
        return GA.firm

    def fitness():
        try:
            fit = -1 * minimize(1300 - 260 * (schedule.price() - schedule.price0()) ** 2, 0)
        except:
            fit = 1
            # temporary error catcher while this is debugged
        return fit
# placeholder function as part of my pseudocode, will update later
   # def reproduction():
        # GA.fitness() / sumj/fitj



    def crossover():
        # not yet worked on
        offspring = []
        for i in GA.firm:
            chance = random.uniform(0,1)
            # not sure if this is the optimal random function to use
            print(chance)
            if chance < prob.p_cross:
                print("Crossover will occur")
            else:
                print("Crossover will not occur")


    def mutation():
        # mutation working properly, try to improve benchmarks and make it more pythonic
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
        # work on this last
        pass

# this will rely on the string function of the parent to create a mutation


class schedule:
    def cobweb():
        #cobweb needs debugging
        E = -1*minimize(1300-260*(schedule.price()-schedule.price0())**2,0)
        return E


    def supply():
        #appears to be working as intended
        try:
            supply_schedule = np.tanh(world.λ * (schedule.price_estimate() - 6)) + 1
        except:
            supply_schedule = np.tanh(world.λ*(schedule.price0()-6))+1
        return supply_schedule
    def demand():
        #appears to be working as intended
        try:
            demand = world.a-world.d*(schedule.price())+world.η
        except:
            demand = world.a-world.d*(schedule.price0())+world.η
        return demand
    def equilibrium():
        #needs to be tested to see if its working
        summation = []
        for i in range(0, world.pool):
            summation.append((schedule.supply()))
        total = 0
        for i in summation:
            total += i
        equilibrium_star = (1 / world.pool)*total
        return equilibrium_star
    def price():
        # working as intended
        price = (world.a - (1/world.pool)*schedule.supply()) / world.d + world.epsilon
        return price
    def price0():
        # hommes and lux cite this as the experimental price
        return 5.57
    def price_estimate():
        # p^e(i,t+1)
        price_est = bitcode.generate_bitcode()+bitcode.generate_bitcode()*(schedule.price()-bitcode.generate_bitcode())
        return price_est

class bitcode:
    # 11.5 @ a = 2.3? should be between 0,10.
    # Maybe a != a^j(i,t). What is it then?
    def generate_bitcode():
        αit = 0
        for i in GA.firm:
            temp_firm = i
            alphai = 10 * sum(([temp_firm[j] * 2 ** (j - 1) / ((2 ** 20) - 1) for j in range(1, int(world.genes / 2))]))
            αit += alphai
        return (αit)
    # mother, a included in the set [0,1], the bits at position j(j=1...40) of chromosome i at time t
    # 2.59 @ a = 2.3? should be between -2,2
        βit = 0
        for i in GA.firm:
            temp_firm = i
            betai = -2 + 4 * sum(([temp_firm[j] * 2 ** (j-21) / ((2 ** 20)-1) for j in range(21, int(world.genes))]))
            βit += betai
        return (βit)
    # father
    αi = 3  # placeholder values while i figure out the equation
    βi = 1  # placeholder values while i figure out the equation
# main simulation code
def simulation():
    GA.firm_gen()
    bitcode.generate_bitcode()

    for i in range(world.period):
#    GA.reproduction()
#     GA.crossover()
        GA.mutation()
#     GA.election()
        print(i, schedule.price())
        # this is here for testing purposes

#
    results = print("The price is", schedule.price() ,"and the equilibrium is ", schedule.equilibrium())
    return results