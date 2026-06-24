# How To: Infer Objects

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test infer objects

## Prerequisites

**Required Modules:**
- `datetime`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': ['a', 1, 2, 3], 'b': ['b', 2.0, 3.0, 4.1], 'c': ['c', datetime(2016, 1, 1), datetime(2016, 1, 2), datetime(2016, 1, 3)], 'd': [1, 2, 3, 'd']}, columns=['a', 'b', 'c', 'd'])
```

**Verification:**
```python
assert df['a'].dtype == 'int64'
```

### Step 2: Assign df = unknown.infer_objects(...)

```python
df = df.iloc[1:].infer_objects()
```

**Verification:**
```python
assert df['b'].dtype == 'float64'
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1, 2, 3], 'b': [2.0, 3.0, 4.1], 'c': [datetime(2016, 1, 1), datetime(2016, 1, 2), datetime(2016, 1, 3)], 'd': [2, 3, 'd']}, columns=['a', 'b', 'c', 'd'])
```

**Verification:**
```python
assert df['c'].dtype == 'M8[ns]'
```

### Step 4: Assign result = df.reset_index(...)

```python
result = df.reset_index(drop=True)
```

**Verification:**
```python
assert df['d'].dtype == 'object'
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': ['a', 1, 2, 3], 'b': ['b', 2.0, 3.0, 4.1], 'c': ['c', datetime(2016, 1, 1), datetime(2016, 1, 2), datetime(2016, 1, 3)], 'd': [1, 2, 3, 'd']}, columns=['a', 'b', 'c', 'd'])
df = df.iloc[1:].infer_objects()
assert df['a'].dtype == 'int64'
assert df['b'].dtype == 'float64'
assert df['c'].dtype == 'M8[ns]'
assert df['d'].dtype == 'object'
expected = DataFrame({'a': [1, 2, 3], 'b': [2.0, 3.0, 4.1], 'c': [datetime(2016, 1, 1), datetime(2016, 1, 2), datetime(2016, 1, 3)], 'd': [2, 3, 'd']}, columns=['a', 'b', 'c', 'd'])
result = df.reset_index(drop=True)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_infer_objects.py:8 | Complexity: Intermediate | Last updated: 2026-06-02*