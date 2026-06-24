# How To: Forward Probability

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test forward probability

## Prerequisites

**Required Modules:**
- `pytest`
- `nltk.tag`
- `numpy.testing`
- `numpy.testing`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign unknown = hmm._market_hmm_example(...)

```python
model, states, symbols = hmm._market_hmm_example()
```

**Verification:**
```python
assert_array_almost_equal(fp, expected)
```

### Step 2: Assign seq = value

```python
seq = [('up', None), ('up', None)]
```

### Step 3: Assign expected = value

```python
expected = [[0.35, 0.02, 0.09], [0.1792, 0.0085, 0.0357]]
```

### Step 4: Assign fp = value

```python
fp = 2 ** model._forward_probability(seq)
```

### Step 5: Call assert_array_almost_equal()

```python
assert_array_almost_equal(fp, expected)
```


## Complete Example

```python
# Workflow
from numpy.testing import assert_array_almost_equal
model, states, symbols = hmm._market_hmm_example()
seq = [('up', None), ('up', None)]
expected = [[0.35, 0.02, 0.09], [0.1792, 0.0085, 0.0357]]
fp = 2 ** model._forward_probability(seq)
assert_array_almost_equal(fp, expected)
```

## Next Steps


---

*Source: test_hmm.py:24 | Complexity: Intermediate | Last updated: 2026-06-02*