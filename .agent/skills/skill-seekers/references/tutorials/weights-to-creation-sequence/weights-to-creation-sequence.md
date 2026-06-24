# How To: Weights To Creation Sequence

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test weights to creation sequence

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.threshold`


## Step-by-Step Guide

### Step 1: Assign deg = value

```python
deg = [3, 2, 2, 1]
```

**Verification:**
```python
assert nxt.weights_to_creation_sequence(deg, with_labels=True) == [(3, 'd'), (1, 'd'), (2, 'd'), (0, 'd')]
```

### Step 2: Call nxt.weights_to_creation_sequence()

```python
nxt.weights_to_creation_sequence(deg, with_labels=True, compact=True)
```

**Verification:**
```python
assert nxt.weights_to_creation_sequence(deg, compact=True) == [4]
```


## Complete Example

```python
# Workflow
deg = [3, 2, 2, 1]
with pytest.raises(ValueError):
    nxt.weights_to_creation_sequence(deg, with_labels=True, compact=True)
assert nxt.weights_to_creation_sequence(deg, with_labels=True) == [(3, 'd'), (1, 'd'), (2, 'd'), (0, 'd')]
assert nxt.weights_to_creation_sequence(deg, compact=True) == [4]
```

## Next Steps


---

*Source: test_threshold.py:86 | Complexity: Beginner | Last updated: 2026-06-02*