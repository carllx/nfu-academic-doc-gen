# How To: Frame At With Duplicate Axes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test frame at with duplicate axes

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arr = np.random.default_rng.standard_normal.reshape(...)

```python
arr = np.random.default_rng(2).standard_normal(6).reshape(3, 2)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(arr, columns=['A', 'A'])
```

### Step 3: Assign result = value

```python
result = df.at[0, 'A']
```

### Step 4: Assign expected = unknown.copy(...)

```python
expected = df.iloc[0].copy()
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = value

```python
result = df.T.at['A', 0]
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign unknown = 2

```python
df.at[1, 'A'] = 2
```

### Step 9: Assign expected = Series(...)

```python
expected = Series([2.0, 2.0], index=['A', 'A'], name=1)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(df.iloc[1], expected)
```


## Complete Example

```python
# Workflow
arr = np.random.default_rng(2).standard_normal(6).reshape(3, 2)
df = DataFrame(arr, columns=['A', 'A'])
result = df.at[0, 'A']
expected = df.iloc[0].copy()
tm.assert_series_equal(result, expected)
result = df.T.at['A', 0]
tm.assert_series_equal(result, expected)
df.at[1, 'A'] = 2
expected = Series([2.0, 2.0], index=['A', 'A'], name=1)
tm.assert_series_equal(df.iloc[1], expected)
```

## Next Steps


---

*Source: test_scalar.py:137 | Complexity: Advanced | Last updated: 2026-06-02*