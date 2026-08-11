# Python OOP — Final Boss

## Overview

A complete RPG battle system built to demonstrate core Object-Oriented Programming concepts in Python.

## OOP Concepts Used

* Classes and Objects
* Inheritance
* `super()`
* Encapsulation
* Private attributes
* Getters and Setters
* Method Overriding
* Polymorphism
* Duck Typing
* Abstraction
* `ABC`
* `@abstractmethod`
* `*args`
* `**kwargs`

## Characters

The battle system contains three character types:

* Warrior
* Mage
* Archer

Each character has its own resources and abilities.

### Warrior

* Uses stamina
* Light attack
* Special attack with bleeding bonus

### Mage

* Uses mana
* Magic attack
* Fireball with burning bonus

### Archer

* Uses arrows
* Normal arrow attack
* Critical attack

## Battle Rules

* Health is limited between 0 and 100.
* Characters cannot attack themselves.
* Dead characters cannot be attacked.
* Characters consume their resources when using attacks.
* Different character types implement their own `attack()` behavior.

## Sample Run

```text
Warrior attacks Mage
Mage attacks Warrior with mana blast
Warrior uses a special attack on Archer
Mage attacks Warrior with a fire ball
Archer attacks Warrior with arrows
Archer attacks Warrior with crit

Character health and resource statistics are displayed throughout the battle.
```

## Purpose

This project serves as the final core-OOP challenge before moving into file-based projects using CSV and JSON.
