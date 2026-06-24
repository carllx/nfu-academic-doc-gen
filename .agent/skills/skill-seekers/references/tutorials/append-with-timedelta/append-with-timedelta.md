# How To: Append With Timedelta

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test append with timedelta

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas.tests.io.pytables.common`

**Setup Required:**
```python
# Fixtures: setup_path
```

## Step-by-Step Guide

### Step 1: Assign ts = Timestamp.as_unit(...)

```python
ts = Timestamp('20130101').as_unit('ns')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': ts, 'B': [ts + timedelta(days=i, seconds=10) for i in range(10)]})
```

### Step 3: Assign unknown = value

```python
df['C'] = df['A'] - df['B']
```

### Step 4: Assign unknown = value

```python
df.loc[3:5, 'C'] = np.nan
```

### Step 5: Call _maybe_remove()

```python
_maybe_remove(store, 'df')
```

### Step 6: Call store.append()

```python
store.append('df', df, data_columns=True)
```

### Step 7: Assign result = store.select(...)

```python
result = store.select('df')
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df)
```

### Step 9: Assign result = store.select(...)

```python
result = store.select('df', where='C<100000')
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df)
```

### Step 11: Assign result = store.select(...)

```python
result = store.select('df', where="C<pd.Timedelta('-3D')")
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df.iloc[3:])
```

### Step 13: Assign result = store.select(...)

```python
result = store.select('df', "C<'-3D'")
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df.iloc[3:])
```

### Step 15: Assign result = store.select(...)

```python
result = store.select('df', "C<'-500000s'")
```

### Step 16: Assign result = result.dropna(...)

```python
result = result.dropna(subset=['C'])
```

### Step 17: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df.iloc[6:])
```

### Step 18: Assign result = store.select(...)

```python
result = store.select('df', "C<'-3.5D'")
```

### Step 19: Assign result = value

```python
result = result.iloc[1:]
```

### Step 20: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df.iloc[4:])
```

### Step 21: Call _maybe_remove()

```python
_maybe_remove(store, 'df2')
```

### Step 22: Call store.put()

```python
store.put('df2', df)
```

### Step 23: Assign result = store.select(...)

```python
result = store.select('df2')
```

### Step 24: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df)
```


## Complete Example

```python
# Setup
# Fixtures: setup_path

# Workflow
ts = Timestamp('20130101').as_unit('ns')
df = DataFrame({'A': ts, 'B': [ts + timedelta(days=i, seconds=10) for i in range(10)]})
df['C'] = df['A'] - df['B']
df.loc[3:5, 'C'] = np.nan
with ensure_clean_store(setup_path) as store:
    _maybe_remove(store, 'df')
    store.append('df', df, data_columns=True)
    result = store.select('df')
    tm.assert_frame_equal(result, df)
    result = store.select('df', where='C<100000')
    tm.assert_frame_equal(result, df)
    result = store.select('df', where="C<pd.Timedelta('-3D')")
    tm.assert_frame_equal(result, df.iloc[3:])
    result = store.select('df', "C<'-3D'")
    tm.assert_frame_equal(result, df.iloc[3:])
    result = store.select('df', "C<'-500000s'")
    result = result.dropna(subset=['C'])
    tm.assert_frame_equal(result, df.iloc[6:])
    result = store.select('df', "C<'-3.5D'")
    result = result.iloc[1:]
    tm.assert_frame_equal(result, df.iloc[4:])
    _maybe_remove(store, 'df2')
    store.put('df2', df)
    result = store.select('df2')
    tm.assert_frame_equal(result, df)
```

## Next Steps


---

*Source: test_append.py:830 | Complexity: Advanced | Last updated: 2026-06-02*