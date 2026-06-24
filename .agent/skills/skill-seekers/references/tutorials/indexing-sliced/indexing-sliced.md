# How To: Indexing Sliced

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test indexing sliced

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
df = tm.SubclassedDataFrame({'X': [1, 2, 3], 'Y': [4, 5, 6], 'Z': [7, 8, 9]}, index=['a', 'b', 'c'])
```

**Verification:**
```python
assert isinstance(res, tm.SubclassedSeries)
```

### Step 2: Assign res = value

```python
res = df.loc[:, 'X']
```

**Verification:**
```python
assert isinstance(res, tm.SubclassedSeries)
```

### Step 3: Assign exp = tm.SubclassedSeries(...)

```python
exp = tm.SubclassedSeries([1, 2, 3], index=list('abc'), name='X')
```

**Verification:**
```python
assert isinstance(res, tm.SubclassedSeries)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```

**Verification:**
```python
assert isinstance(res, tm.SubclassedSeries)
```

### Step 5: Assign res = value

```python
res = df.iloc[:, 1]
```

**Verification:**
```python
assert isinstance(res, tm.SubclassedSeries)
```

### Step 6: Assign exp = tm.SubclassedSeries(...)

```python
exp = tm.SubclassedSeries([4, 5, 6], index=list('abc'), name='Y')
```

**Verification:**
```python
assert isinstance(res, tm.SubclassedSeries)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```

**Verification:**
```python
assert isinstance(res, tm.SubclassedSeries)
```

### Step 8: Assign res = value

```python
res = df.loc[:, 'Z']
```

### Step 9: Assign exp = tm.SubclassedSeries(...)

```python
exp = tm.SubclassedSeries([7, 8, 9], index=list('abc'), name='Z')
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```

**Verification:**
```python
assert isinstance(res, tm.SubclassedSeries)
```

### Step 11: Assign res = value

```python
res = df.loc['a', :]
```

### Step 12: Assign exp = tm.SubclassedSeries(...)

```python
exp = tm.SubclassedSeries([1, 4, 7], index=list('XYZ'), name='a')
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```

**Verification:**
```python
assert isinstance(res, tm.SubclassedSeries)
```

### Step 14: Assign res = value

```python
res = df.iloc[1, :]
```

### Step 15: Assign exp = tm.SubclassedSeries(...)

```python
exp = tm.SubclassedSeries([2, 5, 8], index=list('XYZ'), name='b')
```

### Step 16: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```

**Verification:**
```python
assert isinstance(res, tm.SubclassedSeries)
```

### Step 17: Assign res = value

```python
res = df.loc['c', :]
```

### Step 18: Assign exp = tm.SubclassedSeries(...)

```python
exp = tm.SubclassedSeries([3, 6, 9], index=list('XYZ'), name='c')
```

### Step 19: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```

**Verification:**
```python
assert isinstance(res, tm.SubclassedSeries)
```


## Complete Example

```python
# Workflow
df = tm.SubclassedDataFrame({'X': [1, 2, 3], 'Y': [4, 5, 6], 'Z': [7, 8, 9]}, index=['a', 'b', 'c'])
res = df.loc[:, 'X']
exp = tm.SubclassedSeries([1, 2, 3], index=list('abc'), name='X')
tm.assert_series_equal(res, exp)
assert isinstance(res, tm.SubclassedSeries)
res = df.iloc[:, 1]
exp = tm.SubclassedSeries([4, 5, 6], index=list('abc'), name='Y')
tm.assert_series_equal(res, exp)
assert isinstance(res, tm.SubclassedSeries)
res = df.loc[:, 'Z']
exp = tm.SubclassedSeries([7, 8, 9], index=list('abc'), name='Z')
tm.assert_series_equal(res, exp)
assert isinstance(res, tm.SubclassedSeries)
res = df.loc['a', :]
exp = tm.SubclassedSeries([1, 4, 7], index=list('XYZ'), name='a')
tm.assert_series_equal(res, exp)
assert isinstance(res, tm.SubclassedSeries)
res = df.iloc[1, :]
exp = tm.SubclassedSeries([2, 5, 8], index=list('XYZ'), name='b')
tm.assert_series_equal(res, exp)
assert isinstance(res, tm.SubclassedSeries)
res = df.loc['c', :]
exp = tm.SubclassedSeries([3, 6, 9], index=list('XYZ'), name='c')
tm.assert_series_equal(res, exp)
assert isinstance(res, tm.SubclassedSeries)
```

## Next Steps


---

*Source: test_subclass.py:115 | Complexity: Advanced | Last updated: 2026-06-02*