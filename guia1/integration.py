
import numpy as np
import matplotlib.pyplot as plt

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
        if i == len(intervals):
            weights[-1] /= 2
        integral += weights @ y_values.T
    return integral

def simpson_int(INTERVAL, f, N=1_000_000, chunk_size=1_000_000, dtype=np.float32):
    N = N -1 if N % 2 == 0 else N
    h = (INTERVAL[1] - INTERVAL[0]) / (N +1)
    # get the intervals and terms of the chunks
    intervals = chunkify(INTERVAL, N, chunk_size)
    integral = 0
    for i in range(len(intervals)):
        a, b, terms, endpoint = intervals[i]
        # x_values = np.linspace(a, b, terms +1, endpoint=endpoint, dtype=dtype)
        x_values = np.arange(a, b, h)
        y_values = f(x_values)
        weights = np.full(len(y_values), 4*h/3, dtype=dtype)
        weights[::2] = 2*h/3
        if i == 0:
            weights[0] = h/3
        if i == len(intervals):
            weights[-1] = h/3
        
        integral += weights @ y_values.T
    return integral

def chunkify(INTERVAL, N, chunk_size=1_000_000):
    # compute de amount of full chunks needed
    # if "N" is not an integer multiple of "chunk_size", then store
    # the remainder terms in "remainder"
    CHUNKS, remainder = divmod(N, chunk_size)
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
        
N = tuple(range(10, 10_000_000, 100_000))
errors = []
errors2 = []
errors3 = []
errors4 = []
dtype = np.float64
for n in N:
    trap1 = trap_int([0, 1], lambda x: x*x*x*x*x, N=n, dtype=dtype)
    trap2 = trap_int([0, 1], lambda x: 3*x*x*x, N=n, dtype=dtype)
    simp1 = simpson_int([0, 1], lambda x: x*x*x*x*x, N=n, dtype=dtype)
    simp2 = simpson_int([0, 1], lambda x: 3*x*x*x, N=n, dtype=dtype)
    print(f"N: {n}, simp1: {simp1}, simp2: {simp2}")
    errors.append(abs(1/6 - trap1))
    errors2.append(abs(3/4 - trap2))
    errors3.append(abs(1/6 - simp1))
    errors4.append(abs(3/4 - simp2))
errors = errors / max(errors)
errors2 = errors2 / max(errors2)
errors3 = errors3 / max(errors3)
errors4 = errors4 / max(errors4)
plt.loglog(N, errors, label="$x^5$", c="k")
plt.loglog(N, errors2, label="$1/2 x^{-1/2}$", c="k")
# plt.title("Trapeze integral")
# plt.legend()
# plt.show()
plt.loglog(N, errors3, label="$x^5$", c="r")
plt.loglog(N, errors4, label="$1/2 x^{-1/2}$", c="r")
# plt.title("Simpson integral")
plt.legend()
plt.show()
