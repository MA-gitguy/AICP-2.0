#_____1
import matplotlib.pyplot as plt

x = [1.0, 2.0, 3.0]
y = [2.0, 4.0, 1.0]

plt.plot(x, y)

plt.title("Graph Chart")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.xlim([1.0, 3.0])
plt.ylim([1.0, 4.0])

plt.xticks([1.0, 1.5, 2.0, 2.5, 3.0])
plt.yticks([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])

plt.show()

#______2
import matplotlib.pyplot as plt

xb = [10, 20, 30]
yb = [20, 40, 10]

xr = [10, 20, 30]
yr = [40, 10, 30]

plt.plot(xb, yb, label="Blue Line", color="blue", linewidth=3)
plt.plot(xr, yr, label="Red Line", color="red", linewidth=5)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Two Different Lines")

plt.xticks([10, 15, 20, 25, 30])
plt.yticks([10, 15, 20, 30, 35, 40])

plt.xlim(10, 30)
plt.ylim(10, 40)

plt.legend(["line1-width=3", "line2-width=5"])

plt.show()


#________3
import matplotlib.pyplot as plt

x = [1, 4, 5, 6, 7]
y = [2, 6, 3, 6, 3]

plt.plot(x, y, color="red", marker="." ,linestyle="dotted", markerfacecolor="blue",
         markeredgecolor="blue", markersize=20)

plt.title("Display Marker")
plt.xticks([1,2,3,4,5,6,7,8])
plt.yticks([1,2,3,4,5,6,7,8])

plt.xlim([1, 8])
plt.ylim([1, 8])

plt.show()

#______4
import matplotlib.pyplot as plt

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.barh(languages, popularity, color="Green")
plt.title("Popularity Chart of PL")
plt.xlabel("Popularity")
plt.ylabel("Languages")

plt.grid(which="major", color="red", linestyle="-", alpha=0.7)
plt.minorticks_on()
plt.grid(which="minor", color="blue", linestyle=":", alpha=0.5)

plt.show()

#________5
import pandas as pd
import matplotlib.pyplot as plt

data = {'a': [2, 4, 6, 8, 10],
        'b': [8, 2, 4, 2, 4],
        'c': [5, 3, 7, 4, 3],
        'd': [7, 2, 4, 8, 3],
        'e': [6, 6, 8, 6, 2]}

df = pd.DataFrame(data, index=[2,4,6,8,10])

colors = ["blue", "green", "red", "cyan", "purple"]
df.plot(kind='bar', color=colors)
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Bar Plot from DataFrame')

plt.grid(which="major", color="red", linestyle="-", alpha=0.5)
plt.minorticks_on()
plt.grid(which="minor", color="blue", linestyle=":", alpha=0.3)


plt.show()

#_______6
import pandas as pd
import matplotlib.pyplot as plt

file_path = "notebooks/DATA.csv"

df = pd.read_csv(file_path)

countries = df["country"]
gold_medals = df["gold"]

plt.pie(gold_medals, labels=countries, autopct='%1.1f%%', startangle=140)
plt.title("Gold Medal/Country")

plt.show()


#________7
import matplotlib.pyplot as plt

science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]

plt.scatter(marks_range, math_marks, color="green", label="Maths Marks")
plt.scatter(marks_range, science_marks, color="red", label="Science Marks")

plt.xlabel('Marks Range')
plt.ylabel('Marks Scored')
plt.title('Scatter Plot')

plt.xlim([0, 120])
plt.legend()
plt.show()


















