import matplotlib.pyplot as plt
import logparser


def hitdict_creator(file):
  fileIn = open(file)
  dayHit = {}
  for line in fileIn:
    data = logparser.parser(line)
    day = data["time"].split(":")[0]
    if day not in dayHit:
      dayHit[day] = 1
    else:
      dayHit[day] += 1
  fileIn.close()
  return dayHit

day_hit = hitdict_creator('access.log')

y = list(day_hit.keys())
print(y)
w = list(day_hit.values())
plt.barh(y, w, height=.5, color='blue', linewidth=.1, edgecolor='black', align="edge")
for i, count in enumerate(w):
  plt.text(count+10, i, str(count), fontweight='bold')
plt.xlabel("HIT COUNT", color='green', fontweight='bold')
plt.ylabel("DATE", color="green", fontweight='bold')
plt.title("IP HIT CHART", color='red', fontweight='bold')
plt.grid()
plt.show()
