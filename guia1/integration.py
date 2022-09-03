
import numpy as np
import matplotlib.pyplot as plt
from time import time

def trap_int(INTERVAL, f, N=1_000_000, chunk_size=1_000_000, dtype=np.float32):
    h = (INTERVAL[1] - INTERVAL[0]) / N
    # get the intervals and terms of the chunks
    intervals = chunkify(INTERVAL, N, chunk_size)
    integral = 0
    for i in range(len(intervals)):
        a, b, terms, endpoint = intervals[i]
        x_values = np.linspace(a, b, terms, endpoint=endpoint, dtype=dtype)
        y_values = f(x_values)
        weights = np.full(len(y_values), h, dtype=dtype)
        if i == 0:
            weights[0] /= 2
        elif i == len(intervals):
            weights[-1] /= 2
        integral += weights @ y_values.T
    return integral

def chunkify(INTERVAL, N, chunk_size=1_000_000):
    # compute de amount of full chunks needed
    # if "N" is not an integer multiple of "chunk_size", then store
    # the remainder terms in "remainder"
    CHUNKS, remainder = N // chunk_size, N % chunk_size
    h = (INTERVAL[1] - INTERVAL[0]) / N
    # "INTERVAL_STEP" is the range of the intervals
    INTERVAL_STEP = chunk_size * h
    intervals = []
    for chunk in range(CHUNKS +1 if remainder else CHUNKS):
        # left limit
        a = INTERVAL[0] + chunk*INTERVAL_STEP
        terms = None
        # if there is remainder and is the last chunk, then:
        if remainder and chunk == CHUNKS:
            b = INTERVAL[1]
            endpoint = True
            terms = remainder
        # but if there is no remainder and is the last chunk, then:
        elif not remainder and chunk == CHUNKS -1:
            b = INTERVAL[1]
            endpoint = True
            terms = chunk_size
        else:
            b = a + INTERVAL_STEP
            endpoint = False
            terms = chunk_size
        intervals.append((a, b, terms, endpoint))
    return intervals
        
N = tuple(range(1, 10_000_000, 100_000))
errors = []
for n in N:
    start = time()
    func = trap_int([0, 1], lambda x: x*x*x*x*x, N=n, dtype=np.float32)
    end = time()
    print(f"N: {n}, f: {func}, time: {round(end - start, 2)}s")
    errors.append(abs(1/6 - func))
plt.loglog(N, errors)
plt.show()