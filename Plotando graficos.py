import matplotlib.pyplot as plt
fig, ax = plt.subplots()
circle = plt.circle((0,0), 0.64, color='white')
lbls = ['Codar', 'Estudar', 'Comer', 'Dormir']

ax.pie([7,4,2,5],
       labels=lbls,
       autopct='%1.1f%%',
       pctdistance=.82)
ax.add_artist(circle)
ax.set_title('Donut_chart', fontsize=16)
plt.show()