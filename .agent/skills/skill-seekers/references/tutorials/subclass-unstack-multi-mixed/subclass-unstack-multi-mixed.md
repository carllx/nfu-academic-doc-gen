# How To: Subclass Unstack Multi Mixed

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test subclass unstack multi mixed

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = tm.SubclassedDataFrame(...)

```python
df = tm.SubclassedDataFrame([[10, 11, 12.0, 13.0], [20, 21, 22.0, 23.0], [30, 31, 32.0, 33.0], [40, 41, 42.0, 43.0]], index=MultiIndex.from_tuples(list(zip(list('AABB'), list('cdcd'))), names=['aaa', 'ccc']), columns=MultiIndex.from_tuples(list(zip(list('WWXX'), list('yzyz'))), names=['www', 'yyy']))
```

### Step 2: Assign exp = tm.SubclassedDataFrame(...)

```python
exp = tm.SubclassedDataFrame([[10, 20, 11, 21, 12.0, 22.0, 13.0, 23.0], [30, 40, 31, 41, 32.0, 42.0, 33.0, 43.0]], index=Index(['A', 'B'], name='aaa'), columns=MultiIndex.from_tuples(list(zip(list('WWWWXXXX'), list('yyzzyyzz'), list('cdcdcdcd'))), names=['www', 'yyy', 'ccc']))
```

### Step 3: Assign res = df.unstack(...)

```python
res = df.unstack()
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp)
```

### Step 5: Assign res = df.unstack(...)

```python
res = df.unstack('ccc')
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp)
```

### Step 7: Assign exp = tm.SubclassedDataFrame(...)

```python
exp = tm.SubclassedDataFrame([[10, 30, 11, 31, 12.0, 32.0, 13.0, 33.0], [20, 40, 21, 41, 22.0, 42.0, 23.0, 43.0]], index=Index(['c', 'd'], name='ccc'), columns=MultiIndex.from_tuples(list(zip(list('WWWWXXXX'), list('yyzzyyzz'), list('ABABABAB'))), names=['www', 'yyy', 'aaa']))
```

### Step 8: Assign res = df.unstack(...)

```python
res = df.unstack('aaa')
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp)
```


## Complete Example

```python
# Workflow
df = tm.SubclassedDataFrame([[10, 11, 12.0, 13.0], [20, 21, 22.0, 23.0], [30, 31, 32.0, 33.0], [40, 41, 42.0, 43.0]], index=MultiIndex.from_tuples(list(zip(list('AABB'), list('cdcd'))), names=['aaa', 'ccc']), columns=MultiIndex.from_tuples(list(zip(list('WWXX'), list('yzyz'))), names=['www', 'yyy']))
exp = tm.SubclassedDataFrame([[10, 20, 11, 21, 12.0, 22.0, 13.0, 23.0], [30, 40, 31, 41, 32.0, 42.0, 33.0, 43.0]], index=Index(['A', 'B'], name='aaa'), columns=MultiIndex.from_tuples(list(zip(list('WWWWXXXX'), list('yyzzyyzz'), list('cdcdcdcd'))), names=['www', 'yyy', 'ccc']))
res = df.unstack()
tm.assert_frame_equal(res, exp)
res = df.unstack('ccc')
tm.assert_frame_equal(res, exp)
exp = tm.SubclassedDataFrame([[10, 30, 11, 31, 12.0, 32.0, 13.0, 33.0], [20, 40, 21, 41, 22.0, 42.0, 23.0, 43.0]], index=Index(['c', 'd'], name='ccc'), columns=MultiIndex.from_tuples(list(zip(list('WWWWXXXX'), list('yyzzyyzz'), list('ABABABAB'))), names=['www', 'yyy', 'aaa']))
res = df.unstack('aaa')
tm.assert_frame_equal(res, exp)
```

## Next Steps


---

*Source: test_subclass.py:412 | Complexity: Advanced | Last updated: 2026-06-02*