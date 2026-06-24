# How To: Frame

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test frame

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

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=Index(list('ABCD')), index=Index([f'i-{i}' for i in range(30)]))
```

**Verification:**
```python
assert recons._mgr.is_consolidated()
```

### Step 2: Assign unknown = value

```python
df.iloc[0, 0] = np.nan
```

### Step 3: Assign unknown = value

```python
df.iloc[5, 3] = np.nan
```

### Step 4: Call _check_roundtrip_table()

```python
_check_roundtrip_table(df, tm.assert_frame_equal, path=setup_path, compression=compression)
```

### Step 5: Call _check_roundtrip()

```python
_check_roundtrip(df, tm.assert_frame_equal, path=setup_path, compression=compression)
```

### Step 6: Assign tdf = DataFrame(...)

```python
tdf = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=Index(list('ABCD')), index=date_range('2000-01-01', periods=10, freq='B'))
```

### Step 7: Call _check_roundtrip()

```python
_check_roundtrip(tdf, tm.assert_frame_equal, path=setup_path, compression=compression)
```

### Step 8: Assign df2 = value

```python
df2 = df[:0]
```

### Step 9: Assign df2.index = Index(...)

```python
df2.index = Index([])
```

### Step 10: Call _check_roundtrip()

```python
_check_roundtrip(df2[:0], tm.assert_frame_equal, path=setup_path)
```

### Step 11: Assign unknown = np.random.default_rng.standard_normal(...)

```python
df['foo'] = np.random.default_rng(2).standard_normal(len(df))
```

### Step 12: Assign unknown = df

```python
store['df'] = df
```

### Step 13: Assign recons = value

```python
recons = store['df']
```

**Verification:**
```python
assert recons._mgr.is_consolidated()
```


## Complete Example

```python
# Setup
# Fixtures: compression, setup_path

# Workflow
df = DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=Index(list('ABCD')), index=Index([f'i-{i}' for i in range(30)]))
df.iloc[0, 0] = np.nan
df.iloc[5, 3] = np.nan
_check_roundtrip_table(df, tm.assert_frame_equal, path=setup_path, compression=compression)
_check_roundtrip(df, tm.assert_frame_equal, path=setup_path, compression=compression)
tdf = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=Index(list('ABCD')), index=date_range('2000-01-01', periods=10, freq='B'))
_check_roundtrip(tdf, tm.assert_frame_equal, path=setup_path, compression=compression)
with ensure_clean_store(setup_path) as store:
    df['foo'] = np.random.default_rng(2).standard_normal(len(df))
    store['df'] = df
    recons = store['df']
    assert recons._mgr.is_consolidated()
df2 = df[:0]
df2.index = Index([])
_check_roundtrip(df2[:0], tm.assert_frame_equal, path=setup_path)
```

## Next Steps


---

*Source: test_round_trip.py:362 | Complexity: Advanced | Last updated: 2026-06-02*