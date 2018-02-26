TO DO:

- Make .app smaller

- raw birth probability is a sample from a normally distributed curve : https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.random.normal.html

- populations lose about 1% of its genetic diversity each "generation" https://www.britannica.com/topic/50-500-rule

- at each generation, the loss of heterozygosity is a linear function of population size (N = 0; loss = .5, N = 500; loss = 0)

- so: diversity = 1 - loss of heterozygosity (0-.5) + gene flow (0-0.1)

- death rate = some function of population and genetic diversity

- if genetic diversity is high, it doesn't really matter, if it is low, than it bumps up death rate massively

- can also add stepping stone populations (no new code, just new populations)

- add density independent mortality (a given percentage of the initial K dies each year (something about 2-3 %))
