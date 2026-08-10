# Python OOP — Polymorphism Final Boss

A practical Python project built to test and combine the core Object-Oriented Programming concepts learned throughout my Python study.

## Concepts Used

* Classes and Objects
* Constructors (`__init__`)
* Inheritance
* `super()`
* Encapsulation
* Private Attributes
* Getters and Setters
* Method Overriding
* Polymorphism
* Duck Typing
* `*args`
* `**kwargs`

## Project Overview

This project is a small RPG-style character system.

It includes:

* A base `Character` class
* `Warrior`, `Mage`, and `Archer` child classes
* Different attack behaviors for each character
* Health management with getters and setters
* Damage handling
* Character-specific resources such as stamina, mana, and arrows
* Flexible character information using `**kwargs`
* Variable attack effects using `*args`

## Example

Different characters can attack the same target in different ways:

```text
Warrior attacks with a sword
Mage casts a fireball
Archer shoots an arrow
```

The target's health is updated after each attack.

## Purpose

This project was created as the final practical challenge for the Python OOP fundamentals section, combining multiple concepts into one working program rather than practicing each concept separately.

## Next Step

The next topic is **Abstraction**, followed by a complete OOP project before moving into CSV and JSON projects.
