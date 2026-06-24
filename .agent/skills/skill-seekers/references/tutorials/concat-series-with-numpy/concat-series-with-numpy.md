# How To: Concat Series With Numpy

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test concat series with numpy

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: to_concat_dtypes, result_dtype
```

## Step-by-Step Guide

### Step 1: Assign s1 = pd.Series(...)

```python
s1 = pd.Series([0, 1, pd.NA], dtype=to_concat_dtypes[0])
```

### Step 2: Assign s2 = pd.Series(...)

```python
s2 = pd.Series(np.array([0, 1], dtype=to_concat_dtypes[1]))
```

### Step 3: Assign result = pd.concat(...)

```python
result = pd.concat([s1, s2], ignore_index=True)
```

### Step 4: Assign expected = pd.Series.astype(...)

```python
expected = pd.Series([0, 1, pd.NA, 0, 1], dtype=object).astype(result_dtype)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = pd.concat(...)

```python
result = pd.concat([s2, s1], ignore_index=True)
```

### Step 7: Assign expected = pd.Series.astype(...)

```python
expected = pd.Series([0, 1, 0, 1, pd.NA], dtype=object).astype(result_dtype)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: to_concat_dtypes, result_dtype

# Workflow
s1 = pd.Series([0, 1, pd.NA], dtype=to_concat_dtypes[0])
s2 = pd.Series(np.array([0, 1], dtype=to_concat_dtypes[1]))
result = pd.concat([s1, s2], ignore_index=True)
expected = pd.Series([0, 1, pd.NA, 0, 1], dtype=object).astype(result_dtype)
tm.assert_series_equal(result, expected)
result = pd.concat([s2, s1], ignore_index=True)
expected = pd.Series([0, 1, 0, 1, pd.NA], dtype=object).astype(result_dtype)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_concat.py:56 | Complexity: Advanced | Last updated: 2026-06-02*