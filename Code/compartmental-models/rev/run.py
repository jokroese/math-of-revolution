import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Total population, P.
P = 10 * 10**6
# Percentage of population who are open to revolting, N. (based on age, political inclination, medical history etc.)
N=P*(1/5)
# Initial number of exposed, infected and recovered individuals, E0, I0 and R0.
E0, I0, R0 = 0, 1, 0
# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0 -E0
# Contact rate, beta, activation rate, gamma, and mean removal rate, alpha, (in 1/days).
alpha = 1./10
gamma = 1./5
beta = 1.5*alpha/N
# A grid of ticks
t_max=4500
ticks_per_day=100
t = np.linspace(0, t_max, t_max*ticks_per_day)

# Define transfer rate g(x)
# k is the threshold, n is the severity of the threshold, delta is the percentage of 'zealots'
k=3/50
n=2
delta=1/100
def g(x):
    y = delta+ gamma * ((x) ** n) / (k ** n + (x) ** n)
    return y

# The SIR model differential equations.
def SEIR_eq(y, t, N, beta, gamma, alpha):
    S, E, I, R = y
    Sdot = -beta * S * I
    Edot = beta * S * I - E * g(I/N)
    Idot = E * g(I/N) - alpha * I
    Rdot = alpha * I
    return Sdot, Edot, Idot, Rdot

# Initial conditions vector
y0 = S0, E0, I0, R0
# Integrate the SIR equations over the time grid, t.
ret = odeint(SEIR_eq, y0, t, args=(N, beta, gamma, alpha))
S, E, I, R = ret.T

# Plot the data
# colours
s_colour='#ADD694' # Green
e_colour='#FFCD47' # Yellow
i_colour='#F2728C' # Red
r_colour='#67B8C7' # Blue

font = {'family' : 'normal',
        'size'   : 12}
plt.rc('font', **font)

fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='w', axisbelow=True)
ax.plot(t, S, alpha=0.8, lw=3, label='Susceptible', color=s_colour)
ax.plot(t, E, alpha=0.8, lw=3, label='Exposed', color=e_colour)
ax.plot(t, I, alpha=0.8, lw=3, label='Infective', color=i_colour)
ax.plot(t, R, alpha=0.8, lw=3, label='Removed', color=r_colour)
ax.set_xlabel('Time (Days)')
ax.set_ylabel('Number of Individuals')
ax.set_xlim(0)
ax.set_ylim(0,N*1.1)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='black', lw=1, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.9)
for spine in ('top', 'right'):
    ax.spines[spine].set_visible(False)
# parameter_text = 'alpha=%s, beta=%s, gamma=%s, delta=%s, k=%s, n=%s, N=%s' % \
#                      ('%.4f' % alpha, '%.4f' % beta, '%.2f' % gamma, '%.2f' % delta, '%.2f' % k, '%.1f' % n, N)
# plt.text(t_max/20, N*1.1, parameter_text,
#     bbox={'facecolor':'white', 'alpha':0.8, 'pad':10})
plt.show()