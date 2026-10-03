# Sales Data Analyzer

A NumPy-based project that analyzes product sales data across multiple months. It calculates sales statistics, revenue, rankings, filtering results, and simulated future sales data.

## Features

* Calculate total units sold for each product
* Calculate average monthly sales
* Find highest and lowest sales
* Calculate revenue for each product
* Calculate total revenue
* Analyze monthly revenue
* Find best- and worst-selling products
* Filter products using NumPy boolean indexing
* Rank products using `np.argsort()`
* Calculate mean, median, and standard deviation
* Apply discounts using NumPy broadcasting
* Generate simulated sales data using NumPy random functions

## Technologies Used

* Python
* NumPy

## Data

The project analyzes five products:

* Laptop
* Phone
* Tablet
* Headphones
* Keyboard

Sales data is recorded across four months:

* January
* February
* March
* April

## NumPy Concepts Used

* NumPy arrays
* `axis`
* `sum()`
* `mean()`
* `min()`
* `max()`
* `median()`
* `std()`
* `argmax()`
* `argmin()`
* `argsort()`
* Boolean indexing
* `np.where()`
* Broadcasting
* `np.random`
* Array manipulation

## Example

Example sales data:

```text
Laptop       12  15  10  18
Phone        25  30  28  35
Tablet       18  22  20  25
Headphones   40  45  38  50
Keyboard     30  35  32  40
```

Example output:

```text
Laptop total: 55
Phone total: 118
Tablet total: 85
Headphones total: 173
Keyboard total: 137
```

The program then uses this data to perform further sales and revenue analysis.

## Purpose

This project was created as a practical exercise to apply NumPy concepts to a realistic data-analysis problem.

## How to Run

Make sure NumPy is installed:

```bash
pip install numpy
```

Then run:

```bash
python sales_analyzer.py
```
