# How To: Forward Probability2

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test forward probability2

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
assert_array_almost_equal(wikipedia_results, fp, 4)
```

### Step 2: Assign fp = value

```python
fp = 2 ** model._forward_probability(seq)
```

### Step 3: Assign fp = value

```python
fp = (fp.T / fp.sum(axis=1)).T
```

### Step 4: Assign wikipedia_results = value

```python
wikipedia_results = [[0.8182, 0.1818], [0.8834, 0.1166], [0.1907, 0.8093], [0.7308, 0.2692], [0.8673, 0.1327]]
```

### Step 5: Call assert_array_almost_equal()

```python
assert_array_almost_equal(wikipedia_results, fp, 4)
```


## Complete Example

```python
# Workflow
from numpy.testing import assert_array_almost_equal
model, states, symbols, seq = _wikipedia_example_hmm()
fp = 2 ** model._forward_probability(seq)
fp = (fp.T / fp.sum(axis=1)).T
wikipedia_results = [[0.8182, 0.1818], [0.8834, 0.1166], [0.1907, 0.8093], [0.7308, 0.2692], [0.8673, 0.1327]]
assert_array_almost_equal(wikipedia_results, fp, 4)
```

## Next Steps


---

*Source: test_hmm.py:37 | Complexity: Intermediate | Last updated: 2026-06-02*