# How To: Group Shift With Fill Value

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test group shift with fill value

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign n_rows = 24

```python
n_rows = 24
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame([(i % 12, i % 3, i) for i in range(n_rows)], dtype=float, columns=['A', 'B', 'Z'], index=None)
```

### Step 3: Assign g = df.groupby(...)

```python
g = df.groupby(['A', 'B'])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([i + 12 if i < n_rows - 12 else 0 for i in range(n_rows)], dtype=float, columns=['Z'], index=None)
```

### Step 5: Assign result = g.shift(...)

```python
result = g.shift(-1, fill_value=0)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
n_rows = 24
df = DataFrame([(i % 12, i % 3, i) for i in range(n_rows)], dtype=float, columns=['A', 'B', 'Z'], index=None)
g = df.groupby(['A', 'B'])
expected = DataFrame([i + 12 if i < n_rows - 12 else 0 for i in range(n_rows)], dtype=float, columns=['Z'], index=None)
result = g.shift(-1, fill_value=0)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_groupby_shift_diff.py:42 | Complexity: Intermediate | Last updated: 2026-06-02*