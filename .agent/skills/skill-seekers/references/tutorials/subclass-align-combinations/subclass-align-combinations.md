# How To: Subclass Align Combinations

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test subclass align combinations

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
df = tm.SubclassedDataFrame({'a': [1, 3, 5], 'b': [1, 3, 5]}, index=list('ACE'))
```

**Verification:**
```python
assert isinstance(res1, tm.SubclassedDataFrame)
```

### Step 2: Assign s = tm.SubclassedSeries(...)

```python
s = tm.SubclassedSeries([1, 2, 4], index=list('ABD'), name='x')
```

**Verification:**
```python
assert isinstance(res2, tm.SubclassedSeries)
```

### Step 3: Assign unknown = df.align(...)

```python
res1, res2 = df.align(s, axis=0)
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
assert isinstance(res2, tm.SubclassedDataFrame)
```

### Step 5: Assign exp2 = tm.SubclassedSeries(...)

```python
exp2 = tm.SubclassedSeries([1, 2, np.nan, 4, np.nan], index=list('ABCDE'), name='x')
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
assert isinstance(res2, tm.SubclassedSeries)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res2, exp2)
```

### Step 8: Assign unknown = s.align(...)

```python
res1, res2 = s.align(df)
```

**Verification:**
```python
assert isinstance(res1, tm.SubclassedSeries)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res1, exp2)
```

**Verification:**
```python
assert isinstance(res2, tm.SubclassedDataFrame)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res2, exp1)
```


## Complete Example

```python
# Workflow
df = tm.SubclassedDataFrame({'a': [1, 3, 5], 'b': [1, 3, 5]}, index=list('ACE'))
s = tm.SubclassedSeries([1, 2, 4], index=list('ABD'), name='x')
res1, res2 = df.align(s, axis=0)
exp1 = tm.SubclassedDataFrame({'a': [1, np.nan, 3, np.nan, 5], 'b': [1, np.nan, 3, np.nan, 5]}, index=list('ABCDE'))
exp2 = tm.SubclassedSeries([1, 2, np.nan, 4, np.nan], index=list('ABCDE'), name='x')
assert isinstance(res1, tm.SubclassedDataFrame)
tm.assert_frame_equal(res1, exp1)
assert isinstance(res2, tm.SubclassedSeries)
tm.assert_series_equal(res2, exp2)
res1, res2 = s.align(df)
assert isinstance(res1, tm.SubclassedSeries)
tm.assert_series_equal(res1, exp2)
assert isinstance(res2, tm.SubclassedDataFrame)
tm.assert_frame_equal(res2, exp1)
```

## Next Steps


---

*Source: test_subclass.py:189 | Complexity: Advanced | Last updated: 2026-06-02*