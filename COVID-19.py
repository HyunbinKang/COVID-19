from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

Countries = ["United States", "Spain", "Italy", "Germany", "France", "China", "Iran", "UK", "Turkey", "Switzerland",
             "Belgium", "Netherlands", "Canada", "Austria", "Portugal", "Brazil", "S.Korea"]
Total_Cases = [336907, 135032, 128948, 100232, 92839, 81708, 60500, 47806, 27069, 21652, 20814,
               18803, 15512, 12236, 11730, 11450, 10284]
death_Cases = [9624, 13055, 15887, 1591, 8078, 3331, 3739, 4934, 574, 734, 1632, 1867, 280, 220, 311, 491, 186]
death_rate = [2.86, 9.67, 12.32, 1.59, 8.7, 4.08, 6.18, 10.32, 2.12, 3.39, 7.84, 9.93, 1.81, 1.8, 2.65, 4.29, 1.81]
test = [1773366, 355000, 691461, 918460, 224254, 0, 186000, 195524, 181445, 162500, 70000, 75415, 330901, 111296, 91794,
      54824, 461233]


x = np.arange(len(Countries))
width = 0.45

fig, ax = plt.subplots()
case = ax.bar(x, Total_Cases, label='Total Cases')


ax.set_ylabel('The number of people')
ax.set_title('COVID-19(2020-04-06)')
ax.set_xticklabels(Countries)
ax.legend()


plt.plot(Countries, death_Cases, label='Death Cases', color='red', marker='.', linestyle='--')
ax.legend()

plt.xticks(rotation=- 45)

fig.tight_layout()

fig, ax = plt.subplots()
ax.plot(Countries, death_rate, label="death_rate", color='green')
ax.legend()

plt.xticks(rotation=- 45)
plt.title("Death rate of countries (2020-04-06)")
plt.ylabel('death rate %')

fig, ax = plt.subplots()
ax.bar(Countries, test, label="test", color='magenta')
ax.legend()

plt.xticks(rotation=- 45)
plt.title("The number of COVID-19 tests (2020-04-06)")
plt.ylabel('Tests')


plt.show()