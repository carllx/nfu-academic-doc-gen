# How To: Concat Ignore Index

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat ignore index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `copy`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: sort
```

## Step-by-Step Guide

### Step 1: Assign frame1 = DataFrame(...)

```python
frame1 = DataFrame({'test1': ['a', 'b', 'c'], 'test2': [1, 2, 3], 'test3': [4.5, 3.2, 1.2]})
```

### Step 2: Assign frame2 = DataFrame(...)

```python
frame2 = DataFrame({'test3': [5.2, 2.2, 4.3]})
```

### Step 3: Assign frame1.index = Index(...)

```python
frame1.index = Index(['x', 'y', 'z'])
```

### Step 4: Assign frame2.index = Index(...)

```python
frame2.index = Index(['x', 'y', 'q'])
```

### Step 5: Assign v1 = concat(...)

```python
v1 = concat([frame1, frame2], axis=1, ignore_index=True, sort=sort)
```

### Step 6: Assign nan = value

```python
nan = np.nan
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame([[nan, nan, nan, 4.3], ['a', 1, 4.5, 5.2], ['b', 2, 3.2, 2.2], ['c', 3, 1.2, nan]], index=Index(['q', 'x', 'y', 'z']))
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(v1, expected)
```

### Step 9: Assign expected = value

```python
expected = expected.loc[['x', 'y', 'z', 'q']]
```


## Complete Example

```python
# Setup
# Fixtures: sort

# Workflow
frame1 = DataFrame({'test1': ['a', 'b', 'c'], 'test2': [1, 2, 3], 'test3': [4.5, 3.2, 1.2]})
frame2 = DataFrame({'test3': [5.2, 2.2, 4.3]})
frame1.index = Index(['x', 'y', 'z'])
frame2.index = Index(['x', 'y', 'q'])
v1 = concat([frame1, frame2], axis=1, ignore_index=True, sort=sort)
nan = np.nan
expected = DataFrame([[nan, nan, nan, 4.3], ['a', 1, 4.5, 5.2], ['b', 2, 3.2, 2.2], ['c', 3, 1.2, nan]], index=Index(['q', 'x', 'y', 'z']))
if not sort:
    expected = expected.loc[['x', 'y', 'z', 'q']]
tm.assert_frame_equal(v1, expected)
```

## Next Steps


---

*Source: test_index.py:20 | Complexity: Advanced | Last updated: 2026-06-02*