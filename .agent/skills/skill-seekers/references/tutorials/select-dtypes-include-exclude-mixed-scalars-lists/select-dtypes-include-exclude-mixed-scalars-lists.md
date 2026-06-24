# How To: Select Dtypes Include Exclude Mixed Scalars Lists

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test select dtypes include exclude mixed scalars lists

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': list('abc'), 'b': list(range(1, 4)), 'c': np.arange(3, 6).astype('u1'), 'd': np.arange(4.0, 7.0, dtype='float64'), 'e': [True, False, True], 'f': pd.Categorical(list('abc')), 'g': pd.date_range('20130101', periods=3), 'h': pd.date_range('20130101', periods=3, tz='US/Eastern'), 'i': pd.date_range('20130101', periods=3, tz='CET'), 'j': pd.period_range('2013-01', periods=3, freq='M'), 'k': pd.timedelta_range('1 day', periods=3)})
```

### Step 2: Assign ri = df.select_dtypes(...)

```python
ri = df.select_dtypes(include=np.number, exclude=['floating', 'timedelta'])
```

### Step 3: Assign ei = value

```python
ei = df[['b', 'c']]
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(ri, ei)
```

### Step 5: Assign ri = df.select_dtypes(...)

```python
ri = df.select_dtypes(include=[np.number, 'category'], exclude='floating')
```

### Step 6: Assign ei = value

```python
ei = df[['b', 'c', 'f', 'k']]
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(ri, ei)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': list('abc'), 'b': list(range(1, 4)), 'c': np.arange(3, 6).astype('u1'), 'd': np.arange(4.0, 7.0, dtype='float64'), 'e': [True, False, True], 'f': pd.Categorical(list('abc')), 'g': pd.date_range('20130101', periods=3), 'h': pd.date_range('20130101', periods=3, tz='US/Eastern'), 'i': pd.date_range('20130101', periods=3, tz='CET'), 'j': pd.period_range('2013-01', periods=3, freq='M'), 'k': pd.timedelta_range('1 day', periods=3)})
ri = df.select_dtypes(include=np.number, exclude=['floating', 'timedelta'])
ei = df[['b', 'c']]
tm.assert_frame_equal(ri, ei)
ri = df.select_dtypes(include=[np.number, 'category'], exclude='floating')
ei = df[['b', 'c', 'f', 'k']]
tm.assert_frame_equal(ri, ei)
```

## Next Steps


---

*Source: test_select_dtypes.py:256 | Complexity: Intermediate | Last updated: 2026-06-02*