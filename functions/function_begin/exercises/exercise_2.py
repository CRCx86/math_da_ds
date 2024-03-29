import numpy as np
from matplotlib import pyplot as plt

population_data = np.array([[2000, 146596869],
                            [2001, 145976482],
                            [2002, 145306497],
                            [2003, 144648618],
                            [2004, 144067316],
                            [2005, 143518814],
                            [2006, 143049637],
                            [2007, 142805114],
                            [2008, 142742366],
                            [2009, 142785348],
                            [2010, 142849468],
                            [2011, 142960908],
                            [2012, 143201721],
                            [2013, 143506995],
                            [2014, 146090613],
                            [2015, 146405999],
                            [2016, 146674541],
                            [2017, 146842401],
                            [2018, 146830575],
                            [2019, 146764655],
                            [2020, 146459803],
                            [2021, 145864296]])

plt.plot(population_data[:, 0], population_data[:, 1])
