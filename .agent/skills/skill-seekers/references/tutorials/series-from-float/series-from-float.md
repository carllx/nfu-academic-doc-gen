# How To: Series From Float

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series from float

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.arrays.floating`

**Setup Required:**
```python
# Fixtures: data
```

## Step-by-Step Guide

### Step 1: Assign dtype = value

```python
dtype = data.dtype
```

### Step 2: Assign expected = pd.Series(...)

```python
expected = pd.Series(data)
```

### Step 3: Assign result = pd.Series(...)

```python
result = pd.Series(data.to_numpy(na_value=np.nan, dtype='float'), dtype=str(dtype))
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign expected = pd.Series(...)

```python
expected = pd.Series(data)
```

### Step 6: Assign result = pd.Series(...)

```python
result = pd.Series(np.array(data).tolist(), dtype=str(dtype))
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: data

# Workflow
dtype = data.dtype
expected = pd.Series(data)
result = pd.Series(data.to_numpy(na_value=np.nan, dtype='float'), dtype=str(dtype))
tm.assert_series_equal(result, expected)
expected = pd.Series(data)
result = pd.Series(np.array(data).tolist(), dtype=str(dtype))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_construction.py:192 | Complexity: Intermediate | Last updated: 2026-06-02*