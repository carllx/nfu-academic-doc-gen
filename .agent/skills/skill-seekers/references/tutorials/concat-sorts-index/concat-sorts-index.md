# How To: Concat Sorts Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat sorts index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
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
df1 = DataFrame({'a': [1, 2, 3]}, index=['c', 'a', 'b'])
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'b': [1, 2]}, index=['a', 'b'])
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [2, 3, 1], 'b': [1, 2, None]}, index=['a', 'b', 'c'], columns=['a', 'b'])
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign expected = value

```python
expected = expected.loc[['c', 'a', 'b']]
```

### Step 6: Assign result = pd.concat(...)

```python
result = pd.concat([df1, df2], axis=1, sort=sort)
```


## Complete Example

```python
# Setup
# Fixtures: sort

# Workflow
df1 = DataFrame({'a': [1, 2, 3]}, index=['c', 'a', 'b'])
df2 = DataFrame({'b': [1, 2]}, index=['a', 'b'])
expected = DataFrame({'a': [2, 3, 1], 'b': [1, 2, None]}, index=['a', 'b', 'c'], columns=['a', 'b'])
if sort is False:
    expected = expected.loc[['c', 'a', 'b']]
with tm.assert_produces_warning(None):
    result = pd.concat([df1, df2], axis=1, sort=sort)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_sort.py:29 | Complexity: Intermediate | Last updated: 2026-06-02*