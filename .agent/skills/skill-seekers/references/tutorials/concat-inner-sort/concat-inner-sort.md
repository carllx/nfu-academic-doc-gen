# How To: Concat Inner Sort

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat inner sort

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
df1 = DataFrame({'a': [1, 2], 'b': [1, 2], 'c': [1, 2]}, columns=['b', 'a', 'c'])
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'a': [1, 2], 'b': [3, 4]}, index=[3, 4])
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'b': [1, 2, 3, 4], 'a': [1, 2, 1, 2]}, columns=['b', 'a'])
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = pd.concat(...)

```python
result = pd.concat([df1, df2], sort=sort, join='inner', ignore_index=True)
```

### Step 6: Assign expected = value

```python
expected = expected[['a', 'b']]
```


## Complete Example

```python
# Setup
# Fixtures: sort

# Workflow
df1 = DataFrame({'a': [1, 2], 'b': [1, 2], 'c': [1, 2]}, columns=['b', 'a', 'c'])
df2 = DataFrame({'a': [1, 2], 'b': [3, 4]}, index=[3, 4])
with tm.assert_produces_warning(None):
    result = pd.concat([df1, df2], sort=sort, join='inner', ignore_index=True)
expected = DataFrame({'b': [1, 2, 3, 4], 'a': [1, 2, 1, 2]}, columns=['b', 'a'])
if sort is True:
    expected = expected[['a', 'b']]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_sort.py:47 | Complexity: Intermediate | Last updated: 2026-06-02*