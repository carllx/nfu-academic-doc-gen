# How To: Backward Probability

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test backward probability

## Prerequisites

**Required Modules:**
- `pytest`
- `nltk.tag`
- `numpy.testing`
- `numpy.testing`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign unknown = _wikipedia_example_hmm(...)

```python
model, states, symbols, seq = _wikipedia_example_hmm()
```

**Verification:**
```python
assert_array_almost_equal(wikipedia_results, bp, 4)
```

### Step 2: Assign bp = value

```python
bp = 2 ** model._backward_probability(seq)
```

### Step 3: Assign bp = value

```python
bp = (bp.T / bp.sum(axis=1)).T
```

### Step 4: Assign wikipedia_results = value

```python
wikipedia_results = [[0.5923, 0.4077], [0.3763, 0.6237], [0.6533, 0.3467], [0.6273, 0.3727], [0.5, 0.5]]
```

### Step 5: Call assert_array_almost_equal()

```python
assert_array_almost_equal(wikipedia_results, bp, 4)
```


## Complete Example

```python
# Workflow
from numpy.testing import assert_array_almost_equal
model, states, symbols, seq = _wikipedia_example_hmm()
bp = 2 ** model._backward_probability(seq)
bp = (bp.T / bp.sum(axis=1)).T
wikipedia_results = [[0.5923, 0.4077], [0.3763, 0.6237], [0.6533, 0.3467], [0.6273, 0.3727], [0.5, 0.5]]
assert_array_almost_equal(wikipedia_results, bp, 4)
```

## Next Steps


---

*Source: test_hmm.py:57 | Complexity: Intermediate | Last updated: 2026-06-02*