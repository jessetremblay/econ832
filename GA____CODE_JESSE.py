# OUTDATED CODE, KEEPING IT AS A BACKUP

import random
import numpy as np

class housekeeping:
    random.seed()

class world:

    def demand_shock():
        η = np.random.normal(0,0.5)
        return η
    
    pool = 2
    period = 30
    genes = 40
# these three may be possible to phase out eventually

    λ = 0.22
    a = 2.3
    d = 0.25 
    epsilon = demand_shock() / d

# a, d = parameters that remain the same throughout paper;
# however, it may be nice to keep them in a class of their own just for flexibility's sake
# λ = supply parameter, η = demand shock

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

    fitness_levels = []

    def fitness():
        for i in bitcode.price_starA:
            accuracy = (1300 - 260 * (i - schedule.price_star()) ** 2)
            fit = 0
            if accuracy > 0:
                fit = accuracy
            else:
                fit == 0
            GA.fitness_levels.append(fit)
            return fit

    def sum_fitness():
        total = 0
        for i in GA.fitness_levels:
            total += i
        return total

    roulette = []
    def check_fitness():
        try:
            for i in GA.fitness_levels:
                percentage = i / GA.sum_fitness()
                GA.roulette.append(percentage)
        except ZeroDivisionError:
            pass
        return True


    def reproduction():
        new_firm = []
        for i in GA.roulette:
            x = np.array(GA.roulette)
            selection = random.choice(range(x.size))
            new_firm.append(GA.firm[selection])

        print(new_firm)


        return True





class schedule:
    def demand():
        try:
            demand = world.a-world.d*(schedule.price())+world.demand_shock()
        except:
            demand = world.a-world.d*(schedule.price0())+world.demand_shock()
        return demand

    def supply():
        try:
            supply_schedule = np.tanh(world.λ * (schedule.price_eit() - 6)) + 1
        except:
            supply_schedule = np.tanh(world.λ*(schedule.price0()-6))+1
        return supply_schedule

    def price():
        price = (world.a - (1/world.pool)*schedule.supply()) / world.d + world.epsilon
        return price
    
    def price0():
        return 5.57
    
    def price_star():
        price_star = (world.a - (1/world.pool)*schedule.supply()) / world.d
        return price_star
    
    def price_eit():
        # p^e(i,t+1)
        price_eit = bitcode.generate_bitcode()+bitcode.generate_bitcode2()*(schedule.price()-bitcode.generate_bitcode())
        return price_eit



class bitcode:

    price_starA = []
    price_starB = []

    def generate_bitcode():
        sum_output = 0
        for i in GA.firm:
            temp_firm = i
            alphai = 10 * sum(([temp_firm[j] * 2 ** (j - 1) / ((2 ** 20) - 1) for j in range(1, int(world.genes / 2))]))
            sum_output += alphai
            bitcode.price_starA.append(sum_output)
        return sum_output

    def generate_bitcode2():
        sum_output = 0
        for i in GA.firm:
            temp_firm = i
            betai = -2 + 4 * sum(([temp_firm[j] * 2 ** (j-21) / ((2 ** 20)-1) for j in range(21, int(world.genes))]))
            sum_output += betai
            bitcode.price_starB.append(sum_output)
        return sum_output

def simulation():
    GA.firm_gen(2, 40)
    bitcode.generate_bitcode()
    bitcode.generate_bitcode2()
    print(GA.firm)

    for i in range(world.period):
        GA.fitness()
        GA.check_fitness()
        GA.reproduction()
#     GA.crossover()
        GA.mutation(0.025)
#     GA.election()
        if i % 5 ==0:
            print(i, schedule.price(), GA.fitness())

    print(GA.firm)
    return True
