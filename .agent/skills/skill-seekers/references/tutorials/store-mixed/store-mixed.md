# How To: Store Mixed

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test store mixed

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.compat`
- `pandas`
- `pandas`
- `pandas.tests.io.pytables.common`
- `pandas.util`

**Setup Required:**
```python
# Fixtures: compression, setup_path
```

## Step-by-Step Guide

### Step 1: Assign df1 = _make_one(...)

```python
df1 = _make_one()
```

### Step 2: Assign df2 = _make_one(...)

```python
df2 = _make_one()
```

### Step 3: Call _check_roundtrip()

```python
_check_roundtrip(df1, tm.assert_frame_equal, path=setup_path)
```

### Step 4: Call _check_roundtrip()

```python
_check_roundtrip(df2, tm.assert_frame_equal, path=setup_path)
```

### Step 5: Call _check_roundtrip()

```python
_check_roundtrip(df1['obj1'], tm.assert_series_equal, path=setup_path, compression=compression)
```

### Step 6: Call _check_roundtrip()

```python
_check_roundtrip(df1['bool1'], tm.assert_series_equal, path=setup_path, compression=compression)
```

### Step 7: Call _check_roundtrip()

```python
_check_roundtrip(df1['int1'], tm.assert_series_equal, path=setup_path, compression=compression)
```

### Step 8: Assign df = DataFrame(...)

```python
df = DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=Index(list('ABCD')), index=Index([f'i-{i}' for i in range(30)]))
```

### Step 9: Assign unknown = 'foo'

```python
df['obj1'] = 'foo'
```

### Step 10: Assign unknown = 'bar'

```python
df['obj2'] = 'bar'
```

### Step 11: Assign unknown = value

```python
df['bool1'] = df['A'] > 0
```

### Step 12: Assign unknown = value

```python
df['bool2'] = df['B'] > 0
```

### Step 13: Assign unknown = 1

```python
df['int1'] = 1
```

### Step 14: Assign unknown = 2

```python
df['int2'] = 2
```

### Step 15: Assign unknown = df1

```python
store['obj'] = df1
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(store['obj'], df1)
```

### Step 17: Assign unknown = df2

```python
store['obj'] = df2
```

### Step 18: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(store['obj'], df2)
```


## Complete Example

```python
# Setup
# Fixtures: compression, setup_path

# Workflow
def _make_one():
    df = DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=Index(list('ABCD')), index=Index([f'i-{i}' for i in range(30)]))
    df['obj1'] = 'foo'
    df['obj2'] = 'bar'
    df['bool1'] = df['A'] > 0
    df['bool2'] = df['B'] > 0
    df['int1'] = 1
    df['int2'] = 2
    return df._consolidate()
df1 = _make_one()
df2 = _make_one()
_check_roundtrip(df1, tm.assert_frame_equal, path=setup_path)
_check_roundtrip(df2, tm.assert_frame_equal, path=setup_path)
with ensure_clean_store(setup_path) as store:
    store['obj'] = df1
    tm.assert_frame_equal(store['obj'], df1)
    store['obj'] = df2
    tm.assert_frame_equal(store['obj'], df2)
_check_roundtrip(df1['obj1'], tm.assert_series_equal, path=setup_path, compression=compression)
_check_roundtrip(df1['bool1'], tm.assert_series_equal, path=setup_path, compression=compression)
_check_roundtrip(df1['int1'], tm.assert_series_equal, path=setup_path, compression=compression)
```

## Next Steps


---

*Source: test_round_trip.py:457 | Complexity: Advanced | Last updated: 2026-06-02*