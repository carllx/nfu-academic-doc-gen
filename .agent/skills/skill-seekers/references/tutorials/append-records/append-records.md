# How To: Append Records

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test append records

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `dateutil`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arr1 = np.zeros(...)

```python
arr1 = np.zeros((2,), dtype='i4,f4,S10')
```

### Step 2: Assign unknown = value

```python
arr1[:] = [(1, 2.0, 'Hello'), (2, 3.0, 'World')]
```

### Step 3: Assign arr2 = np.zeros(...)

```python
arr2 = np.zeros((3,), dtype='i4,f4,S10')
```

### Step 4: Assign unknown = value

```python
arr2[:] = [(3, 4.0, 'foo'), (5, 6.0, 'bar'), (7.0, 8.0, 'baz')]
```

### Step 5: Assign df1 = DataFrame(...)

```python
df1 = DataFrame(arr1)
```

### Step 6: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(arr2)
```

### Step 7: Assign result = df1._append(...)

```python
result = df1._append(df2, ignore_index=True)
```

### Step 8: Assign expected = DataFrame(...)

```python
expected = DataFrame(np.concatenate((arr1, arr2)))
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
arr1 = np.zeros((2,), dtype='i4,f4,S10')
arr1[:] = [(1, 2.0, 'Hello'), (2, 3.0, 'World')]
arr2 = np.zeros((3,), dtype='i4,f4,S10')
arr2[:] = [(3, 4.0, 'foo'), (5, 6.0, 'bar'), (7.0, 8.0, 'baz')]
df1 = DataFrame(arr1)
df2 = DataFrame(arr2)
result = df1._append(df2, ignore_index=True)
expected = DataFrame(np.concatenate((arr1, arr2)))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_append.py:93 | Complexity: Advanced | Last updated: 2026-06-02*