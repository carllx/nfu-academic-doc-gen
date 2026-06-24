# How To: Multiple Agg Funcs

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test multiple agg funcs

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: func, window_size, expected_vals
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([['A', 10, 20], ['A', 20, 30], ['A', 30, 40], ['B', 10, 30], ['B', 30, 40], ['B', 40, 80], ['B', 80, 90]], columns=['stock', 'low', 'high'])
```

### Step 2: Assign f = getattr(...)

```python
f = getattr(df.groupby('stock'), func)
```

### Step 3: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples([('A', 0), ('A', 1), ('A', 2), ('B', 3), ('B', 4), ('B', 5), ('B', 6)], names=['stock', None])
```

### Step 4: Assign columns = MultiIndex.from_tuples(...)

```python
columns = MultiIndex.from_tuples([('low', 'mean'), ('low', 'max'), ('high', 'mean'), ('high', 'min')])
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame(expected_vals, index=index, columns=columns)
```

### Step 6: Assign result = window.agg(...)

```python
result = window.agg({'low': ['mean', 'max'], 'high': ['mean', 'min']})
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign window = f(...)

```python
window = f(window_size)
```

### Step 9: Assign window = f(...)

```python
window = f()
```


## Complete Example

```python
# Setup
# Fixtures: func, window_size, expected_vals

# Workflow
df = DataFrame([['A', 10, 20], ['A', 20, 30], ['A', 30, 40], ['B', 10, 30], ['B', 30, 40], ['B', 40, 80], ['B', 80, 90]], columns=['stock', 'low', 'high'])
f = getattr(df.groupby('stock'), func)
if window_size:
    window = f(window_size)
else:
    window = f()
index = MultiIndex.from_tuples([('A', 0), ('A', 1), ('A', 2), ('B', 3), ('B', 4), ('B', 5), ('B', 6)], names=['stock', None])
columns = MultiIndex.from_tuples([('low', 'mean'), ('low', 'max'), ('high', 'mean'), ('high', 'min')])
expected = DataFrame(expected_vals, index=index, columns=columns)
result = window.agg({'low': ['mean', 'max'], 'high': ['mean', 'min']})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_api.py:307 | Complexity: Advanced | Last updated: 2026-06-02*