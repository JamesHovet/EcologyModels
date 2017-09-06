import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### FLAGS
DISTRIBUTION_MATRIX = "./JH_WS_DistributionMatrixCSV.csv"
PROB_EXTINCTION_VECTOR = "./JH_WS_ExtinctionVectorCSV.csv"

NUM_TRIALS = 1000

DISTANCE_UNIT_FACTOR = 75

PROB_EXTINCTION_MULTIPLICATION_FACTOR   = 1
PROB_COLONIZATION_MULTIPLICATION_FACTOR = 1

### READ DATA INTO FORMAT WE WANT
# pandas (pd.anything) lets us read csv's really easily, we then convert them into numpy arrays, which allows us to do linear algebra really quickly and easily

dist_db = pd.read_csv(DISTRIBUTION_MATRIX)
Pe_db = pd.read_csv(PROB_EXTINCTION_VECTOR)

dist_db = dist_db.fillna(1e5) #replace NaN's with big number so that the log function turns them to 0 probability

Pe = (np.array(Pe_db.Pe)[:]).astype("float")
dist = (np.array(dist_db)[:,1:]).astype("float")

 #in case we want to mess with the numbers a bit, we can divide the extinction vector by a scalar

### Transform distance matrix into probability of colonization matrix
#parameters found by regression to fit given ln curve: y ~ a * ln(x) + b
a = -0.34869
b = 0.98509

dist = a*np.log(np.ceil(dist/DISTANCE_UNIT_FACTOR)) + b #transform distance input into probability of colonization output: y = a*ln(x) + b

dist[np.where(dist<0)] = 0 #replace anything lower than 0 with a 0.

results = []

for i in range(NUM_TRIALS): #Run the test a certain number of times
    Pe = Pe * PROB_EXTINCTION_MULTIPLICATION_FACTOR

    #generate two sets of random numbers in the shapes of the extinction vector and distribution matrix (0-1 exclusive, I think...)
    random1 = np.random.rand(Pe.shape[0])
    random2 = np.random.rand(dist.shape[0],dist.shape[1])

    isAlive = np.zeros(Pe.shape)
    isAlive[np.where(Pe < random1)] = 1 #roll dice, see if patch is still alive


    Pc = dist * isAlive #elementwise multiply to eliminate colonization from dead cells, still allows colonization TO dead cells

    Pc = Pc * PROB_COLONIZATION_MULTIPLICATION_FACTOR #mess with numbers

    PcMirrored = Pc + np.transpose(Pc) #add colonization to and colonization from (normal and transposed matricies)

    isColonized = np.zeros(dist.shape)
    isColonized[np.where(PcMirrored > random2)] = 1 #create a new matrix of 0's where the patch is not colonized and 1's where it is

    patchColonized = np.sum(isColonized, axis=1)

    final = np.zeros(dist.shape[0])
    final[np.where(np.logical_or(isAlive,patchColonized))] = 1 #final matrix: 1 if colonized or not dead

    sumOfAliveCells = np.sum(final)
    results.append(sumOfAliveCells)


#Calculate number of extinction events (0 alive populations) as a % of NUM_TRIALS

numZero = NUM_TRIALS - np.count_nonzero(np.array(results)) #how many times the meta-population goes extinct
percentage = numZero/NUM_TRIALS

print("THE FINAL PROBABILITY OF EXTINCTION IS :", percentage)
