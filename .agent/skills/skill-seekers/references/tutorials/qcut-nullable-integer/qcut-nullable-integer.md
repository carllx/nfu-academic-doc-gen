# How To: Qcut Nullable Integer

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test qcut nullable integer

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: q, any_numeric_ea_dtype
```

## Step-by-Step Guide

### Step 1: Assign arr = pd.array(...)

```python
arr = pd.array(np.arange(100), dtype=any_numeric_ea_dtype)
```

### Step 2: Assign unknown = value

```python
arr[::2] = pd.NA
```

### Step 3: Assign result = qcut(...)

```python
result = qcut(arr, q)
```

### Step 4: Assign expected = qcut(...)

```python
expected = qcut(arr.astype(float), q)
```

### Step 5: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: q, any_numeric_ea_dtype

# Workflow
arr = pd.array(np.arange(100), dtype=any_numeric_ea_dtype)
arr[::2] = pd.NA
result = qcut(arr, q)
expected = qcut(arr.astype(float), q)
tm.assert_categorical_equal(result, expected)
```

## Next Steps


---

*Source: test_qcut.py:298 | Complexity: Intermediate | Last updated: 2026-06-02*