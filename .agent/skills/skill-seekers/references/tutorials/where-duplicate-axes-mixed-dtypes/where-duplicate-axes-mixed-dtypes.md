# How To: Where Duplicate Axes Mixed Dtypes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test where duplicate axes mixed dtypes

## Prerequisites

**Required Modules:**
- `datetime`
- `hypothesis`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas._testing._hypothesis`


## Step-by-Step Guide

### Step 1: Assign result = DataFrame(...)

```python
result = DataFrame(data=[[0, np.nan]], columns=Index(['A', 'A']))
```

### Step 2: Assign unknown = value

```python
index, columns = result.axes
```

### Step 3: Assign mask = DataFrame(...)

```python
mask = DataFrame(data=[[True, True]], columns=columns, index=index)
```

### Step 4: Assign a = result.astype.where(...)

```python
a = result.astype(object).where(mask)
```

### Step 5: Assign b = result.astype.where(...)

```python
b = result.astype('f8').where(mask)
```

### Step 6: Assign c = value

```python
c = result.T.where(mask.T).T
```

### Step 7: Assign d = result.where(...)

```python
d = result.where(mask)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(a.astype('f8'), b.astype('f8'))
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(b.astype('f8'), c.astype('f8'))
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(c.astype('f8'), d.astype('f8'))
```


## Complete Example

```python
# Workflow
result = DataFrame(data=[[0, np.nan]], columns=Index(['A', 'A']))
index, columns = result.axes
mask = DataFrame(data=[[True, True]], columns=columns, index=index)
a = result.astype(object).where(mask)
b = result.astype('f8').where(mask)
c = result.T.where(mask.T).T
d = result.where(mask)
tm.assert_frame_equal(a.astype('f8'), b.astype('f8'))
tm.assert_frame_equal(b.astype('f8'), c.astype('f8'))
tm.assert_frame_equal(c.astype('f8'), d.astype('f8'))
```

## Next Steps


---

*Source: test_where.py:898 | Complexity: Advanced | Last updated: 2026-06-02*