# How To: Expanding Skew Kurt Numerical Stability

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test expanding skew kurt numerical stability

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: method
```

## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(np.random.default_rng(2).random(10))
```

### Step 2: Assign expected = getattr(...)

```python
expected = getattr(s.expanding(3), method)()
```

### Step 3: Assign s = value

```python
s = s + 5000
```

### Step 4: Assign result = getattr(...)

```python
result = getattr(s.expanding(3), method)()
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: method

# Workflow
s = Series(np.random.default_rng(2).random(10))
expected = getattr(s.expanding(3), method)()
s = s + 5000
result = getattr(s.expanding(3), method)()
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_expanding.py:232 | Complexity: Intermediate | Last updated: 2026-06-02*