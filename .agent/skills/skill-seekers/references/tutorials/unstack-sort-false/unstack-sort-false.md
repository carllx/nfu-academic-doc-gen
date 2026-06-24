# How To: Unstack Sort False

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test unstack sort false

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
# Fixtures: frame_or_series, dtype
```

## Step-by-Step Guide

### Step 1: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples([('two', 'z', 'b'), ('two', 'y', 'a'), ('one', 'z', 'b'), ('one', 'y', 'a')])
```

### Step 2: Assign obj = frame_or_series(...)

```python
obj = frame_or_series(np.arange(1.0, 5.0), index=index, dtype=dtype)
```

### Step 3: Assign result = obj.unstack(...)

```python
result = obj.unstack(level=-1, sort=False)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1.0, np.nan], [np.nan, 2.0], [3.0, np.nan], [np.nan, 4.0]], columns=expected_columns, index=MultiIndex.from_tuples([('two', 'z'), ('two', 'y'), ('one', 'z'), ('one', 'y')]), dtype=dtype)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = obj.unstack(...)

```python
result = obj.unstack(level=[1, 2], sort=False)
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1.0, 2.0], [3.0, 4.0]], index=['two', 'one'], columns=expected_columns, dtype=dtype)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign expected_columns = MultiIndex.from_tuples(...)

```python
expected_columns = MultiIndex.from_tuples([(0, 'b'), (0, 'a')])
```

### Step 10: Assign expected_columns = value

```python
expected_columns = ['b', 'a']
```

### Step 11: Assign expected_columns = MultiIndex.from_tuples(...)

```python
expected_columns = MultiIndex.from_tuples([(0, 'z', 'b'), (0, 'y', 'a')])
```

### Step 12: Assign expected_columns = MultiIndex.from_tuples(...)

```python
expected_columns = MultiIndex.from_tuples([('z', 'b'), ('y', 'a')])
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series, dtype

# Workflow
index = MultiIndex.from_tuples([('two', 'z', 'b'), ('two', 'y', 'a'), ('one', 'z', 'b'), ('one', 'y', 'a')])
obj = frame_or_series(np.arange(1.0, 5.0), index=index, dtype=dtype)
result = obj.unstack(level=-1, sort=False)
if frame_or_series is DataFrame:
    expected_columns = MultiIndex.from_tuples([(0, 'b'), (0, 'a')])
else:
    expected_columns = ['b', 'a']
expected = DataFrame([[1.0, np.nan], [np.nan, 2.0], [3.0, np.nan], [np.nan, 4.0]], columns=expected_columns, index=MultiIndex.from_tuples([('two', 'z'), ('two', 'y'), ('one', 'z'), ('one', 'y')]), dtype=dtype)
tm.assert_frame_equal(result, expected)
result = obj.unstack(level=[1, 2], sort=False)
if frame_or_series is DataFrame:
    expected_columns = MultiIndex.from_tuples([(0, 'z', 'b'), (0, 'y', 'a')])
else:
    expected_columns = MultiIndex.from_tuples([('z', 'b'), ('y', 'a')])
expected = DataFrame([[1.0, 2.0], [3.0, 4.0]], index=['two', 'one'], columns=expected_columns, dtype=dtype)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_stack_unstack.py:1320 | Complexity: Advanced | Last updated: 2026-06-02*