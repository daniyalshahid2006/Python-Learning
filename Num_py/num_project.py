import numpy as np


names = np.array(["Ali", "Dani", "Ahmed", "Sara", "Usman"])

marks = np.array([
    [78, 92, 65, 88, 71],   # Python
    [85, 95, 70, 91, 76],   # Math
    [69, 89, 60, 84, 73]    # AI
])

subjects = ["Python", "Math", "AI"]

sub_avg = marks.mean(axis=1)
sub_max = marks.max(axis=1)
sub_min = marks.min(axis=1)
avg = marks.mean()

for i in range(3):
    print(f"{subjects[i]} avg: {sub_avg[i]:.2f}, max: {sub_max[i]:.2f}, min: {sub_min[i]:.2f}")
print("overall avg: ", avg)


averages = marks.mean(axis=0)

best = np.argmax(averages)
worst = np.argmin(averages)

for i in range(5):
    print(f"{names[i]} avg: {averages[i]:.2f}")

print(f"Best student: {names[best]} ({averages[best]:.2f})")
print(f"Worst student: {names[worst]} ({averages[worst]:.2f})")


mask = averages >= 80
print(names[mask])



order = np.argsort(averages)[::-1]
for i in order:
    print(f"{names[i]} avg: {averages[i]:.2f}")

categories = np.where(
    averages >= 80,
    "Excellent",
    np.where(averages >= 70, "Good", "Needs Improvement")
)

for i in range(5):
    print(f"{names[i]}: {averages[i]:.2f} - {categories[i]}")


scores = np.random.randint(50, 101, size=5)   # 101 because the end is excluded

print("\n=== Part 6: Random scores ===")
print("Scores:", scores)
print("Mean:  ", scores.mean())
print("Median:", np.median(scores))
print("Std:   ", scores.std())