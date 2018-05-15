import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Total population, N.
N = 1000
# Initial number of infective and recovered individuals, I0 and R0.
I0, R0 = 1, 0
# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0
# Contact rate, beta, and mean recovery rate, alpha, (in 1/days).
beta = 0.0002
alpha = 1./10
# A grid of ticks
t = np.linspace(0, 200, 200)

# The SIR model differential equations.
def SIR_eq(y, t, N, beta, alpha):
    S, I, R = y
    Sdot = -beta * S * I
    Idot = beta * S * I - alpha * I
    Rdot = alpha * I
    return Sdot, Idot, Rdot

# Initial conditions vector
y0 = S0, I0, R0
# Integrate the SIR equations over the time grid, t.
ret = odeint(SIR_eq, y0, t, args=(N, beta, alpha))
S, I, R = ret.T

# Plot the data on three separate curves for S(t), I(t) and R(t)
#
s_colour='#ADD694'
i_colour='#F2728C'
r_colour='#67B8C7'
# s_colour='Green'
# i_colour='Red'
# r_colour='Blue'


fig = plt.figure(facecolor='#dddddd')
ax = fig.add_subplot(111, axis_bgcolor='w', axisbelow=True)
ax.plot(t, S, 'b', alpha=0.8, lw=2, label='Susceptible', color=s_colour)
ax.plot(t, I, 'r', alpha=0.8, lw=2, label='Infective', color=i_colour)
ax.plot(t, R, 'g', alpha=0.8, lw=2, label='Removed', color=r_colour)
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
plt.show()