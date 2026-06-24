# How To: Dataframe From Dict Of Series With Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dataframe from dict of series with dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`

**Setup Required:**
```python
# Fixtures: index
```

## Step-by-Step Guide

### Step 1: Assign s1 = Series(...)

```python
s1 = Series([1.0, 2.0, 3.0])
```

**Verification:**
```python
assert not np.shares_memory(arr_before, get_array(s1))
```

### Step 2: Assign s2 = Series(...)

```python
s2 = Series([4, 5, 6])
```

**Verification:**
```python
assert np.shares_memory(arr_before, arr_after)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'a': s1, 'b': s2}, index=index, dtype='int64', copy=False)
```

### Step 4: Assign arr_before = get_array(...)

```python
arr_before = get_array(df, 'a')
```

**Verification:**
```python
assert not np.shares_memory(arr_before, get_array(s1))
```

### Step 5: Assign unknown = 100

```python
df.iloc[0, 0] = 100
```

### Step 6: Assign arr_after = get_array(...)

```python
arr_after = get_array(df, 'a')
```

**Verification:**
```python
assert np.shares_memory(arr_before, arr_after)
```


## Complete Example

```python
# Setup
# Fixtures: index

# Workflow
s1 = Series([1.0, 2.0, 3.0])
s2 = Series([4, 5, 6])
df = DataFrame({'a': s1, 'b': s2}, index=index, dtype='int64', copy=False)
arr_before = get_array(df, 'a')
assert not np.shares_memory(arr_before, get_array(s1))
df.iloc[0, 0] = 100
arr_after = get_array(df, 'a')
assert np.shares_memory(arr_before, arr_after)
```

## Next Steps


---

*Source: test_constructors.py:325 | Complexity: Intermediate | Last updated: 2026-06-02*