# How To: Numba Numeric Colnames

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test numba numeric colnames

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.util.version`

**Setup Required:**
```python
# Fixtures: colnames
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.int64), columns=colnames)
```

### Step 2: Assign first_col = value

```python
first_col = colnames[0]
```

### Step 3: Assign f = value

```python
f = lambda x: x[first_col]
```

### Step 4: Assign result = df.apply(...)

```python
result = df.apply(f, engine='numba', axis=1)
```

### Step 5: Assign expected = df.apply(...)

```python
expected = df.apply(f, engine='python', axis=1)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: colnames

# Workflow
df = DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.int64), columns=colnames)
first_col = colnames[0]
f = lambda x: x[first_col]
result = df.apply(f, engine='numba', axis=1)
expected = df.apply(f, engine='python', axis=1)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_numba.py:81 | Complexity: Intermediate | Last updated: 2026-06-02*