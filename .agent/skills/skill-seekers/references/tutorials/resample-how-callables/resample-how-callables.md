# How To: Resample How Callables

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test resample how callables

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `functools`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas._typing`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`
- `pandas.core.indexes.datetimes`
- `pandas.core.indexes.period`
- `pandas.core.resample`
- `pandas.tseries`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: unit
```

## Step-by-Step Guide

### Step 1: Assign data = np.arange(...)

```python
data = np.arange(5, dtype=np.int64)
```

### Step 2: Assign ind = date_range.as_unit(...)

```python
ind = date_range(start='2014-01-01', periods=len(data), freq='d').as_unit(unit)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'A': data, 'B': data}, index=ind)
```

### Step 4: Assign df_standard = df.resample.apply(...)

```python
df_standard = df.resample('ME').apply(fn)
```

### Step 5: Assign df_lambda = df.resample.apply(...)

```python
df_lambda = df.resample('ME').apply(lambda x: str(type(x)))
```

### Step 6: Assign df_partial = df.resample.apply(...)

```python
df_partial = df.resample('ME').apply(partial(fn))
```

### Step 7: Assign df_partial2 = df.resample.apply(...)

```python
df_partial2 = df.resample('ME').apply(partial(fn, a=2))
```

### Step 8: Assign df_class = df.resample.apply(...)

```python
df_class = df.resample('ME').apply(FnClass())
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_standard, df_lambda)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_standard, df_partial)
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_standard, df_partial2)
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_standard, df_class)
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
data = np.arange(5, dtype=np.int64)
ind = date_range(start='2014-01-01', periods=len(data), freq='d').as_unit(unit)
df = DataFrame({'A': data, 'B': data}, index=ind)

def fn(x, a=1):
    return str(type(x))

class FnClass:

    def __call__(self, x):
        return str(type(x))
df_standard = df.resample('ME').apply(fn)
df_lambda = df.resample('ME').apply(lambda x: str(type(x)))
df_partial = df.resample('ME').apply(partial(fn))
df_partial2 = df.resample('ME').apply(partial(fn, a=2))
df_class = df.resample('ME').apply(FnClass())
tm.assert_frame_equal(df_standard, df_lambda)
tm.assert_frame_equal(df_standard, df_partial)
tm.assert_frame_equal(df_standard, df_partial2)
tm.assert_frame_equal(df_standard, df_class)
```

## Next Steps


---

*Source: test_datetime_index.py:260 | Complexity: Advanced | Last updated: 2026-06-02*