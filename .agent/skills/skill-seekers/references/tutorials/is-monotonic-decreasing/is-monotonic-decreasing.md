# How To: Is Monotonic Decreasing

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test is monotonic decreasing

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: in_vals, out_vals
```

## Step-by-Step Guide

### Step 1: Assign source_dict = value

```python
source_dict = {'A': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'], 'B': ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd'], 'C': in_vals}
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(source_dict)
```

### Step 3: Assign result = value

```python
result = df.groupby('B').C.is_monotonic_decreasing
```

### Step 4: Assign index = Index(...)

```python
index = Index(list('abcd'), name='B')
```

### Step 5: Assign expected = Series(...)

```python
expected = Series(index=index, data=out_vals, name='C')
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: in_vals, out_vals

# Workflow
source_dict = {'A': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'], 'B': ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd'], 'C': in_vals}
df = DataFrame(source_dict)
result = df.groupby('B').C.is_monotonic_decreasing
index = Index(list('abcd'), name='B')
expected = Series(index=index, data=out_vals, name='C')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_is_monotonic.py:66 | Complexity: Intermediate | Last updated: 2026-06-02*