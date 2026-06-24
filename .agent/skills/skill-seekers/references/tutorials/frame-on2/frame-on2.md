# How To: Frame On2

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test frame on2

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: unit
```

## Step-by-Step Guide

### Step 1: Assign dti = DatetimeIndex.as_unit(...)

```python
dti = DatetimeIndex([Timestamp('20130101 09:00:00'), Timestamp('20130101 09:00:02'), Timestamp('20130101 09:00:03'), Timestamp('20130101 09:00:05'), Timestamp('20130101 09:00:06')]).as_unit(unit)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [0, 1, 2, 3, 4], 'B': [0, 1, 2, np.nan, 4], 'C': dti}, columns=['A', 'C', 'B'])
```

### Step 3: Assign expected1 = DataFrame(...)

```python
expected1 = DataFrame({'A': [0.0, 1, 3, 3, 7], 'B': [0, 1, 3, np.nan, 4], 'C': df['C']}, columns=['A', 'C', 'B'])
```

### Step 4: Assign result = df.rolling.sum(...)

```python
result = df.rolling('2s', on='C').sum()
```

### Step 5: Assign expected = expected1

```python
expected = expected1
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign expected = Series(...)

```python
expected = Series([0, 1, 3, np.nan, 4], name='B')
```

### Step 8: Assign result = df.rolling.B.sum(...)

```python
result = df.rolling('2s', on='C').B.sum()
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 10: Assign expected = value

```python
expected = expected1[['A', 'B', 'C']]
```

### Step 11: Assign result = unknown.sum(...)

```python
result = df.rolling('2s', on='C')[['A', 'B', 'C']].sum()
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
dti = DatetimeIndex([Timestamp('20130101 09:00:00'), Timestamp('20130101 09:00:02'), Timestamp('20130101 09:00:03'), Timestamp('20130101 09:00:05'), Timestamp('20130101 09:00:06')]).as_unit(unit)
df = DataFrame({'A': [0, 1, 2, 3, 4], 'B': [0, 1, 2, np.nan, 4], 'C': dti}, columns=['A', 'C', 'B'])
expected1 = DataFrame({'A': [0.0, 1, 3, 3, 7], 'B': [0, 1, 3, np.nan, 4], 'C': df['C']}, columns=['A', 'C', 'B'])
result = df.rolling('2s', on='C').sum()
expected = expected1
tm.assert_frame_equal(result, expected)
expected = Series([0, 1, 3, np.nan, 4], name='B')
result = df.rolling('2s', on='C').B.sum()
tm.assert_series_equal(result, expected)
expected = expected1[['A', 'B', 'C']]
result = df.rolling('2s', on='C')[['A', 'B', 'C']].sum()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_timeseries_window.py:184 | Complexity: Advanced | Last updated: 2026-06-02*