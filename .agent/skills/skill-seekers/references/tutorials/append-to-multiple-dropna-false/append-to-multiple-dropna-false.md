# How To: Append To Multiple Dropna False

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test append to multiple dropna false

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

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=Index(list('ABCD')), index=date_range('2000-01-01', periods=10, freq='B'))
```

**Verification:**
```python
assert not store.select('df1a').index.equals(store.select('df2a').index)
```

### Step 2: Assign df2 = df1.copy.rename(...)

```python
df2 = df1.copy().rename(columns='{}_2'.format)
```

### Step 3: Assign unknown = value

```python
df1.iloc[1, df1.columns.get_indexer(['A', 'B'])] = np.nan
```

### Step 4: Assign df = concat(...)

```python
df = concat([df1, df2], axis=1)
```

### Step 5: Call store.append_to_multiple()

```python
store.append_to_multiple({'df1a': ['A', 'B'], 'df2a': None}, df, selector='df1a', dropna=False)
```

### Step 6: Assign msg = 'all tables must have exactly the same nrows!'

```python
msg = 'all tables must have exactly the same nrows!'
```

**Verification:**
```python
assert not store.select('df1a').index.equals(store.select('df2a').index)
```

### Step 7: Call store.select_as_multiple()

```python
store.select_as_multiple(['df1a', 'df2a'])
```


## Complete Example

```python
# Setup
# Fixtures: setup_path

# Workflow
df1 = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=Index(list('ABCD')), index=date_range('2000-01-01', periods=10, freq='B'))
df2 = df1.copy().rename(columns='{}_2'.format)
df1.iloc[1, df1.columns.get_indexer(['A', 'B'])] = np.nan
df = concat([df1, df2], axis=1)
with ensure_clean_store(setup_path) as store, pd.option_context('io.hdf.dropna_table', True):
    store.append_to_multiple({'df1a': ['A', 'B'], 'df2a': None}, df, selector='df1a', dropna=False)
    msg = 'all tables must have exactly the same nrows!'
    with pytest.raises(ValueError, match=msg):
        store.select_as_multiple(['df1a', 'df2a'])
    assert not store.select('df1a').index.equals(store.select('df2a').index)
```

## Next Steps


---

*Source: test_append.py:939 | Complexity: Intermediate | Last updated: 2026-06-02*