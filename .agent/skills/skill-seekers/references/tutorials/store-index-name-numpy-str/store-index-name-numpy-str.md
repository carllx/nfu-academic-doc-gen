# How To: Store Index Name Numpy Str

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test store index name numpy str

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `datetime`
- `hashlib`
- `tempfile`
- `time`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.io.pytables.common`
- `pandas.io.pytables`

**Setup Required:**
```python
# Fixtures: tmp_path, table_format, setup_path, unit, tz
```

## Step-by-Step Guide

### Step 1: Assign idx = DatetimeIndex.tz_localize(...)

```python
idx = DatetimeIndex([dt.date(2000, 1, 1), dt.date(2000, 1, 2)], name='colsג').tz_localize(tz)
```

**Verification:**
```python
assert isinstance(df2.index.name, str)
```

### Step 2: Assign idx1 = DatetimeIndex.as_unit.tz_localize(...)

```python
idx1 = DatetimeIndex([dt.date(2010, 1, 1), dt.date(2010, 1, 2)], name='rowsא').as_unit(unit).tz_localize(tz)
```

**Verification:**
```python
assert isinstance(df2.columns.name, str)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(np.arange(4).reshape(2, 2), columns=idx, index=idx1)
```

### Step 4: Assign path = value

```python
path = tmp_path / setup_path
```

### Step 5: Call df.to_hdf()

```python
df.to_hdf(path, key='df', format=table_format)
```

### Step 6: Assign df2 = read_hdf(...)

```python
df2 = read_hdf(path, 'df')
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df2, check_names=True)
```

**Verification:**
```python
assert isinstance(df2.index.name, str)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, table_format, setup_path, unit, tz

# Workflow
idx = DatetimeIndex([dt.date(2000, 1, 1), dt.date(2000, 1, 2)], name='colsג').tz_localize(tz)
idx1 = DatetimeIndex([dt.date(2010, 1, 1), dt.date(2010, 1, 2)], name='rowsא').as_unit(unit).tz_localize(tz)
df = DataFrame(np.arange(4).reshape(2, 2), columns=idx, index=idx1)
path = tmp_path / setup_path
df.to_hdf(path, key='df', format=table_format)
df2 = read_hdf(path, 'df')
tm.assert_frame_equal(df, df2, check_names=True)
assert isinstance(df2.index.name, str)
assert isinstance(df2.columns.name, str)
```

## Next Steps


---

*Source: test_store.py:636 | Complexity: Intermediate | Last updated: 2026-06-02*