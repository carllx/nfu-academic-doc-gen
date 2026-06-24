# How To: Select Dtypes Exclude Using Scalars

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test select dtypes exclude using scalars

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
ri = df.select_dtypes(exclude=np.number)
```

### Step 3: Assign ei = value

```python
ei = df[['a', 'e', 'f', 'g', 'h', 'i', 'j']]
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(ri, ei)
```

### Step 5: Assign ri = df.select_dtypes(...)

```python
ri = df.select_dtypes(exclude='category')
```

### Step 6: Assign ei = value

```python
ei = df[['a', 'b', 'c', 'd', 'e', 'g', 'h', 'i', 'j', 'k']]
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(ri, ei)
```

### Step 8: Call df.select_dtypes()

```python
df.select_dtypes(exclude='period')
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': list('abc'), 'b': list(range(1, 4)), 'c': np.arange(3, 6).astype('u1'), 'd': np.arange(4.0, 7.0, dtype='float64'), 'e': [True, False, True], 'f': pd.Categorical(list('abc')), 'g': pd.date_range('20130101', periods=3), 'h': pd.date_range('20130101', periods=3, tz='US/Eastern'), 'i': pd.date_range('20130101', periods=3, tz='CET'), 'j': pd.period_range('2013-01', periods=3, freq='M'), 'k': pd.timedelta_range('1 day', periods=3)})
ri = df.select_dtypes(exclude=np.number)
ei = df[['a', 'e', 'f', 'g', 'h', 'i', 'j']]
tm.assert_frame_equal(ri, ei)
ri = df.select_dtypes(exclude='category')
ei = df[['a', 'b', 'c', 'd', 'e', 'g', 'h', 'i', 'j', 'k']]
tm.assert_frame_equal(ri, ei)
with pytest.raises(NotImplementedError, match='^$'):
    df.select_dtypes(exclude='period')
```

## Next Steps


---

*Source: test_select_dtypes.py:207 | Complexity: Advanced | Last updated: 2026-06-02*