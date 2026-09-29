import numpy as np

names = np.array(["Ali", "Dani", "Ahmed", "Sara", "Usman"])

marks = np.array([
    [78, 92, 65, 88, 71],   # Python
    [85, 95, 70, 91, 76],   # Math
    [69, 89, 60, 84, 73]    # AI
])

subjects = ["Python", "Math", "AI"]

# ---------- Part 1: Basic statistics ----------
subject_avg = marks.mean(axis=1)   # one result per subject (row)
subject_max = marks.max(axis=1)
subject_min = marks.min(axis=1)
overall_avg = marks.mean()

print("=== Part 1: Basic statistics ===")
for i in range(3):
    print(f"{subjects[i]}: avg={subject_avg[i]:.1f}, max={subject_max[i]}, min={subject_min[i]}")
print(f"Overall average: {overall_avg:.2f}")

# ---------- Part 2: Student analysis ----------
averages = marks.mean(axis=0)      # one result per student (column)

best = np.argmax(averages)         # index of the highest average
worst = np.argmin(averages)        # index of the lowest average

print("\n=== Part 2: Student analysis ===")
for name, avg in zip(names, averages):
    print(f"{name}: {avg:.2f}")
print(f"Highest: {names[best]} ({averages[best]:.2f})")
print(f"Lowest:  {names[worst]} ({averages[worst]:.2f})")

# ---------- Part 3: Filtering ----------
mask = averages >= 80              # array of True/False
print("\n=== Part 3: Students with average >= 80 ===")
print(names[mask])

# ---------- Part 4: Ranking ----------
order = np.argsort(averages)[::-1]  # argsort is low->high, [::-1] flips it

print("\n=== Part 4: Ranking ===")
for rank, i in enumerate(order, start=1):
    print(f"{rank}. {names[i]} - {averages[i]:.2f}")

# ---------- Part 5: Performance categories ----------
categories = np.where(
    averages >= 80, "Excellent",
    np.where(averages >= 70, "Good", "Needs Improvement")
)

print("\n=== Part 5: Categories ===")
for name, cat in zip(names, categories):
    print(f"{name}: {cat}")

# ---------- Part 6: Random data ----------
scores = np.random.randint(50, 101, size=5)   # 101 because the end is excluded

print("\n=== Part 6: Random scores ===")
print("Scores:", scores)
print("Mean:  ", scores.mean())
print("Median:", np.median(scores))
print("Std:   ", scores.std())