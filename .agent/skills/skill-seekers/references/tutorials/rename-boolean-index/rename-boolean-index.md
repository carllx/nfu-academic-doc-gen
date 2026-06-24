# How To: Rename Boolean Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rename boolean index

## Prerequisites

**Required Modules:**
- `collections`
- `inspect`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.arange(15).reshape(3, 5), columns=[False, True, 2, 3, 4])
```

### Step 2: Assign mapper = value

```python
mapper = {0: 'foo', 1: 'bar', 2: 'bah'}
```

### Step 3: Assign res = df.rename(...)

```python
res = df.rename(index=mapper)
```

### Step 4: Assign exp = DataFrame(...)

```python
exp = DataFrame(np.arange(15).reshape(3, 5), columns=[False, True, 2, 3, 4], index=['foo', 'bar', 'bah'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.arange(15).reshape(3, 5), columns=[False, True, 2, 3, 4])
mapper = {0: 'foo', 1: 'bar', 2: 'bah'}
res = df.rename(index=mapper)
exp = DataFrame(np.arange(15).reshape(3, 5), columns=[False, True, 2, 3, 4], index=['foo', 'bar', 'bah'])
tm.assert_frame_equal(res, exp)
```

## Next Steps


---

*Source: test_rename.py:406 | Complexity: Intermediate | Last updated: 2026-06-02*