def cheat(assignment):
    if assignment == '3.2.1':
        print("""sim_data = np.random.normal(0, 2, 30)
plt.boxplot(sim_data)
plt.savefig('my_first_py_boxplot.png')
plt.clf()
sns.violinplot(data=sim_data)
sns.stripplot(data=sim_data, color='k')
plt.savefig('my_first_py_violin_plot.png')
plt.clf()""")

    elif assignment == '3.2.2':
        print("""titanic_data = pd.read_csv(
'https://raw.githubusercontent.com/hannesrosenbusch/schiphol_class/master/titanic.csv')  # loading in dataset from github
survived_f = len(titanic_data[(titanic_data.Survived == 1) & (titanic_data.Sex == 'female')])
survived_m = len(titanic_data[(titanic_data.Survived == 1) & (titanic_data.Sex == 'male')])
dead_f = len(titanic_data[(titanic_data.Survived == 0) & (titanic_data.Sex == 'female')])
dead_m = len(titanic_data[(titanic_data.Survived == 0) & (titanic_data.Sex == 'male')])
alive = [survived_f, survived_m]
dead = [dead_f, dead_m]

labels = ['female', 'male']
width = 0.35  # the width of the bars

fig, ax = plt.subplots()

ax.bar(labels, dead, width, bottom=alive, label='dead', color='salmon')
ax.bar(labels, alive, width, label='alive', color='mediumturquoise')
ax.set_ylabel('count')
ax.legend(bbox_to_anchor=(1.05, 1.0), loc='center left', title='How did it go?', labels=['alive', 'dead'])
plt.tight_layout()
plt.savefig('titanic_bar_plot.png')
plt.clf()""")

    elif assignment == '3.2.3':
        print("""data = load_wine()
wine_df = pd.DataFrame(data.data, columns=data.feature_names)
# print(wine_df)
plt.scatter(x=wine_df.malic_acid, y=wine_df.alcohol)
b, m = polyfit(wine_df.malic_acid, wine_df.alcohol, 1)
plt.plot(wine_df.malic_acid, b + m * wine_df.malic_acid, '-', color='k')
plt.xlabel('malic_acid', fontsize=20)
plt.ylabel('alcohol', fontsize=20)
plt.tight_layout()
plt.savefig('wine_scatter_plot.png')
plt.clf()""")
    elif assignment == '3.2.4':
        print("""fig, axes = plt.subplots(1, 2, figsize=(15, 5))
fig.suptitle('Making a subplot')

# heatmap
cor_wine = wine_df.corr()
sns.heatmap(cor_wine, ax=axes[0])
axes[0].set_title('heatmap')

# kdeplot
sns.kdeplot(x=wine_df.alcohol, y=wine_df.color_intensity, ax=axes[1])
axes[1].set_title('kernel density estimate')

plt.savefig('wine_subplot.png')
plt.clf()
""")
    elif type(assignment) != str:
        print('please enter the assignment number as a string')
    else:
        print('this assignment is not incorporated in this cheat function')

cheat("3.2.1")