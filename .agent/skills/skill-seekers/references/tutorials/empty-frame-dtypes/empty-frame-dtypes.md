# How To: Empty Frame Dtypes

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test empty frame dtypes

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

### Step 1: Assign empty_df = DataFrame(...)

```python
empty_df = DataFrame()
```

### Step 2: Call tm.assert_series_equal()

```python
tm.assert_series_equal(empty_df.dtypes, Series(dtype=object))
```

### Step 3: Assign nocols_df = DataFrame(...)

```python
nocols_df = DataFrame(index=[1, 2, 3])
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(nocols_df.dtypes, Series(dtype=object))
```

### Step 5: Assign norows_df = DataFrame(...)

```python
norows_df = DataFrame(columns=list('abc'))
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(norows_df.dtypes, Series(object, index=list('abc')))
```

### Step 7: Assign norows_int_df = DataFrame.astype(...)

```python
norows_int_df = DataFrame(columns=list('abc')).astype(np.int32)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(norows_int_df.dtypes, Series(np.dtype('int32'), index=list('abc')))
```

### Step 9: Assign df = DataFrame(...)

```python
df = DataFrame({'a': 1, 'b': True, 'c': 1.0}, index=[1, 2, 3])
```

### Step 10: Assign ex_dtypes = Series(...)

```python
ex_dtypes = Series({'a': np.int64, 'b': np.bool_, 'c': np.float64})
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(df.dtypes, ex_dtypes)
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(df[:0].dtypes, ex_dtypes)
```


## Complete Example

```python
# Workflow
empty_df = DataFrame()
tm.assert_series_equal(empty_df.dtypes, Series(dtype=object))
nocols_df = DataFrame(index=[1, 2, 3])
tm.assert_series_equal(nocols_df.dtypes, Series(dtype=object))
norows_df = DataFrame(columns=list('abc'))
tm.assert_series_equal(norows_df.dtypes, Series(object, index=list('abc')))
norows_int_df = DataFrame(columns=list('abc')).astype(np.int32)
tm.assert_series_equal(norows_int_df.dtypes, Series(np.dtype('int32'), index=list('abc')))
df = DataFrame({'a': 1, 'b': True, 'c': 1.0}, index=[1, 2, 3])
ex_dtypes = Series({'a': np.int64, 'b': np.bool_, 'c': np.float64})
tm.assert_series_equal(df.dtypes, ex_dtypes)
tm.assert_series_equal(df[:0].dtypes, ex_dtypes)
```

## Next Steps


---

*Source: test_dtypes.py:19 | Complexity: Advanced | Last updated: 2026-06-02*