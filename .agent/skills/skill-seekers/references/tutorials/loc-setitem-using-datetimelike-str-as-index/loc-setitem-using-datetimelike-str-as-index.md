# How To: Loc Setitem Using Datetimelike Str As Index

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test loc setitem using datetimelike str as index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `contextlib`
- `datetime`
- `re`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._libs`
- `pandas.compat.numpy`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.indexing`
- `pandas.tests.indexing.common`

**Setup Required:**
```python
# Fixtures: fill_val, exp_dtype
```

## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = ['2022-01-02', '2022-01-03', '2022-01-04', fill_val.date()]
```

### Step 2: Assign index = DatetimeIndex(...)

```python
index = DatetimeIndex(data, tz=fill_val.tz, dtype=exp_dtype)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame([10, 11, 12, 14], columns=['a'], index=index)
```

### Step 4: Assign unknown = 13

```python
df.loc['2022-01-08', 'a'] = 13
```

### Step 5: Call data.append()

```python
data.append('2022-01-08')
```

### Step 6: Assign expected_index = DatetimeIndex(...)

```python
expected_index = DatetimeIndex(data, dtype=exp_dtype)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(df.index, expected_index, exact=True)
```


## Complete Example

```python
# Setup
# Fixtures: fill_val, exp_dtype

# Workflow
data = ['2022-01-02', '2022-01-03', '2022-01-04', fill_val.date()]
index = DatetimeIndex(data, tz=fill_val.tz, dtype=exp_dtype)
df = DataFrame([10, 11, 12, 14], columns=['a'], index=index)
df.loc['2022-01-08', 'a'] = 13
data.append('2022-01-08')
expected_index = DatetimeIndex(data, dtype=exp_dtype)
tm.assert_index_equal(df.index, expected_index, exact=True)
```

## Next Steps


---

*Source: test_loc.py:3085 | Complexity: Intermediate | Last updated: 2026-06-02*