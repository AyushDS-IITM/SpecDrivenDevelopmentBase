# Simple Todo App

## What This App Does

Simple Todo App is a beginner-friendly web app for keeping track of tasks.
You can add a todo, mark it as complete, and delete it when you no longer need it.

This project can also be used as a small example for comparing **vibe coding**
with **spec driven development**.

## Features

- Add a new todo
- Mark a todo as complete
- Delete a todo
- Works in the browser with plain HTML, CSS, and JavaScript

## How To Run

Open `index.html` in your web browser.

## Vibe Coding vs Spec Driven Development

### Vibe Coding

Vibe coding is an exploratory way of building software where the developer
describes an idea, lets an AI assistant generate code, tries the result, and
keeps adjusting based on feel. It is useful when the goal is still forming or
when speed matters more than structure.

**Benefits**

- Fast for prototypes, demos, and experiments
- Helps explore ideas before all requirements are known
- Low setup cost for small projects
- Encourages quick iteration and creative discovery

**Cons**

- Requirements can stay vague, which may lead to missing behavior
- Code quality can become inconsistent without review or tests
- Harder to maintain as the project grows
- Bugs can hide because success is judged mostly by whether the result "feels right"

### Spec Driven Development

Spec driven development starts with a clear specification before implementation.
The expected behavior, constraints, user flows, edge cases, and acceptance
criteria are written down first. Code is then created to satisfy that spec.

**Benefits**

- Clear requirements before coding begins
- Easier to test because expected behavior is documented
- Better for collaboration, handoff, and long-term maintenance
- Reduces ambiguity when using AI-generated code
- Helps prevent scope creep by defining what is in and out of scope

**Cons**

- Slower to start than an exploratory approach
- Requires more upfront thinking and writing
- Specs can become outdated if they are not maintained
- May feel heavy for tiny throwaway experiments

## Key Difference

Vibe coding optimizes for exploration and speed. Spec driven development
optimizes for clarity, reliability, and maintainability.

For a small todo app, vibe coding might be enough to quickly create the first
version. Spec driven development becomes more valuable when the app needs
defined behavior, tests, collaboration, or future changes.
