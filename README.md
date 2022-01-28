# programming-course
In this repository is a cheat function. 

This function is created for the programming course in the research master psychology

usage `cheat(assignment_number)` the assignment number is a string input, for instance `'3.2.1'`

output gives the solution of the assigment in text. For instance `cheat('3.2.1')` gives:

````sim_data = np.random.normal(0, 2, 30)
plt.boxplot(sim_data)
plt.savefig('my_first_py_boxplot.png')
plt.clf()
sns.violinplot(data=sim_data)
sns.stripplot(data=sim_data, color='k')
plt.savefig('my_first_py_violin_plot.png')
plt.clf()
