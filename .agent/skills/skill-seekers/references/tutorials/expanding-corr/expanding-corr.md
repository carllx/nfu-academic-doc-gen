# How To: Expanding Corr

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test expanding corr

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: series
```

## Step-by-Step Guide

### Step 1: Assign A = series.dropna(...)

```python
A = series.dropna()
```

### Step 2: Assign B = value

```python
B = (A + np.random.default_rng(2).standard_normal(len(A)))[:-5]
```

### Step 3: Assign result = A.expanding.corr(...)

```python
result = A.expanding().corr(B)
```

### Step 4: Assign rolling_result = A.rolling.corr(...)

```python
rolling_result = A.rolling(window=len(A), min_periods=1).corr(B)
```

### Step 5: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(rolling_result, result)
```


## Complete Example

```python
# Setup
# Fixtures: series

# Workflow
A = series.dropna()
B = (A + np.random.default_rng(2).standard_normal(len(A)))[:-5]
result = A.expanding().corr(B)
rolling_result = A.rolling(window=len(A), min_periods=1).corr(B)
tm.assert_almost_equal(rolling_result, result)
```

## Next Steps


---

*Source: test_expanding.py:267 | Complexity: Intermediate | Last updated: 2026-06-02*