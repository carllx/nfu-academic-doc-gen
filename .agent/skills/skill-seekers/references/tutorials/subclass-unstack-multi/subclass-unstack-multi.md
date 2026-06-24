# How To: Subclass Unstack Multi

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test subclass unstack multi

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
df = tm.SubclassedDataFrame([[10, 11, 12, 13], [20, 21, 22, 23], [30, 31, 32, 33], [40, 41, 42, 43]], index=MultiIndex.from_tuples(list(zip(list('AABB'), list('cdcd'))), names=['aaa', 'ccc']), columns=MultiIndex.from_tuples(list(zip(list('WWXX'), list('yzyz'))), names=['www', 'yyy']))
```

### Step 2: Assign exp = tm.SubclassedDataFrame(...)

```python
exp = tm.SubclassedDataFrame([[10, 20, 11, 21, 12, 22, 13, 23], [30, 40, 31, 41, 32, 42, 33, 43]], index=Index(['A', 'B'], name='aaa'), columns=MultiIndex.from_tuples(list(zip(list('WWWWXXXX'), list('yyzzyyzz'), list('cdcdcdcd'))), names=['www', 'yyy', 'ccc']))
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
exp = tm.SubclassedDataFrame([[10, 30, 11, 31, 12, 32, 13, 33], [20, 40, 21, 41, 22, 42, 23, 43]], index=Index(['c', 'd'], name='ccc'), columns=MultiIndex.from_tuples(list(zip(list('WWWWXXXX'), list('yyzzyyzz'), list('ABABABAB'))), names=['www', 'yyy', 'aaa']))
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
df = tm.SubclassedDataFrame([[10, 11, 12, 13], [20, 21, 22, 23], [30, 31, 32, 33], [40, 41, 42, 43]], index=MultiIndex.from_tuples(list(zip(list('AABB'), list('cdcd'))), names=['aaa', 'ccc']), columns=MultiIndex.from_tuples(list(zip(list('WWXX'), list('yzyz'))), names=['www', 'yyy']))
exp = tm.SubclassedDataFrame([[10, 20, 11, 21, 12, 22, 13, 23], [30, 40, 31, 41, 32, 42, 33, 43]], index=Index(['A', 'B'], name='aaa'), columns=MultiIndex.from_tuples(list(zip(list('WWWWXXXX'), list('yyzzyyzz'), list('cdcdcdcd'))), names=['www', 'yyy', 'ccc']))
res = df.unstack()
tm.assert_frame_equal(res, exp)
res = df.unstack('ccc')
tm.assert_frame_equal(res, exp)
exp = tm.SubclassedDataFrame([[10, 30, 11, 31, 12, 32, 13, 33], [20, 40, 21, 41, 22, 42, 23, 43]], index=Index(['c', 'd'], name='ccc'), columns=MultiIndex.from_tuples(list(zip(list('WWWWXXXX'), list('yyzzyyzz'), list('ABABABAB'))), names=['www', 'yyy', 'aaa']))
res = df.unstack('aaa')
tm.assert_frame_equal(res, exp)
```

## Next Steps


---

*Source: test_subclass.py:373 | Complexity: Advanced | Last updated: 2026-06-02*