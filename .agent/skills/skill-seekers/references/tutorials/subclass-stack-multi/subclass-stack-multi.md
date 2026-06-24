# How To: Subclass Stack Multi

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test subclass stack multi

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
exp = tm.SubclassedDataFrame([[10, 12], [11, 13], [20, 22], [21, 23], [30, 32], [31, 33], [40, 42], [41, 43]], index=MultiIndex.from_tuples(list(zip(list('AAAABBBB'), list('ccddccdd'), list('yzyzyzyz'))), names=['aaa', 'ccc', 'yyy']), columns=Index(['W', 'X'], name='www'))
```

### Step 3: Assign res = df.stack(...)

```python
res = df.stack(future_stack=True)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp)
```

### Step 5: Assign res = df.stack(...)

```python
res = df.stack('yyy', future_stack=True)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp)
```

### Step 7: Assign exp = tm.SubclassedDataFrame(...)

```python
exp = tm.SubclassedDataFrame([[10, 11], [12, 13], [20, 21], [22, 23], [30, 31], [32, 33], [40, 41], [42, 43]], index=MultiIndex.from_tuples(list(zip(list('AAAABBBB'), list('ccddccdd'), list('WXWXWXWX'))), names=['aaa', 'ccc', 'www']), columns=Index(['y', 'z'], name='yyy'))
```

### Step 8: Assign res = df.stack(...)

```python
res = df.stack('www', future_stack=True)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp)
```


## Complete Example

```python
# Workflow
df = tm.SubclassedDataFrame([[10, 11, 12, 13], [20, 21, 22, 23], [30, 31, 32, 33], [40, 41, 42, 43]], index=MultiIndex.from_tuples(list(zip(list('AABB'), list('cdcd'))), names=['aaa', 'ccc']), columns=MultiIndex.from_tuples(list(zip(list('WWXX'), list('yzyz'))), names=['www', 'yyy']))
exp = tm.SubclassedDataFrame([[10, 12], [11, 13], [20, 22], [21, 23], [30, 32], [31, 33], [40, 42], [41, 43]], index=MultiIndex.from_tuples(list(zip(list('AAAABBBB'), list('ccddccdd'), list('yzyzyzyz'))), names=['aaa', 'ccc', 'yyy']), columns=Index(['W', 'X'], name='www'))
res = df.stack(future_stack=True)
tm.assert_frame_equal(res, exp)
res = df.stack('yyy', future_stack=True)
tm.assert_frame_equal(res, exp)
exp = tm.SubclassedDataFrame([[10, 11], [12, 13], [20, 21], [22, 23], [30, 31], [32, 33], [40, 41], [42, 43]], index=MultiIndex.from_tuples(list(zip(list('AAAABBBB'), list('ccddccdd'), list('WXWXWXWX'))), names=['aaa', 'ccc', 'www']), columns=Index(['y', 'z'], name='yyy'))
res = df.stack('www', future_stack=True)
tm.assert_frame_equal(res, exp)
```

## Next Steps


---

*Source: test_subclass.py:239 | Complexity: Advanced | Last updated: 2026-06-02*