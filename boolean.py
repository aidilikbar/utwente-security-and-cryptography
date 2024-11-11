import numpy as np

# Function to calculate Walsh Transform for a Boolean function
def walsh_transform(truth_table):
    n = len(truth_table)
    walsh_spectrum = truth_table.copy()
    for i in range(int(np.log2(n))):
        for j in range(0, n, 2**(i+1)):
            for k in range(2**i):
                u = walsh_spectrum[j+k]
                v = walsh_spectrum[j+k+2**i]
                walsh_spectrum[j+k] = u + v
                walsh_spectrum[j+k+2**i] = u - v
    return walsh_spectrum

# Function to check if the Boolean function is balanced
def is_balanced(truth_table):
    count_ones = sum(truth_table)
    return count_ones == len(truth_table) // 2

# Function to check correlation immunity up to t-th order
def is_t_correlation_immune(truth_table, t):
    walsh_spectrum = walsh_transform(truth_table)
    n = len(truth_table)
    num_vars = int(np.log2(n))
    
    for i in range(1, t+1):
        for index in range(n):
            hamming_weight = bin(index).count('1')
            if hamming_weight == i and walsh_spectrum[index] != 0:
                return False
    return True

# Example truth table (use hex format to generate the truth table)
truth_table = [0, 1, 1, 0, 1, 0, 0, 1]  # Example for 3-variable function

# Check if the function is balanced and t-th order correlation immune
t = 1  # For 1st order correlation immunity
print("Is balanced:", is_balanced(truth_table))
print(f"Is {t}-th order correlation immune:", is_t_correlation_immune(truth_table, t))