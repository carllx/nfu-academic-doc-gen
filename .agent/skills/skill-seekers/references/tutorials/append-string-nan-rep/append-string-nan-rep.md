# How To: Append String Nan Rep

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test append string nan rep

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

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': 'a', 'B': 'foo'}, index=np.arange(10))
```

### Step 2: Assign df_nan = df.copy(...)

```python
df_nan = df.copy()
```

### Step 3: Assign unknown = value

```python
df_nan.loc[0:4, :] = np.nan
```

### Step 4: Assign msg = 'NaN representation is too large for existing column size'

```python
msg = 'NaN representation is too large for existing column size'
```

### Step 5: Call store.append()

```python
store.append('sa', df['A'])
```

### Step 6: Call store.append()

```python
store.append('sb', df['B'], nan_rep='bars')
```

### Step 7: Call store.append()

```python
store.append('sc', df['A'], nan_rep='n')
```

### Step 8: Call store.append()

```python
store.append('sc', df_nan['A'])
```

### Step 9: Assign result = value

```python
result = store['sc']
```

### Step 10: Assign expected = concat(...)

```python
expected = concat([df['A'], df_nan['A']])
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 12: Call store.append()

```python
store.append('sa', df_nan['A'])
```

### Step 13: Call store.append()

```python
store.append('sb', df_nan['B'])
```


## Complete Example

```python
# Setup
# Fixtures: setup_path

# Workflow
df = DataFrame({'A': 'a', 'B': 'foo'}, index=np.arange(10))
df_nan = df.copy()
df_nan.loc[0:4, :] = np.nan
msg = 'NaN representation is too large for existing column size'
with ensure_clean_store(setup_path) as store:
    store.append('sa', df['A'])
    with pytest.raises(ValueError, match=msg):
        store.append('sa', df_nan['A'])
    store.append('sb', df['B'], nan_rep='bars')
    with pytest.raises(ValueError, match=msg):
        store.append('sb', df_nan['B'])
    store.append('sc', df['A'], nan_rep='n')
    store.append('sc', df_nan['A'])
    result = store['sc']
    expected = concat([df['A'], df_nan['A']])
    tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_append.py:992 | Complexity: Advanced | Last updated: 2026-06-02*