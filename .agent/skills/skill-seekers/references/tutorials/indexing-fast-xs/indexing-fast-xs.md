# How To: Indexing Fast Xs

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test indexing fast xs

## Prerequisites

**Required Modules:**
- `re`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': date_range('2014-01-01', periods=10, tz='UTC')})
```

### Step 2: Assign result = value

```python
result = df.iloc[5]
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([Timestamp('2014-01-06 00:00:00+0000', tz='UTC')], index=['a'], name=5, dtype='M8[ns, UTC]')
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = value

```python
result = df.loc[5]
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign result = value

```python
result = df[df.a > df.a[3]]
```

### Step 8: Assign expected = value

```python
expected = df.iloc[4:]
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': date_range('2014-01-01', periods=10, tz='UTC')})
result = df.iloc[5]
expected = Series([Timestamp('2014-01-06 00:00:00+0000', tz='UTC')], index=['a'], name=5, dtype='M8[ns, UTC]')
tm.assert_series_equal(result, expected)
result = df.loc[5]
tm.assert_series_equal(result, expected)
result = df[df.a > df.a[3]]
expected = df.iloc[4:]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_datetime.py:55 | Complexity: Advanced | Last updated: 2026-06-02*