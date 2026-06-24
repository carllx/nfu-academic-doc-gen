# How To: Select Dtypes Include Using Scalars

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test select dtypes include using scalars

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': list('abc'), 'b': list(range(1, 4)), 'c': np.arange(3, 6).astype('u1'), 'd': np.arange(4.0, 7.0, dtype='float64'), 'e': [True, False, True], 'f': pd.Categorical(list('abc')), 'g': pd.date_range('20130101', periods=3), 'h': pd.date_range('20130101', periods=3, tz='US/Eastern'), 'i': pd.date_range('20130101', periods=3, tz='CET'), 'j': pd.period_range('2013-01', periods=3, freq='M'), 'k': pd.timedelta_range('1 day', periods=3)})
```

### Step 2: Assign ri = df.select_dtypes(...)

```python
ri = df.select_dtypes(include=np.number)
```

### Step 3: Assign ei = value

```python
ei = df[['b', 'c', 'd', 'k']]
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(ri, ei)
```

### Step 5: Assign ri = df.select_dtypes(...)

```python
ri = df.select_dtypes(include='datetime')
```

### Step 6: Assign ei = value

```python
ei = df[['g']]
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(ri, ei)
```

### Step 8: Assign ri = df.select_dtypes(...)

```python
ri = df.select_dtypes(include='datetime64')
```

### Step 9: Assign ei = value

```python
ei = df[['g']]
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(ri, ei)
```

### Step 11: Assign ri = df.select_dtypes(...)

```python
ri = df.select_dtypes(include='category')
```

### Step 12: Assign ei = value

```python
ei = df[['f']]
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(ri, ei)
```

### Step 14: Call df.select_dtypes()

```python
df.select_dtypes(include='period')
```

### Step 15: Assign ri = df.select_dtypes(...)

```python
ri = df.select_dtypes(include='str')
```

### Step 16: Assign ei = value

```python
ei = df[['a']]
```

### Step 17: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(ri, ei)
```


## Complete Example

```python
# Setup
# Fixtures: using_infer_string

# Workflow
df = DataFrame({'a': list('abc'), 'b': list(range(1, 4)), 'c': np.arange(3, 6).astype('u1'), 'd': np.arange(4.0, 7.0, dtype='float64'), 'e': [True, False, True], 'f': pd.Categorical(list('abc')), 'g': pd.date_range('20130101', periods=3), 'h': pd.date_range('20130101', periods=3, tz='US/Eastern'), 'i': pd.date_range('20130101', periods=3, tz='CET'), 'j': pd.period_range('2013-01', periods=3, freq='M'), 'k': pd.timedelta_range('1 day', periods=3)})
ri = df.select_dtypes(include=np.number)
ei = df[['b', 'c', 'd', 'k']]
tm.assert_frame_equal(ri, ei)
ri = df.select_dtypes(include='datetime')
ei = df[['g']]
tm.assert_frame_equal(ri, ei)
ri = df.select_dtypes(include='datetime64')
ei = df[['g']]
tm.assert_frame_equal(ri, ei)
ri = df.select_dtypes(include='category')
ei = df[['f']]
tm.assert_frame_equal(ri, ei)
with pytest.raises(NotImplementedError, match='^$'):
    df.select_dtypes(include='period')
if using_infer_string:
    ri = df.select_dtypes(include='str')
    ei = df[['a']]
    tm.assert_frame_equal(ri, ei)
```

## Next Steps


---

*Source: test_select_dtypes.py:166 | Complexity: Advanced | Last updated: 2026-06-02*