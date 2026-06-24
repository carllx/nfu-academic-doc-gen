# How To: Push Bumps Off Worst Hypothesis When Stack Is Full

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test push bumps off worst hypothesis when stack is full

## Prerequisites

**Required Modules:**
- `unittest`
- `collections`
- `math`
- `nltk.translate`
- `nltk.translate.stack_decoder`


## Step-by-Step Guide

### Step 1: Assign stack = _Stack(...)

```python
stack = _Stack(3)
```

### Step 2: Assign poor_hypothesis = _Hypothesis(...)

```python
poor_hypothesis = _Hypothesis(0.01)
```

### Step 3: Call stack.push()

```python
stack.push(_Hypothesis(0.2))
```

### Step 4: Call stack.push()

```python
stack.push(poor_hypothesis)
```

### Step 5: Call stack.push()

```python
stack.push(_Hypothesis(0.1))
```

### Step 6: Call stack.push()

```python
stack.push(_Hypothesis(0.3))
```

### Step 7: Call self.assertFalse()

```python
self.assertFalse(poor_hypothesis in stack)
```


## Complete Example

```python
# Workflow
stack = _Stack(3)
poor_hypothesis = _Hypothesis(0.01)
stack.push(_Hypothesis(0.2))
stack.push(poor_hypothesis)
stack.push(_Hypothesis(0.1))
stack.push(_Hypothesis(0.3))
self.assertFalse(poor_hypothesis in stack)
```

## Next Steps


---

*Source: test_stack_decoder.py:235 | Complexity: Intermediate | Last updated: 2026-06-02*