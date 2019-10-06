import random
import numpy as np
from scipy.optimize import minimize

class housekeeping:
    random.seed()

class world:
    pool = 1
    period = 200
    genes = 40
# these three may be possible to phase out eventually

    λ = 0.22
    a = 2.3
    d = 0.25
    η = np.random.normal(0,0.5)
    epsilon = η / d

# a, d = parameters that remain the same throughout paper;
# however, it may be nice to keep them in a class of their own just for flexibility's sake
# λ = supply parameter, η = demand shock

class prob:
#    p_sampled = Ei/sum(Ej) , probability to be sampled from old population
    p_cross = 0.6
    p_unchanged = 1 - p_cross
    election = 0.05
# this entire class will be phased out eventually

class GA:
    firm = []

    def string(length):
        strings = []
        while len(strings) < length:
            strings.append(random.randint(0, 1))
        return strings

    def firm_gen(pool, genes):
        while len(GA.firm) < pool:
            firms = GA.string(genes)
            GA.firm.append(firms)
        return GA.firm

    def mutation(mutation_probability):
        mutated_firms = []
        for i in GA.firm:
            temp_firm = []
            for x in i:
                chance = random.uniform(0, 1)
                if chance > mutation_probability:
                    temp_firm.append(x)
                elif chance < mutation_probability and x == 0:
                    x = 1
                    temp_firm.append(x)
                elif chance < mutation_probability and x == 1:
                    x = 0
                    temp_firm.append(x)
            mutated_firms.append(temp_firm)
        GA.firm = mutated_firms
        return GA.firm

    def fitness():
        accuracy = (1300 - 260 * (schedule.price() - schedule.price_star()) ** 2)
        fit = 0
        if accuracy > 0:
            fit = accuracy
        else:
            fit == 0
        return fit

            # temporary error catcher while this is debugged
# placeholder function as part of my pseudocode, will update later
    def reproduction():
        sum_fitness = 1
        reproduction_operator = [1]
        for i in GA.firm:
            try:
                sum_fitness += GA.fitness()
                reproduction_operator[0] = GA.fitness() / sum_fitness
            except ZeroDivisionError:
                pass
        print(reproduction_operator)
        return reproduction_operator

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
    def price_star():
        price_star = schedule.price()-world.epsilon
        return price_star
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
    GA.firm_gen(1, 40)
    bitcode.generate_bitcode()

    for i in range(world.period):
#       GA.reproduction()
#     GA.crossover()
        GA.mutation(0.025)
#     GA.election()
        if i % 5 ==0:
            print(i, schedule.price())
        # this is here for testing purposes

    results = print("The price is", schedule.price() ,"and the equilibrium is ", schedule.equilibrium())
    return results