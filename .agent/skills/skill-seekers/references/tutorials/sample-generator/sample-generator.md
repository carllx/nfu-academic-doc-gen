# How To: Sample Generator

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sample generator

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.common`

**Setup Required:**
```python
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign obj = frame_or_series(...)

```python
obj = frame_or_series(np.arange(100))
```

**Verification:**
```python
assert not (result1.index.values == result2.index.values).all()
```

### Step 2: Assign rng = np.random.default_rng(...)

```python
rng = np.random.default_rng(2)
```

### Step 3: Assign result1 = obj.sample(...)

```python
result1 = obj.sample(n=50, random_state=rng)
```

### Step 4: Assign result2 = obj.sample(...)

```python
result2 = obj.sample(n=50, random_state=rng)
```

**Verification:**
```python
assert not (result1.index.values == result2.index.values).all()
```

### Step 5: Assign result1 = obj.sample(...)

```python
result1 = obj.sample(n=50, random_state=np.random.default_rng(11))
```

### Step 6: Assign result2 = obj.sample(...)

```python
result2 = obj.sample(n=50, random_state=np.random.default_rng(11))
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(result1, result2)
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
obj = frame_or_series(np.arange(100))
rng = np.random.default_rng(2)
result1 = obj.sample(n=50, random_state=rng)
result2 = obj.sample(n=50, random_state=rng)
assert not (result1.index.values == result2.index.values).all()
result1 = obj.sample(n=50, random_state=np.random.default_rng(11))
result2 = obj.sample(n=50, random_state=np.random.default_rng(11))
tm.assert_equal(result1, result2)
```

## Next Steps


---

*Source: test_sample.py:180 | Complexity: Intermediate | Last updated: 2026-06-02*