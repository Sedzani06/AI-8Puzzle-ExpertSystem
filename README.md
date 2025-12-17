# COM2128 Artificial Intelligence Assignment

This repository contains my submission for the COM2128 Fundamentals of Artificial Intelligence assignment. It includes implementations of intelligent search algorithms and a simple rule-based expert system.

## Table of Contents
- [1. Search Algorithms]
  - Breadth-First Search (BFS)
  - Depth-First Search (DFS)
  - A* Search (A-Star)
- [2. Expert System]
  - Learning Style Detection System
- [3. Technologies Used]
- [4. How to Run]
  
---

## 1. Search Algorithms

Implemented three search algorithms to solve the 8-puzzle problem:

### 1.a.i - Breadth-First Search (BFS)
- Explores puzzle states level-by-level
- Guaranteed to find the shortest solution
- May use a lot of memory for harder puzzles

### 1.a.ii - Depth-First Search (DFS)
- Explores one path deeply before backtracking
- Uses less memory
- May find a longer path or fail if the goal is far

### 1.a.iii - A* Search
- Combines actual moves made (g) and an estimate of remaining moves (h)
- Uses the Manhattan distance as the heuristic
- Fast and finds the shortest solution

---

## 2. Expert System

### 2.b - Rule-Based System for Learning Styles
- Asks the user 3 simple questions
- Suggests a suitable learning style (Visual, Auditory, Kinesthetic, etc.)
- Gives learning tips based on the result

---

## 3. Technologies Used
- Python 3.x
- No external libraries required
- VS Code for writing and testing

---

## 4. How to Run

you can run each file separately for better results
