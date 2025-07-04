from imports import math, np

def f_function(N, d, f, flag):
    f_sum = 0
    if flag == 0:
        temp = 0
    else:
        temp = d
    for i in range(N - d):
        if f[temp + i][1] is not None and not math.isnan(f[temp + i][1]):
            f_sum += f[temp + i][1]
    return (1 / (N - d + 1)) * f_sum

def autocorrelation_function(f):
    N = len(f)
    Nd = int(N / 2)
    r = []

    #print(N)
    #print(Nd)

    for d in range(Nd):
        top = 0
        bottom = 0
        temp_b1 = 0
        temp_b2 = 0

        f_minus = f_function(N, d, f, 0)
        F_minus = f_function(N, d, f, 1)

        count = 0 # tracking how many not empty points are used

        for j in range(N - d):

            # Check if valid data is provided
            if f[j][1] is not None and f[d + j][1] is not None and not math.isnan(f[j][1]) and not math.isnan(f[d + j][1]):
                temp1 = float(f[j][1]) - f_minus
                temp2 = float(f[d + j][1]) - F_minus

                #FORMULA TOP PART
                top += temp1 * temp2
                
                #FORMULA BOTTOM PART
                temp_b1 += temp1 ** 2
                temp_b2 += temp2 ** 2

                count += 1

        # If there are no valid data or bottom part of the formula is 0, then return nan
        if count == 0 or temp_b1 == 0 or temp_b2 == 0:
            r.append([d, float("nan")])
        else:
            bottom = math.sqrt(temp_b1 * temp_b2)
            r.append([d, top / bottom])

    return r

def inertia_duration(autocorr_data, N):
    threshold = 2 / math.sqrt(N)
    print(f"Inertia threshold: {threshold}")
    for lag, r_value in autocorr_data:
        if r_value < threshold:
            return lag
    # If it was never less than threshold, then we return 0
    return 0

def signal_with_noise(signal, noise_levels):
    # Extract time and convert values to float
    times = [row[0] for row in signal]
    values = np.array([float(row[1]) for row in signal], dtype=np.float64)

    noisy_signals = []

    for nl in noise_levels:
        noisy_values = values + np.random.normal(0, nl, size=values.shape)
        # Combine unchanged time with noisy values
        noisy_signal = [[t, v] for t, v in zip(times, noisy_values)]
        noisy_signals.append(noisy_signal)

    return noisy_signals