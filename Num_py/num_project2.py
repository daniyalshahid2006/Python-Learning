import numpy as np

# ---------------- DATA ----------------
products = np.array(["Laptop", "Phone", "Tablet", "Headphones", "Keyboard"])

sales = np.array([
    [12, 15, 10, 18],
    [25, 30, 28, 35],
    [18, 22, 20, 25],
    [40, 45, 38, 50],
    [30, 35, 32, 40]
])

prices = np.array([120000, 80000, 50000, 15000, 8000])
months = ["January", "February", "March", "April"]

# ---------------- PART 1: BASIC ANALYSIS ----------------
print("=== PART 1: BASIC ANALYSIS ===")
total_units = sales.sum(axis=1)
avg_monthly = sales.mean(axis=1)
highest_sale = sales.max()
lowest_sale = sales.min()

for product, total, avg in zip(products, total_units, avg_monthly):
    print(f"{product}: total = {total}, average/month = {avg:.2f}")
print("Highest single-month sale:", highest_sale)
print("Lowest single-month sale:", lowest_sale)

# ---------------- PART 2: REVENUE ----------------
print("\n=== PART 2: REVENUE ===")
revenue_per_product = total_units * prices
total_revenue = revenue_per_product.sum()
revenue_by_month = prices @ sales


for product, rev in zip(products, revenue_per_product):
    print(f"{product}: {rev:,}")
print("Total company revenue:", f"{total_revenue:,}")
for month, rev in zip(months, revenue_by_month):
    print(f"{month}: {rev:,}")

# ---------------- PART 3: BEST / WORST ----------------
print("\n=== PART 3: BEST / WORST ===")
best_selling = products[np.argmax(total_units)]
lowest_selling = products[np.argmin(total_units)]
highest_revenue = products[np.argmax(revenue_per_product)]

print("Best-selling product:", best_selling)
print("Lowest-selling product:", lowest_selling)
print("Highest-revenue product:", highest_revenue)

# ---------------- PART 4: FILTERING ----------------
print("\n=== PART 4: FILTERING ===")
min_units = 100
min_revenue = 5_000_000

mask_units = total_units > min_units
mask_revenue = revenue_per_product > min_revenue

print(f"Products with more than {min_units} units:", products[mask_units])
print(f"Products with revenue above {min_revenue:,}:", products[mask_revenue])

# ---------------- PART 5: RANKING ----------------
print("\n=== PART 5: RANKING ===")
units_order = np.argsort(total_units)[::-1]
revenue_order = np.argsort(revenue_per_product)[::-1]

print("Ranking by units sold:")
for rank, i in enumerate(units_order, start=1):
    print(f"{rank}. {products[i]} - {total_units[i]} units")

print("\nRanking by revenue:")
for rank, i in enumerate(revenue_order, start=1):
    print(f"{rank}. {products[i]} - {revenue_per_product[i]:,}")

# ---------------- PART 6: STATISTICS ----------------
print("\n=== PART 6: STATISTICS ===")
print("Overall mean:", sales.mean())
print("Overall median:", np.median(sales))
print("Overall std dev:", round(sales.std(), 2))

print("\nPer product:")
for product, m, med, s in zip(products, sales.mean(axis=1),
                              np.median(sales, axis=1), sales.std(axis=1)):
    print(f"{product}: mean = {m:.2f}, median = {med:.1f}, std = {s:.2f}")

# ---------------- PART 7: BROADCASTING ----------------
print("\n=== PART 7: BROADCASTING (10% DISCOUNT) ===")
discounted_prices = prices * 0.90
discounted_revenue_per_product = total_units * discounted_prices
discounted_total = discounted_revenue_per_product.sum()

print("Discounted prices:", discounted_prices)
for product, rev in zip(products, discounted_revenue_per_product):
    print(f"{product}: {rev:,.0f}")
print("Total discounted revenue:", f"{discounted_total:,.0f}")


print("\n=== PART 8: SIMULATED 5TH MONTH ===")
np.random.seed(42)
new_month = np.random.randint(10, 50, size=5)

sales_extended = np.column_stack((sales, new_month))  # add as a new column
months_extended = months + ["May"]

print("New month (May):", new_month)
print("Updated sales shape:", sales_extended.shape)   # (5, 5)
print(sales_extended)

# Re-run the analysis on the updated data
new_total_units = sales_extended.sum(axis=1)
new_revenue = new_total_units * prices
print("\nUpdated total units:", new_total_units)
print("Updated total revenue:", f"{new_revenue.sum():,}")