import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

N = 500  # number of samples
n = [1,5,15]  # sample size
colors = ['red', 'orange', 'green']
rng = np.random.default_rng()  # create a generator instance

mu = 0.0  # mean of normal distribution
sigma = 1.0  # standard deviation of normal distribution
x = np.linspace(-3, 3, 100)  # x values for plotting normal distribution
for n_val, n_color in zip(n, colors):
    samples = rng.normal(loc=mu, scale=sigma, size=(N,n_val))  # loc = mean, scale = stddev
    samples_mean = np.mean(samples, axis=1)  # mean of each sample
    plt.hist(samples_mean, color = n_color, bins=100, density=True, alpha=0.5, 
             label='n={}'.format(n_val))

    pdf = norm.pdf(x, loc=mu, scale=sigma/np.sqrt(n_val))  # probability density function
    plt.plot(x, pdf, color = n_color, label='n={}'.format(n_val))

plt.axvline(mu, color='grey', ls='--', label='mean={}'.format(mu))
plt.legend()
plt.savefig("output/random_histogram.png", dpi=300)  # save figure
plt.show()