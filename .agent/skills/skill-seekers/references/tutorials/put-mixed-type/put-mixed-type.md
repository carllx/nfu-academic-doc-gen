# How To: Put Mixed Type

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test put mixed type

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas.tests.io.pytables.common`
- `pandas.util`

**Setup Required:**
```python
# Fixtures: setup_path, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=Index(list('ABCD')), index=date_range('2000-01-01', periods=10, freq='B'))
```

### Step 2: Assign unknown = 'foo'

```python
df['obj1'] = 'foo'
```

### Step 3: Assign unknown = 'bar'

```python
df['obj2'] = 'bar'
```

### Step 4: Assign unknown = value

```python
df['bool1'] = df['A'] > 0
```

### Step 5: Assign unknown = value

```python
df['bool2'] = df['B'] > 0
```

### Step 6: Assign unknown = True

```python
df['bool3'] = True
```

### Step 7: Assign unknown = 1

```python
df['int1'] = 1
```

### Step 8: Assign unknown = 2

```python
df['int2'] = 2
```

### Step 9: Assign unknown = Timestamp.as_unit(...)

```python
df['timestamp1'] = Timestamp('20010102').as_unit('ns')
```

### Step 10: Assign unknown = Timestamp.as_unit(...)

```python
df['timestamp2'] = Timestamp('20010103').as_unit('ns')
```

### Step 11: Assign unknown = Timestamp.as_unit(...)

```python
df['datetime1'] = Timestamp('20010102').as_unit('ns')
```

### Step 12: Assign unknown = Timestamp.as_unit(...)

```python
df['datetime2'] = Timestamp('20010103').as_unit('ns')
```

### Step 13: Assign unknown = value

```python
df.loc[df.index[3:6], ['obj1']] = np.nan
```

### Step 14: Assign df = df._consolidate(...)

```python
df = df._consolidate()
```

### Step 15: Call _maybe_remove()

```python
_maybe_remove(store, 'df')
```

### Step 16: Assign warning = value

```python
warning = None if using_infer_string else pd.errors.PerformanceWarning
```

### Step 17: Assign expected = store.get(...)

```python
expected = store.get('df')
```

### Step 18: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, df)
```

### Step 19: Call store.put()

```python
store.put('df', df)
```


## Complete Example

```python
# Setup
# Fixtures: setup_path, using_infer_string

# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=Index(list('ABCD')), index=date_range('2000-01-01', periods=10, freq='B'))
df['obj1'] = 'foo'
df['obj2'] = 'bar'
df['bool1'] = df['A'] > 0
df['bool2'] = df['B'] > 0
df['bool3'] = True
df['int1'] = 1
df['int2'] = 2
df['timestamp1'] = Timestamp('20010102').as_unit('ns')
df['timestamp2'] = Timestamp('20010103').as_unit('ns')
df['datetime1'] = Timestamp('20010102').as_unit('ns')
df['datetime2'] = Timestamp('20010103').as_unit('ns')
df.loc[df.index[3:6], ['obj1']] = np.nan
df = df._consolidate()
with ensure_clean_store(setup_path) as store:
    _maybe_remove(store, 'df')
    warning = None if using_infer_string else pd.errors.PerformanceWarning
    with tm.assert_produces_warning(warning):
        store.put('df', df)
    expected = store.get('df')
    tm.assert_frame_equal(expected, df)
```

## Next Steps


---

*Source: test_put.py:205 | Complexity: Advanced | Last updated: 2026-06-02*