'''
Perform an estimation of PI using Monte Carlo, parallelized.
The algorithm is very simple: generate random points in the unit square
(area = 1), then count how many of them are in the circle quarter (area pi/4).

The number of points in the circle quarter will give an estimation for pi/4.
Note that I omitted the confidence intervals, for simplicity.
'''

import numpy as np
from multiprocessing import Pool
import time
import os


def estimate_nbr_points_in_quarter_circle(nbr_samples):
    '''
    Return how many points are actually in the circle
    '''
    # Seed is generated every time since the function will be called in parall
    print(f"...on pid {os.getpid()}")
    np.random.seed()
    xs = np.random.uniform(0, 1, nbr_samples)
    ys = np.random.uniform(0, 1, nbr_samples)
    valid_points = (xs * xs + ys * ys) <= 1.
    return np.sum(valid_points)
#---


if __name__ == '__main__':
    # Use 1e8 points for the Monte Carlo estimation
    nbr_samples_in_total = 1e8

    # Execute 4 processes in parallel
    nbr_parallel_blocks = 4
    pool = Pool(processes = nbr_parallel_blocks)

    # Each process will take care about 1e8/4 points
    nbr_samples_per_worker = int(nbr_samples_in_total / nbr_parallel_blocks)

    # Construct a list of 4 elements, each being the argument for the
    # function to run. In our case, each function just has the number of poins
    arguments = [nbr_samples_per_worker] * nbr_parallel_blocks

    start_time = time.time()

    # Results here contains the number of points inside the quarter circle
    results = pool.map(estimate_nbr_points_in_quarter_circle, arguments)

    # Sum all of them to estimate pi via this frequency
    results = np.sum(results) * 4. / nbr_samples_in_total
    print(f"Estimation: {results}")
    print(f"time: {time.time() - start_time}")
