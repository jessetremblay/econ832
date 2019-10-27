import random
import numpy as np
import matplotlib.pyplot as plt

class world:
    def demand_shock():
        η = np.random.normal(0,0.5)
        return η
    def epsilon():
        return world.demand_shock() / world.d

    pool = 6; genes = 40; λ = 2; a = 2.3; d = 0.25

class GA:
    firm = []
    roulette = []
    fitness_levels = []

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
                   # print("Mutation occured!")
                elif chance < mutation_probability and x == 1:
                    x = 0
                    temp_firm.append(x)
                   # print("Mutation occured!")
            mutated_firms.append(temp_firm)
        GA.firm = mutated_firms
        return GA.firm

    def fitness():
        GA.fitness_levels = []
        for i in range(world.pool):
            fit = (1300 - 260 * (schedule.individual_price_observations[i] - (schedule.price_star() / world.pool)) ** 2)
            if fit > 0:
                GA.fitness_levels.append(fit)
            elif fit < 0:
                GA.fitness_levels.append(0)
        return print("Fitness levels: [",GA.fitness_levels,"]")

    def sum_fitness():
        total = 0
        for i in GA.fitness_levels:
            total += i
        return total

    def check_fitness():
        GA.roulette = []
        try:
            for i in GA.fitness_levels:
                percentage = i / GA.sum_fitness()
                GA.roulette.append(percentage)
        except ZeroDivisionError:
            pass

    def reproduction():
        new_firm = []
        for i in GA.roulette:
            x = np.array(GA.roulette)
            selection = np.random.choice(range(x.size), p=GA.roulette)
 #           print("Selection:",selection)
            new_firm.append(GA.firm[selection])
#            print("New firm:",*new_firm,sep="\n")
        GA.firm = []
        GA.firm = new_firm


    def crossover(probability, strings):
        X = []
        Y = []
        offspring = []
        fitness_levels = []
        for i in range(len(GA.firm)):
            chance = random.uniform(0, 1)
            if chance < probability:
 #               print("Crossover occured!")
                X_chromosome = GA.firm[i][:int(strings/2)]
                Y_chromosome = GA.firm[i][int(strings/2):]
                X.append(X_chromosome)
                Y.append(Y_chromosome)
                fitness_levels.append(GA.fitness_levels[i])
 #               print("with xover",i)
  #              print("new fitness list:",fitness_levels)
   #             print("old fitness list;",GA.fitness_levels)
            else:
               # print(i)
 #               print("No crossover occured.")
                offspring.append(GA.firm[i])

            for j in range(len(X)):
                choice = random.choice(X)
                choice2 = random.choice(Y)
                if GA.election(choice+choice2) > fitness_levels[j]:
                    offspring.append(choice + choice2)
                    X.remove(choice)
                    Y.remove(choice2)
                else:
#                    print("Election failed")
                    X.remove(choice)
                    Y.remove(choice2)
                    offspring.append(GA.firm[i])


        GA.firm = []
        GA.firm = offspring

    def election(operator):
        electa = 10 * sum(([operator[j] * 2 ** (j - 1) / ((2 ** 20) - 1) for j in range(1, int(world.genes / 2))]))
        electb = -2 + 4 * sum(([operator[j] * 2 ** (j - 21) / ((2 ** 20) - 1) for j in range(21, int(world.genes))]))
        new_fit=electa+electb*(schedule.price()-electa)
        fit_check = (1300 - 260 * (new_fit-(schedule.price_star() / world.pool)) ** 2)
        return fit_check

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
        price = (world.a - (1/world.pool)*schedule.supply()) / world.d + world.epsilon()
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

    individual_price_observations = []

    def price_eit_indy():
        schedule.individual_price_observations = []
        for i,j in zip(bitcode.price_starA,bitcode.price_starB):
            price_eit_indy = i + j*(schedule.price()-i)
            schedule.individual_price_observations.append(price_eit_indy)
        return schedule.individual_price_observations

class bitcode:
    price_starA = []
    price_starB = []
    price_permA = []
    price_permB = []
    simulation_plot_time = []
    simulation_plot_price = []

    def generate_bitcode():
        bitcode.price_starA = []
        sum_output = 0
        for i in GA.firm:
            temp_firm = i
            alphai = 10 * sum(([temp_firm[j] * 2 ** (j - 1) / ((2 ** 20) - 1) for j in range(1, int(world.genes / 2))]))
            sum_output += alphai
            bitcode.price_starA.append(alphai)
            bitcode.price_permA.append(alphai)
        return sum_output

    def generate_bitcode2():
        bitcode.price_starB = []
        sum_output = 0
        for i in GA.firm:
            temp_firm = i
            betai = -2 + 4 * sum(([temp_firm[j] * 2 ** (j-21) / ((2 ** 20)-1) for j in range(21, int(world.genes))]))
            sum_output += betai
            bitcode.price_starB.append(betai)
            bitcode.price_permB.append(betai)
        return sum_output

    def draw_plot():
        plt.plot(bitcode.simulation_plot_time, bitcode.simulation_plot_price)
        plt.title("Time Series Results", fontsize=20)
        plt.xlabel("Generations")
        plt.ylabel("Price")
        plt.show()

def simulation(period):
    GA.firm = []
    GA.roulette = []
    GA.fitness_levels = []
    bitcode.price_starA = []
    bitcode.price_starB = []
    bitcode.price_permA = []
    bitcode.price_permB = []
    schedule.individual_price_observations = []
    bitcode.simulation_plot_time = []
    bitcode.simulation_plot_price = []

    GA.firm_gen(world.pool, 40)
    bitcode.generate_bitcode()
    bitcode.generate_bitcode2()
    print("Initial Firms:",*GA.firm, sep = "\n")

    for i in range(period):
        bitcode.generate_bitcode()
        bitcode.generate_bitcode2()
        schedule.price_eit_indy()
        GA.fitness()
        GA.check_fitness()
        GA.reproduction()
        GA.crossover(0.6, world.genes)
        GA.mutation(0.01)
        bitcode.simulation_plot_time.append(i)
        bitcode.simulation_plot_price.append(round(schedule.price(),2))
        if i % 2 ==0:
            print(i, GA.fitness(), round(schedule.price(),2))

#summary
    print("Ending Firms:",*GA.firm, sep="\n")
    print(round(schedule.price(),2))
    bitcode.draw_plot()
    print("Mean of prices: \n", round(sum(bitcode.simulation_plot_price)/len(bitcode.simulation_plot_price),2))
    print("Mean of α: \n", round(sum(bitcode.price_permA)/len(bitcode.price_permA),2))
    print("Mean of β: \n", round(sum(bitcode.price_permB)/len(bitcode.price_permB),2))

    return "Simulation finished"