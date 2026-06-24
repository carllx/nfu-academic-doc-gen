# How To: Retain Index Attributes

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test retain index attributes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas.tests.io.pytables.common`

**Setup Required:**
```python
# Fixtures: setup_path, unit
```

## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2000-1-1', periods=3, freq='h', unit=unit)
```

**Verification:**
```python
assert getattr(getattr(df, idx), attr, None) == getattr(getattr(result, idx), attr, None)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': Series(range(3), index=dti)})
```

**Verification:**
```python
assert store.get_storer('data').info['index']['freq'] is None
```

### Step 3: Call _maybe_remove()

```python
_maybe_remove(store, 'data')
```

### Step 4: Call store.put()

```python
store.put('data', df, format='table')
```

### Step 5: Assign result = store.get(...)

```python
result = store.get('data')
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, result)
```

### Step 7: Assign dti2 = date_range(...)

```python
dti2 = date_range('2002-1-1', periods=3, freq='D', unit=unit)
```

**Verification:**
```python
assert store.get_storer('data').info['index']['freq'] is None
```

### Step 8: Call _maybe_remove()

```python
_maybe_remove(store, 'df2')
```

### Step 9: Assign dti3 = DatetimeIndex(...)

```python
dti3 = DatetimeIndex(['2001-01-01', '2001-01-02', '2002-01-01'], dtype=f'M8[{unit}]')
```

### Step 10: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'A': Series(range(3), index=dti3)})
```

### Step 11: Call store.append()

```python
store.append('df2', df2)
```

### Step 12: Assign dti4 = date_range(...)

```python
dti4 = date_range('2002-1-1', periods=3, freq='D', unit=unit)
```

### Step 13: Assign df3 = DataFrame(...)

```python
df3 = DataFrame({'A': Series(range(3), index=dti4)})
```

### Step 14: Call store.append()

```python
store.append('df2', df3)
```

### Step 15: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'A': Series(range(3), index=dti2)})
```

### Step 16: Call store.append()

```python
store.append('data', df2)
```

**Verification:**
```python
assert getattr(getattr(df, idx), attr, None) == getattr(getattr(result, idx), attr, None)
```


## Complete Example

```python
# Setup
# Fixtures: setup_path, unit

# Workflow
dti = date_range('2000-1-1', periods=3, freq='h', unit=unit)
df = DataFrame({'A': Series(range(3), index=dti)})
with ensure_clean_store(setup_path) as store:
    _maybe_remove(store, 'data')
    store.put('data', df, format='table')
    result = store.get('data')
    tm.assert_frame_equal(df, result)
    for attr in ['freq', 'tz', 'name']:
        for idx in ['index', 'columns']:
            assert getattr(getattr(df, idx), attr, None) == getattr(getattr(result, idx), attr, None)
    dti2 = date_range('2002-1-1', periods=3, freq='D', unit=unit)
    with tm.assert_produces_warning(errors.AttributeConflictWarning):
        df2 = DataFrame({'A': Series(range(3), index=dti2)})
        store.append('data', df2)
    assert store.get_storer('data').info['index']['freq'] is None
    _maybe_remove(store, 'df2')
    dti3 = DatetimeIndex(['2001-01-01', '2001-01-02', '2002-01-01'], dtype=f'M8[{unit}]')
    df2 = DataFrame({'A': Series(range(3), index=dti3)})
    store.append('df2', df2)
    dti4 = date_range('2002-1-1', periods=3, freq='D', unit=unit)
    df3 = DataFrame({'A': Series(range(3), index=dti4)})
    store.append('df2', df3)
```

## Next Steps


---

*Source: test_retain_attributes.py:20 | Complexity: Advanced | Last updated: 2026-06-02*