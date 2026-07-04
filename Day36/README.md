# Day 36
## Smart Expense Analytics Tracker

---

Built a Smart Expense Tracker that doesn't just store your expenses but also analyzes them. 

I originally started this project as a normal expense tracker, but while building it I realised simply storing expenses is not very useful unless the data can also be analyzed properly.

So instead of stopping at basic expense storage, I expanded the project into a small financial analytics tool that processes spending patterns and generates insights from the data. 


## The application allows user to:
- record expenses
- organize them by category
- track weekly and monthly spending
- generate analytics summaries
- identify the highest spending category
- detect the most expensive tranaction


It's not just "store data and print it" — this time the program actually *processes* the data and tells you something useful about it. 

---

## What the project does

You can add expenses with a title, category, amount, and by period whether it's weekly or monthly. Once you've added a few, you can generate a full analytics report that shows total spending, category-wise breakdown, highest spending category, biggest single expense, and an overall spending insight.

It's the kind of output you'd expect from a basic finance app.

---

## Ideal Output

```SMART EXPENSE ANALYTICS TRACKER
1. Add Expense
2. View All Expenses
3. Generate Analytics Report
4. Exit

Enter choice: 1

Enter expense title: Pizza
Enter category: Food
Enter period (weekly/monthly): weekly
Enter amount: 450

Expense added successfully.
```

## The part I want to remember

```python
highest_category = max(category_totals, key=category_totals.get)
```

This line finds the category with the highest total spend.
`max()` with a `key` argument — I hadn't used it this way before, It's clean and short.

Also used a dictionary to build category totals on the fly inside the loop instead of pre-defining anything. That felt like proper data processing logic.

---

## Theory — what this connects to

**Financial Data Processing** is about taking raw numbers and turning them into information that means something — totals, breakdowns, comparisons, insights.

**Analytics Systems** (even at a beginner level) it follows a pattern:
- collect > store > process > report

**Aggregation** means combining multiple values into summarized results.

**Category Aggregation using Dictionaries** — instead of making separate variables for each category, the program builds totals dynamically as it reads through the data. 

That's exactly what this project does. add expense > store in list > loop and calculate > print the report.

The `try/except` around the amount input is also important because real systems don't crash when a user types something wrong. Handling bad input is part of building reliable software.

---

## file

`Day36_smart_expense_analytics_tracker.py`

---

*Day 36 *
*Started to write the code that actually thinks about the data, not just holds it.*
