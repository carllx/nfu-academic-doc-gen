# How To: Construction With Conversions

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test construction with conversions

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.internals.blocks`


## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array([1, 2, 3], dtype='timedelta64[s]')
```

**Verification:**
```python
assert expected.dtypes['dt1'] == 'M8[s]'
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': arr})
```

**Verification:**
```python
assert expected.dtypes['dt2'] == 'M8[s]'
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': pd.timedelta_range('00:00:01', periods=3, freq='s')}, index=range(3))
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(df['A'].to_numpy(), arr)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'dt1': Timestamp('20130101'), 'dt2': date_range('20130101', periods=3).astype('M8[s]')}, index=range(3))
```

**Verification:**
```python
assert expected.dtypes['dt1'] == 'M8[s]'
```

### Step 6: Assign dt1 = np.datetime64(...)

```python
dt1 = np.datetime64('2013-01-01')
```

### Step 7: Assign dt2 = np.array(...)

```python
dt2 = np.array(['2013-01-01', '2013-01-02', '2013-01-03'], dtype='datetime64[D]')
```

### Step 8: Assign df = DataFrame(...)

```python
df = DataFrame({'dt1': dt1, 'dt2': dt2})
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```


## Complete Example

```python
# Workflow
arr = np.array([1, 2, 3], dtype='timedelta64[s]')
df = DataFrame({'A': arr})
expected = DataFrame({'A': pd.timedelta_range('00:00:01', periods=3, freq='s')}, index=range(3))
tm.assert_numpy_array_equal(df['A'].to_numpy(), arr)
expected = DataFrame({'dt1': Timestamp('20130101'), 'dt2': date_range('20130101', periods=3).astype('M8[s]')}, index=range(3))
assert expected.dtypes['dt1'] == 'M8[s]'
assert expected.dtypes['dt2'] == 'M8[s]'
dt1 = np.datetime64('2013-01-01')
dt2 = np.array(['2013-01-01', '2013-01-02', '2013-01-03'], dtype='datetime64[D]')
df = DataFrame({'dt1': dt1, 'dt2': dt2})
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_block_internals.py:207 | Complexity: Advanced | Last updated: 2026-06-02*