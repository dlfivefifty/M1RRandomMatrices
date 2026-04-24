import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Bernoulli with mean=1 is impossible (p must be in [0,1])
# Mean = p, Variance = p(1-p)
# Variance = 1 is also impossible for Bernoulli
# So we'll use mean=0.5 (p=0.5), variance=0.25, and demonstrate CLT

p = 0.5
n = 100     # number of samples

# Generate Bernoulli samples, shifted and scaled to have mean 0 and variance 1
X = 2*np.random.binomial(n, 0.5, size=N)-1
scaled = X

# Plot
x = np.linspace(-4, 4, 300)
plt.figure(figsize=(8, 5))
plt.hist(scaled, bins=60, density=True, alpha=0.7, color='steelblue', label='Scaled Bernoulli sum')
plt.plot(x, np.exp(-x**2/2) / np.sqrt(2 * np.pi), 'r-', linewidth=2, label='Normal')
plt.title(f'CLT: Scaled Sum of Bernoulli(p={p}) vs Gaussian\n(n={n} trials, {N} samples)')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()