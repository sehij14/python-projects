# Day 32 — Workforce Management System

Today I built on what I learned with classes and went a step further — instance variables vs class variables, and instance methods vs class methods. Wanted to actually see the difference in something useful instead of just toy examples, so I made a basic workforce management system.

## What it does

It lets you:
- Add an employee (ID, name, department, salary)
- Display all employees that are currently added.
- Change the company name for ALL employees at once.
- Exit.

## The concept I was trying to nail down

Instance variables = unique to each object (like employee_id, name, salary — every employee has their own).

Class variable = shared across every object of that class. So `company_name` belongs to the Employee class itself, not to one employee. That's why changing it through `change_company_name` updates it everywhere, for every employee, instantly — because they're all pointing to the same class-level value.

Instance method = needs `self`, works with that one object's data (`display_employee`).

Class method = needs `cls` instead of `self`, it is a method that works with the class itself, instead of object data. That's the `@classmethod` decorator doing its thing on `change_company_name`.

Honestly the class variable part confused me a bit at first because in my head every employee should have "their own" company name, but then I realized — no, that's literally the point. They all work for the same company, so it makes sense that's shared, not individual. Once that clicked it made a lot more sense why you'd even want a class variable in the first place.

## Things I'd add later
- Saving employees to a file so they don't disappear when the program closes.
- Maybe a search/edit option for an existing employee.
- Input validation for negative salary.
