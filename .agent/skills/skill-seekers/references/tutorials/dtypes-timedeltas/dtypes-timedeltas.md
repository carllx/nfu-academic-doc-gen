# How To: Dtypes Timedeltas

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dtypes timedeltas

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': Series(date_range('2012-1-1', periods=3, freq='D')), 'B': Series([timedelta(days=i) for i in range(3)])})
```

### Step 2: Assign result = value

```python
result = df.dtypes
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([np.dtype('datetime64[ns]'), np.dtype('timedelta64[ns]')], index=list('AB'))
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign unknown = value

```python
df['C'] = df['A'] + df['B']
```

### Step 6: Assign result = value

```python
result = df.dtypes
```

### Step 7: Assign expected = Series(...)

```python
expected = Series([np.dtype('datetime64[ns]'), np.dtype('timedelta64[ns]'), np.dtype('datetime64[ns]')], index=list('ABC'))
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 9: Assign unknown = 1

```python
df['D'] = 1
```

### Step 10: Assign result = value

```python
result = df.dtypes
```

### Step 11: Assign expected = Series(...)

```python
expected = Series([np.dtype('datetime64[ns]'), np.dtype('timedelta64[ns]'), np.dtype('datetime64[ns]'), np.dtype('int64')], index=list('ABCD'))
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': Series(date_range('2012-1-1', periods=3, freq='D')), 'B': Series([timedelta(days=i) for i in range(3)])})
result = df.dtypes
expected = Series([np.dtype('datetime64[ns]'), np.dtype('timedelta64[ns]')], index=list('AB'))
tm.assert_series_equal(result, expected)
df['C'] = df['A'] + df['B']
result = df.dtypes
expected = Series([np.dtype('datetime64[ns]'), np.dtype('timedelta64[ns]'), np.dtype('datetime64[ns]')], index=list('ABC'))
tm.assert_series_equal(result, expected)
df['D'] = 1
result = df.dtypes
expected = Series([np.dtype('datetime64[ns]'), np.dtype('timedelta64[ns]'), np.dtype('datetime64[ns]'), np.dtype('int64')], index=list('ABCD'))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_dtypes.py:106 | Complexity: Advanced | Last updated: 2026-06-02*