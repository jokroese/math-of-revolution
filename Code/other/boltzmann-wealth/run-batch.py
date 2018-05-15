from model import *	#imports the libraries needed in model.py
import matplotlib.pyplot as plt #for drawing the results


#multiple runs
all_wealth = []
for j in range(100):		#number of instantiations
    # Run the model
    model = MoneyModel(100,1) #number of agents
    for i in range(50):		#number of steps
        model.step()

    # Store the results
    for agent in model.schedule.agents:
        all_wealth.append(agent.wealth)



#fitting
import numpy as np
import scipy.stats as stats

# x = np.linspace(0, max(all_wealth), max(all_wealth))
# markerline, stemlines, baseline = plt.stem(x, all_wealth, '-.')
# plt.setp(baseline, 'color', 'r', 'linewidth', 2)


plt.hist(all_wealth, bins=range(max(all_wealth)+1),
	normed=True, rwidth=0.5, align='left')
plt.xlabel('Agent Wealth')
plt.ylabel('Frequency Density')


# #fit maxwell-bolztmann curve
# maxwell = stats.maxwell
# data = maxwell.rvs(loc=0, scale=2, size=100*100)
# params = maxwell.fit(data, floc=0)
# print(params)

# #plot m-b curve
# x = np.linspace(0, 10, 100)
# plt.plot(x, maxwell.pdf(x, *params), lw=3)

# #plot m-b curve
# xt = plt.xticks()[0]  
# xmin, xmax = 0, max(xt)  
# lnspc = np.linspace(xmin, xmax, len(all_wealth))
# ab,bb = stats.maxwell.fit(all_wealth)  
# pdf_beta = stats.maxwell.pdf(lnspc, ab, bb,)  
# plt.plot(lnspc, pdf_beta, label="Beta")


#plot beta curve
# xt = plt.xticks()[0]  
# xmin, xmax = min(xt), max(xt)  
# lnspc = np.linspace(xmin, xmax, len(all_wealth))
# ab,bb,cb,db = stats.beta.fit(all_wealth)  
# pdf_beta = stats.beta.pdf(lnspc, ab, bb,cb, db)  
# plt.plot(lnspc, pdf_beta, label="Beta")


# #plot beta curve
# xt = plt.xticks()[0]  
# xmin, xmax = min(xt), max(xt)  
# lnspc = np.linspace(xmin, xmax, len(all_wealth))
# ab,bb,cb,db = stats.beta.fit(all_wealth)  
# pdf_beta = stats.beta.pdf(lnspc, ab, bb,cb, db)  
# plt.plot(lnspc, pdf_beta, label="Beta")

#plot gamma curve
# ag,bg,cg = stats.gamma.fit(all_wealth)  
# pdf_gamma = stats.gamma.pdf(lnspc, ag, bg,cg)  
# plt.plot(lnspc, pdf_gamma, label="Gamma")


plt.show()