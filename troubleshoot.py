firm = [[[1,0,1,1,0,0],[1,1,1,0,0,0]],[[1,0,0,1,1,1],[1,1,1,0,0,0]]]
firm_after_crossover = []
import random

def crossover(probability, strings):
    offspring = []
    for i in range(len(firm)):
        temp_offspring = []
        for x in range(len(firm[i])):
            chance = random.uniform(0, 1)
            if chance < probability:
                X_chromosome = firm[i][x][:int(strings / 2)]
                Y_chromosome = firm[i][x][int(strings / 2):]
                K = random.randint(0, strings / 2)
                U = X_chromosome[K:] + Y_chromosome[:K]
                V = Y_chromosome[K:] + X_chromosome[:K]
                Z = U + V
                temp_offspring.append(Z)
                print("crossover occured",x)
            else:
                temp_offspring.append(firm[i])
                print("crossover did not occur in firm",x
                      )
        offspring.append(temp_offspring)
    firm_after_crossover = offspring
    print(firm_after_crossover)
    return None
