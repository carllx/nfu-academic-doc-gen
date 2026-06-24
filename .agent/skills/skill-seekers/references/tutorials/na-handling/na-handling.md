# How To: Na Handling

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test na handling

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.reshape.tile`

**Setup Required:**
```python
# Fixtures: labels
```

## Step-by-Step Guide

### Step 1: Assign arr = np.arange(...)

```python
arr = np.arange(0, 0.75, 0.01)
```

### Step 2: Assign unknown = value

```python
arr[::3] = np.nan
```

### Step 3: Assign result = cut(...)

```python
result = cut(arr, 4, labels=labels)
```

### Step 4: Assign result = np.asarray(...)

```python
result = np.asarray(result)
```

### Step 5: Assign expected = np.where(...)

```python
expected = np.where(isna(arr), np.nan, result)
```

### Step 6: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: labels

# Workflow
arr = np.arange(0, 0.75, 0.01)
arr[::3] = np.nan
result = cut(arr, 4, labels=labels)
result = np.asarray(result)
expected = np.where(isna(arr), np.nan, result)
tm.assert_almost_equal(result, expected)
```

## Next Steps


---

*Source: test_cut.py:257 | Complexity: Intermediate | Last updated: 2026-06-02*