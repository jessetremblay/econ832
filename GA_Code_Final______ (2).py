import random
import numpy as np
import matplotlib.pyplot as plt

#These are just some lists that we save information in for later use
class save_point:
    firm = []
    firm_after_crossover = []
    firm_pre_election = []
    fitness_firm = []
    fitness_firm_pre_election = []
    roulette = []
    prices_from_selection = []
    prices_from_selection_negative_one = []
    price = []

#The bulk of the genetic algorithm is in this class
class main:
    def string(length):
        strings = []
        while len(strings) < length:
            strings.append(random.randint(0, 1))
        return strings

    def firm_gen(pool, M, genes):
        for i in range(pool):
            temp_firms = []
            while len(temp_firms) < M:
                firms = main.string(genes)
                temp_firms.append(firms)
            save_point.firm.append(temp_firms)
        return save_point.firm

    def mutation(mutation_probability):
        mutated_firms = []
        for i in save_point.firm_after_crossover:
            new_firms = []
            for x in i:
                temp_firm = []
                for y in x:
                    chance = random.uniform(0, 1)
                    if chance > mutation_probability:
                        temp_firm.append(y)
                    elif chance < mutation_probability and y == 0:
                        y = 1
                        temp_firm.append(y)
                    elif chance < mutation_probability and y == 1:
                        y = 0
                        temp_firm.append(y)
                new_firms.append(temp_firm)
            mutated_firms.append(new_firms)
        save_point.firm_pre_election = mutated_firms
        return None

    def crossover(probability, strings):
        offspring = []
        for i in range(len(save_point.firm)):
            temp_offspring = []
            for x in range(len(save_point.firm[i])):
                chance = random.uniform(0, 1)
                if chance < probability:
                    X_chromosome = save_point.firm[i][x][:int(strings / 2)]
                    Y_chromosome = save_point.firm[i][x][int(strings / 2):]
                    K = random.randint(1, strings / 2)
                    U = X_chromosome[K:] + Y_chromosome[:K]
                    V = Y_chromosome[K:] + X_chromosome[:K]
                    Z = U + V
                    temp_offspring.append(Z)
                else:
                    temp_offspring.append(save_point.firm[i][x])
            offspring.append(temp_offspring)
        save_point.firm_after_crossover = offspring
        return None

    def election():
        t_pop = []
        l=0
        for i, j in zip(save_point.fitness_firm, save_point.fitness_firm_pre_election):
            x_pop = []
            m = 0
            for p,q in zip(i,j):
                if p > q:
                    x_pop.append(save_point.firm[l][m])
                    m += 1
                elif p == q:
                    x_pop.append(save_point.firm[l][m])
                    m += 1
                else:
                    x_pop.append(save_point.firm_pre_election[l][m])
                    m += 1
            t_pop.append(x_pop)
            l+=1
        save_point.firm = t_pop
        return None

    def fitness_pre(pool,a,d,λ):
        save_point.fitness_firm = []
        l = 0
        for i in schedule.individual_price_observations:
            m = 0
            temp_list = []
            for j in i:
                fit = (1300 - 260 * (schedule.individual_price_observations[l][m] - schedule.price(a,d,pool,λ)) ** 2)
                if fit > 0:
                    temp_list.append(fit)
                    m+=1
                elif fit < 0:
                    temp_list.append(0.01)
                    m += 1
                else:
                    temp_list.append(0.01)
                    m += 1
            l+=1
            save_point.fitness_firm.append(temp_list)
        total_list = []
        for i in save_point.fitness_firm:
            total = 0
            for j in i:
                total += j
            total_list.append(total)
        save_point.roulette = []
        q=0
        for i in save_point.fitness_firm:
            roulette_temp = []
            for j in i:
                percentage = j / total_list[q]
                roulette_temp.append(percentage)
            q+=1
            save_point.roulette.append(roulette_temp)
        return None

    def fitness_post(pool,a,d,λ):
        save_point.fitness_firm_pre_election = []
        m = 0
        for i in schedule.individual_price_observations:
            k = 0
            temp_list = []
            for j in i:
                fit = (1300 - 260 * (schedule.individual_price_observations[m][k] - schedule.price(a,d,pool,λ)) ** 2)
                if fit > 0:
                    temp_list.append(fit)
                    k+=1
                elif fit < 0:
                    temp_list.append(0.01)
                    k += 1
                else:
                    temp_list.append(0.01)
                    k += 1
            save_point.fitness_firm_pre_election.append(temp_list)
            m+=1
        return None

    def reproduction(M):
        new_firm = []
        n = 0
        for i in save_point.roulette:
            holder_firm = []
            while len(holder_firm) < M:
                x = np.array(i)
                selection = np.random.choice(range(x.size), p=i)
                holder_firm.append(save_point.firm[n][selection])
            new_firm.append(holder_firm)
            n+=1
        save_point.firm = new_firm
        return None

#This class primarily handles how we do the decoding of the two halves of the strings, alpha and beta from the paper
class bitcode:
    price_starA = []
    price_starB = []
    price_permA = []
    price_permB = []
    simulation_plot_time = []
    simulation_plot_price = []

    def generate_bitcode(string_length):
        bitcode.price_starA = []
        for i in save_point.firm:
            temp_output = []
            for k in i:
                string = ''
                for y in range(1,int(string_length/2)):
                    string += str(k[y])
                string2 =int(string,2)
                temp_output.append(string2)
            normalized = []
            for k in temp_output:
                norm_output = (k*10)/max(temp_output)
                normalized.append(norm_output)
            bitcode.price_starA.append(normalized)
        return bitcode.price_starA

    def generate_bitcode2(string_length):
        bitcode.price_starB = []
        for i in save_point.firm:
            temp_output = []
            for k in i:
                string = ''
                for y in range(21,int(string_length)):
                    string += str(k[y])
                string2 =int(string,2)
                temp_output.append(string2)
            normalized = []
            for k in temp_output:
                norm_output = (2*k)/max(temp_output)-1
                normalized.append(norm_output)
            bitcode.price_starB.append(normalized)
        return bitcode.price_starB

#This class has the bulk of the environment in it, ie. the supply functions, prices, selection and so on; also, it includes our plot function
class schedule:
    individual_price_observations = []
    individual_price_observations_minus_one = []
    pred_price_perm_list = []

    def supply(λ):
        supply_schedule = []
        k =0
        for i in save_point.prices_from_selection_negative_one:
            supply_sched = np.tanh(λ * (save_point.prices_from_selection_negative_one[k] - 6)) + 1
            supply_schedule.append(supply_sched)
            k+=1
        return sum(supply_schedule)

    def demand_shock():
        η = np.random.normal(0, 0.5)
        return η

    def epsilon(d):
        return schedule.demand_shock() / d

    def selection(M):
        save_point.prices_from_selection_negative_one = save_point.prices_from_selection
        save_point.prices_from_selection = []
        k = 0
        for i in save_point.roulette:
            x = np.array(i)
            selection = np.random.choice(range(x.size), p=i)
            save_point.prices_from_selection.append(schedule.individual_price_observations_minus_one[k][selection])
            k +=1
        schedule.pred_price_perm_list.append(sum(save_point.prices_from_selection)/M)
        return None

    def price(a,d,firms,λ):
        save_point.price = []
        try:
            price = (((a - ((1 / firms) * schedule.supply(λ)))) / d)+schedule.epsilon(d)
            save_point.price.append(price)
        except IndexError:
            price = 5.6
            save_point.price.append(price)
        else:
            pass
        return price

    def price_eit_indy(a,d,firms,λ):
        schedule.individual_price_observations_minus_one = schedule.individual_price_observations
        schedule.individual_price_observations = []
        m = 0
        for i, j in zip(bitcode.price_starA, bitcode.price_starB):
            k = 0
            temp_list = []
            for p,q in zip(i,j):
                price_eit_indy = bitcode.price_starA[m][k] + bitcode.price_starB[m][k] * (schedule.price(a,d,firms,λ) - bitcode.price_starA[m][k])
                temp_list.append(price_eit_indy)
                k += 1
            m+=1
            schedule.individual_price_observations.append(temp_list)
        return schedule.individual_price_observations

    def draw_plot():
        plt.plot(bitcode.simulation_plot_time, bitcode.simulation_plot_price, label="Prices")
        plt.plot(bitcode.simulation_plot_time, schedule.pred_price_perm_list, label="Predicted Prices")
        plt.title("Time Series Results", fontsize=20)
        plt.xlabel("Generations")
        plt.ylabel("Price")
        plt.legend()
        plt.show()

#This is the main simulation function that brings everything together
def simulation(period, firms, firm_strats, string_length, crossover_probability, mutation_probability,a,d,λ):
    # I am resetting all of the lists on the first run, so you can run the simulation multiple times!
    save_point.firm = []
    save_point.firm_after_crossover = []
    save_point.firm_pre_election = []
    save_point.fitness_firm = []
    save_point.fitness_firm_pre_election = []
    save_point.roulette = []
    save_point.prices_from_selection = []
    save_point.prices_from_selection_negative_one = []
    save_point.price = []
    schedule.individual_price_observations = []
    schedule.individual_price_observations_minus_one = []
    schedule.pred_price_perm_list = []
    bitcode.price_starA = []
    bitcode.price_starB = []
    bitcode.price_permA = []
    bitcode.price_permB = []
    bitcode.simulation_plot_time = []
    bitcode.simulation_plot_price = []

#This sets everything up in period 0
    main.firm_gen(firms, firm_strats, string_length)
    bitcode.generate_bitcode(string_length)
    bitcode.generate_bitcode2(string_length)
    schedule.price_eit_indy(a,d,firms,firm_strats)
    print("Initial Firms:",*save_point.firm, sep = "\n")

#This runs the simulation for t periods
    for i in range(period):
        bitcode.generate_bitcode(string_length)
        bitcode.generate_bitcode2(string_length)
        schedule.price_eit_indy(a,d,firms,λ)
        main.fitness_pre(firms,a,d,λ)
        main.reproduction(firm_strats)
        main.crossover(crossover_probability, string_length)
        main.mutation(mutation_probability)
        main.fitness_post(firms,a,d,λ)
        main.election()
        schedule.selection(firm_strats)
        bitcode.simulation_plot_time.append(i)
        bitcode.simulation_plot_price.append(round(schedule.price(a,d,firms,λ),2))
        if i % 5 ==0:
            print(i, round(schedule.price(a,d,firms,λ),2))
#Generating a summary of the simulation
    print("Ending Firms:",*save_point.firm, sep="\n")
    schedule.draw_plot()
    print("Mean of prices: \n", round(sum(bitcode.simulation_plot_price)/len(bitcode.simulation_plot_price),2))
    print("Mean of predicted prices: \n", round(sum(schedule.pred_price_perm_list)/len(schedule.pred_price_perm_list),2))
#    print("Mean of α: \n", round(sum(bitcode.price_permA)/len(bitcode.price_permA),2))
#    print("Mean of β: \n", round(sum(bitcode.price_permB)/len(bitcode.price_permB),2))
    return "Simulation finished"

print("Hello Jasmina and Liang, welcome to our replication project. For your ease of use, we have created a small list of instructions \n"
      "If you would like to run a simulation, you can use our simulation function. Simulation() takes 9 arguments. \n"
      "1. The periods you want to run the simulation for; 2. The number of firms you want; 3. The strategies that each firm possesses \n"
      "4. The string length of each strategy; 5. The probability that crossover will occur; 6. The probability that mutation will occur \n"
      "7. The parameter a; 8. The parameter d; 9. The parameter λ \n"
      "Below, we have provided an example simulation based on some of the values used in the Hommes and Lux paper for your use \n"
      "Thank you for a fun semester \n"
      "Type this in -> simulation(50, 6, 10, 40, 0.6, 0.01,2.3,0.25,0.22)")
