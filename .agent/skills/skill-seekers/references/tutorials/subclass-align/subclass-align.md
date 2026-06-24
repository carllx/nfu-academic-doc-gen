# How To: Subclass Align

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test subclass align

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df1 = tm.SubclassedDataFrame(...)

```python
df1 = tm.SubclassedDataFrame({'a': [1, 3, 5], 'b': [1, 3, 5]}, index=list('ACE'))
```

**Verification:**
```python
assert isinstance(res1, tm.SubclassedDataFrame)
```

### Step 2: Assign df2 = tm.SubclassedDataFrame(...)

```python
df2 = tm.SubclassedDataFrame({'c': [1, 2, 4], 'd': [1, 2, 4]}, index=list('ABD'))
```

**Verification:**
```python
assert isinstance(res2, tm.SubclassedDataFrame)
```

### Step 3: Assign unknown = df1.align(...)

```python
res1, res2 = df1.align(df2, axis=0)
```

**Verification:**
```python
assert isinstance(res1, tm.SubclassedSeries)
```

### Step 4: Assign exp1 = tm.SubclassedDataFrame(...)

```python
exp1 = tm.SubclassedDataFrame({'a': [1, np.nan, 3, np.nan, 5], 'b': [1, np.nan, 3, np.nan, 5]}, index=list('ABCDE'))
```

**Verification:**
```python
assert isinstance(res2, tm.SubclassedSeries)
```

### Step 5: Assign exp2 = tm.SubclassedDataFrame(...)

```python
exp2 = tm.SubclassedDataFrame({'c': [1, 2, np.nan, 4, np.nan], 'd': [1, 2, np.nan, 4, np.nan]}, index=list('ABCDE'))
```

**Verification:**
```python
assert isinstance(res1, tm.SubclassedDataFrame)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res1, exp1)
```

**Verification:**
```python
assert isinstance(res2, tm.SubclassedDataFrame)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res2, exp2)
```

### Step 8: Assign unknown = df1.a.align(...)

```python
res1, res2 = df1.a.align(df2.c)
```

**Verification:**
```python
assert isinstance(res1, tm.SubclassedSeries)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res1, exp1.a)
```

**Verification:**
```python
assert isinstance(res2, tm.SubclassedSeries)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res2, exp2.c)
```


## Complete Example

```python
# Workflow
df1 = tm.SubclassedDataFrame({'a': [1, 3, 5], 'b': [1, 3, 5]}, index=list('ACE'))
df2 = tm.SubclassedDataFrame({'c': [1, 2, 4], 'd': [1, 2, 4]}, index=list('ABD'))
res1, res2 = df1.align(df2, axis=0)
exp1 = tm.SubclassedDataFrame({'a': [1, np.nan, 3, np.nan, 5], 'b': [1, np.nan, 3, np.nan, 5]}, index=list('ABCDE'))
exp2 = tm.SubclassedDataFrame({'c': [1, 2, np.nan, 4, np.nan], 'd': [1, 2, np.nan, 4, np.nan]}, index=list('ABCDE'))
assert isinstance(res1, tm.SubclassedDataFrame)
tm.assert_frame_equal(res1, exp1)
assert isinstance(res2, tm.SubclassedDataFrame)
tm.assert_frame_equal(res2, exp2)
res1, res2 = df1.a.align(df2.c)
assert isinstance(res1, tm.SubclassedSeries)
tm.assert_series_equal(res1, exp1.a)
assert isinstance(res2, tm.SubclassedSeries)
tm.assert_series_equal(res2, exp2.c)
```

## Next Steps


---

*Source: test_subclass.py:160 | Complexity: Advanced | Last updated: 2026-06-02*