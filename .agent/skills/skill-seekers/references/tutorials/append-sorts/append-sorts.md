# How To: Append Sorts

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test append sorts

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `dateutil`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: sort
```

## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'a': [1, 2], 'b': [1, 2]}, columns=['b', 'a'])
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'a': [1, 2], 'c': [3, 4]}, index=[2, 3])
```

### Step 3: Assign result = df1._append(...)

```python
result = df1._append(df2, sort=sort)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'b': [1, 2, None, None], 'a': [1, 2, 1, 2], 'c': [None, None, 3, 4]}, columns=['a', 'b', 'c'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign expected = value

```python
expected = expected[['b', 'a', 'c']]
```


## Complete Example

```python
# Setup
# Fixtures: sort

# Workflow
df1 = DataFrame({'a': [1, 2], 'b': [1, 2]}, columns=['b', 'a'])
df2 = DataFrame({'a': [1, 2], 'c': [3, 4]}, index=[2, 3])
result = df1._append(df2, sort=sort)
expected = DataFrame({'b': [1, 2, None, None], 'a': [1, 2, 1, 2], 'c': [None, None, 3, 4]}, columns=['a', 'b', 'c'])
if sort is False:
    expected = expected[['b', 'a', 'c']]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_append.py:108 | Complexity: Intermediate | Last updated: 2026-06-02*