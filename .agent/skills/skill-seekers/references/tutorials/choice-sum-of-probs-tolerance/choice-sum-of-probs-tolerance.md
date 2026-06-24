# How To: Choice Sum Of Probs Tolerance

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test choice sum of probs tolerance

## Prerequisites

**Required Modules:**
- `sys`
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`
- `gc`
- `gc`


## Step-by-Step Guide

### Step 1: Call random.seed()

```python
random.seed(1234)
```

**Verification:**
```python
assert_(c in a)
```

### Step 2: Assign a = value

```python
a = [1, 2, 3]
```

**Verification:**
```python
assert_raises(ValueError, random.choice, a, p=probs * 0.9)
```

### Step 3: Assign counts = value

```python
counts = [4, 4, 2]
```

### Step 4: Assign probs = value

```python
probs = np.array(counts, dtype=dt) / sum(counts)
```

### Step 5: Assign c = random.choice(...)

```python
c = random.choice(a, p=probs)
```

### Step 6: Call assert_()

```python
assert_(c in a)
```

### Step 7: Call assert_raises()

```python
assert_raises(ValueError, random.choice, a, p=probs * 0.9)
```


## Complete Example

```python
# Workflow
random.seed(1234)
a = [1, 2, 3]
counts = [4, 4, 2]
for dt in (np.float16, np.float32, np.float64):
    probs = np.array(counts, dtype=dt) / sum(counts)
    c = random.choice(a, p=probs)
    assert_(c in a)
    assert_raises(ValueError, random.choice, a, p=probs * 0.9)
```

## Next Steps


---

*Source: test_randomstate_regression.py:88 | Complexity: Intermediate | Last updated: 2026-06-02*