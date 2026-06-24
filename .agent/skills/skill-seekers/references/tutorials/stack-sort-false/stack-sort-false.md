# How To: Stack Sort False

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test stack sort false

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape`

**Setup Required:**
```python
# Fixtures: future_stack
```

## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = [[1, 2, 3.0, 4.0], [2, 3, 4.0, 5.0], [3, 4, np.nan, np.nan]]
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(data, columns=MultiIndex(levels=[['B', 'A'], ['x', 'y']], codes=[[0, 0, 1, 1], [0, 1, 0, 1]]))
```

### Step 3: Assign kwargs = value

```python
kwargs = {} if future_stack else {'sort': False}
```

### Step 4: Assign result = df.stack(...)

```python
result = df.stack(level=0, future_stack=future_stack, **kwargs)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign df = DataFrame(...)

```python
df = DataFrame(data, columns=MultiIndex.from_arrays([['B', 'B', 'A', 'A'], ['x', 'y', 'x', 'y']]))
```

### Step 7: Assign kwargs = value

```python
kwargs = {} if future_stack else {'sort': False}
```

### Step 8: Assign result = df.stack(...)

```python
result = df.stack(level=0, future_stack=future_stack, **kwargs)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign expected = DataFrame(...)

```python
expected = DataFrame({'x': [1.0, 3.0, 2.0, 4.0, 3.0, np.nan], 'y': [2.0, 4.0, 3.0, 5.0, 4.0, np.nan]}, index=MultiIndex.from_arrays([[0, 0, 1, 1, 2, 2], ['B', 'A', 'B', 'A', 'B', 'A']]))
```

### Step 11: Assign expected = DataFrame(...)

```python
expected = DataFrame({'x': [1.0, 3.0, 2.0, 4.0, 3.0], 'y': [2.0, 4.0, 3.0, 5.0, 4.0]}, index=MultiIndex.from_arrays([[0, 0, 1, 1, 2], ['B', 'A', 'B', 'A', 'B']]))
```


## Complete Example

```python
# Setup
# Fixtures: future_stack

# Workflow
data = [[1, 2, 3.0, 4.0], [2, 3, 4.0, 5.0], [3, 4, np.nan, np.nan]]
df = DataFrame(data, columns=MultiIndex(levels=[['B', 'A'], ['x', 'y']], codes=[[0, 0, 1, 1], [0, 1, 0, 1]]))
kwargs = {} if future_stack else {'sort': False}
result = df.stack(level=0, future_stack=future_stack, **kwargs)
if future_stack:
    expected = DataFrame({'x': [1.0, 3.0, 2.0, 4.0, 3.0, np.nan], 'y': [2.0, 4.0, 3.0, 5.0, 4.0, np.nan]}, index=MultiIndex.from_arrays([[0, 0, 1, 1, 2, 2], ['B', 'A', 'B', 'A', 'B', 'A']]))
else:
    expected = DataFrame({'x': [1.0, 3.0, 2.0, 4.0, 3.0], 'y': [2.0, 4.0, 3.0, 5.0, 4.0]}, index=MultiIndex.from_arrays([[0, 0, 1, 1, 2], ['B', 'A', 'B', 'A', 'B']]))
tm.assert_frame_equal(result, expected)
df = DataFrame(data, columns=MultiIndex.from_arrays([['B', 'B', 'A', 'A'], ['x', 'y', 'x', 'y']]))
kwargs = {} if future_stack else {'sort': False}
result = df.stack(level=0, future_stack=future_stack, **kwargs)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_stack_unstack.py:1528 | Complexity: Advanced | Last updated: 2026-06-02*