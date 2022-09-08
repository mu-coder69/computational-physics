
import numpy as np
import matplotlib.pyplot as plt

def trap_int(INTERVAL, f, N=1_000_000, chunk_size=1_000_000, dtype=np.float32):
    h = (INTERVAL[1] - INTERVAL[0]) / (N -1)
    # get the intervals and terms of the chunks
    intervals = chunkify(INTERVAL, N, chunk_size)
    integral = 0
    for i in range(len(intervals)):
        a, b, terms, endpoint = intervals[i]
        x_values = np.linspace(a, b, terms, endpoint=endpoint, dtype=dtype)
        # x_values = np.array([a + i*h for i in range(terms)])
        y_values = f(x_values)
        weights = np.ones(terms, dtype=dtype)/2
        # if i == 0:
        #     weights[0] = 1/2
        # if i == len(intervals) -1:
        #     weights[-1] = 1/2
        # weights *= h
        for j in range(1, terms):
            integral += y_values[j-1]*weights[j-1] + y_values[j]*weights[j]
    return integral*h

def simpson_int(INTERVAL, f, N=1_000_000, chunk_size=1_000_000, dtype=np.float32):
    N = N -1 if N % 2 == 0 else N
    h = (INTERVAL[1] - INTERVAL[0]) / (N -1)
    # get the intervals and terms of the chunks
    intervals = chunkify(INTERVAL, N, chunk_size)
    integral = 0
    for i in range(len(intervals)):
        a, b, terms, endpoint = intervals[i]
        x_values = np.linspace(a, b, terms, endpoint=endpoint, dtype=dtype)
        # x_values = np.array([a + i*h for i in range(terms)])
        # x_values = np.arange(a, b, h)
        y_values = f(x_values)
        weights = np.ones(terms, dtype=dtype)
        weights[0::2] = 1/3
        weights[1::2] = 4/3
        # if i == 0:
        #     weights[0] = 1/3
        # if i == len(intervals) -1:
        #     weights[-1] = 1/3
        # weights *= h
        for j in range(1, terms -1, 2):
            integral += y_values[j-1]*weights[j-1] + y_values[j]*weights[j] + y_values[j+1]*weights[j+1]
    return integral*h

def chunkify(INTERVAL, N, chunk_size=1_000_000):
    # compute de amount of full chunks needed
    # if "N" is not an integer multiple of "chunk_size", then store
    # the remainder terms in "remainder"
    CHUNKS, remainder = divmod(N, chunk_size)
    h = (INTERVAL[1] - INTERVAL[0]) / (N -1)
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
        
# N = tuple(range(3, 1_000_000, 100_000))
N = tuple([int(j*10**i) for i in range(1, 7) for j in range(1, 10)])

errors = []
errors2 = []
errors3 = []
errors4 = []
dtype = np.float64
for n in N:
    trap1 = trap_int([0, 1], lambda x: x*x*x*x*x, N=n, dtype=dtype)
    # trap2 = trap_int([0, 1], lambda x: 3*x*x*x, N=n, dtype=dtype)
    simp1 = simpson_int([0, 1], lambda x: x*x*x*x*x, N=n, dtype=dtype)
    # simp2 = simpson_int([0, 1], lambda x: 3*x*x*x, N=n, dtype=dtype)
    print(f"N: {n}")
    errors.append(abs( (trap1 - 1/6)/(1/6) ))
    # errors2.append(abs(3/4 - trap2))
    errors3.append(abs( (simp1 - 1/6)/(1/6) ))
    # errors4.append(abs(3/4 - simp2))
errors = errors / max(errors)
# errors2 = errors2 / max(errors2)
errors3 = errors3 / max(errors3)
# errors4 = errors4 / max(errors4)
plt.grid()

plt.loglog(N, errors,
            label="simp2", 
            marker="o", 
            markersize=3,
            linestyle="dashed",
            linewidth=0.7)
plt.loglog(N, errors3,
            label="trap2", 
            marker="o", 
            markersize=3,
            linestyle="dashed",
            linewidth=0.7)
plt.legend()
plt.show()