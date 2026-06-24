# How To: Join Empty

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test join empty

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: left_empty, how, exp
```

## Step-by-Step Guide

### Step 1: Assign left = DataFrame.set_index(...)

```python
left = DataFrame({'A': [2, 1], 'B': [3, 4]}, dtype='int64').set_index('A')
```

### Step 2: Assign right = DataFrame.set_index(...)

```python
right = DataFrame({'A': [1], 'C': [5]}, dtype='int64').set_index('A')
```

### Step 3: Assign result = left.join(...)

```python
result = left.join(right, how=how)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign left = left.head(...)

```python
left = left.head(0)
```

### Step 6: Assign right = right.head(...)

```python
right = right.head(0)
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [2, 1], 'B': [3, 4], 'C': [np.nan, np.nan]})
```

### Step 8: Assign expected = expected.set_index(...)

```python
expected = expected.set_index('A')
```

### Step 9: Assign expected = expected.sort_index(...)

```python
expected = expected.sort_index()
```

### Step 10: Assign expected = DataFrame(...)

```python
expected = DataFrame({'B': [np.nan], 'A': [1], 'C': [5]})
```

### Step 11: Assign expected = expected.set_index(...)

```python
expected = expected.set_index('A')
```

### Step 12: Assign expected = DataFrame(...)

```python
expected = DataFrame(columns=['B', 'C'], dtype='int64')
```

### Step 13: Assign expected = expected.rename_axis(...)

```python
expected = expected.rename_axis('A')
```


## Complete Example

```python
# Setup
# Fixtures: left_empty, how, exp

# Workflow
left = DataFrame({'A': [2, 1], 'B': [3, 4]}, dtype='int64').set_index('A')
right = DataFrame({'A': [1], 'C': [5]}, dtype='int64').set_index('A')
if left_empty:
    left = left.head(0)
else:
    right = right.head(0)
result = left.join(right, how=how)
if exp == 'left':
    expected = DataFrame({'A': [2, 1], 'B': [3, 4], 'C': [np.nan, np.nan]})
    expected = expected.set_index('A')
elif exp == 'right':
    expected = DataFrame({'B': [np.nan], 'A': [1], 'C': [5]})
    expected = expected.set_index('A')
elif exp == 'empty':
    expected = DataFrame(columns=['B', 'C'], dtype='int64')
    if how != 'cross':
        expected = expected.rename_axis('A')
if how == 'outer':
    expected = expected.sort_index()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_join.py:1024 | Complexity: Advanced | Last updated: 2026-06-02*