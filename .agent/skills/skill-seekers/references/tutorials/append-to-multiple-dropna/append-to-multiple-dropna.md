# How To: Append To Multiple Dropna

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test append to multiple dropna

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

### Step 2: Assign df2 = DataFrame.rename(...)

```python
df2 = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=Index(list('ABCD')), index=date_range('2000-01-01', periods=10, freq='B')).rename(columns='{}_2'.format)
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
store.append_to_multiple({'df1': ['A', 'B'], 'df2': None}, df, selector='df1', dropna=True)
```

### Step 6: Assign result = store.select_as_multiple(...)

```python
result = store.select_as_multiple(['df1', 'df2'])
```

### Step 7: Assign expected = df.dropna(...)

```python
expected = df.dropna()
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected, check_index_type=True)
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(store.select('df1').index, store.select('df2').index)
```


## Complete Example

```python
# Setup
# Fixtures: setup_path

# Workflow
df1 = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=Index(list('ABCD')), index=date_range('2000-01-01', periods=10, freq='B'))
df2 = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=Index(list('ABCD')), index=date_range('2000-01-01', periods=10, freq='B')).rename(columns='{}_2'.format)
df1.iloc[1, df1.columns.get_indexer(['A', 'B'])] = np.nan
df = concat([df1, df2], axis=1)
with ensure_clean_store(setup_path) as store:
    store.append_to_multiple({'df1': ['A', 'B'], 'df2': None}, df, selector='df1', dropna=True)
    result = store.select_as_multiple(['df1', 'df2'])
    expected = df.dropna()
    tm.assert_frame_equal(result, expected, check_index_type=True)
    tm.assert_index_equal(store.select('df1').index, store.select('df2').index)
```

## Next Steps


---

*Source: test_append.py:914 | Complexity: Advanced | Last updated: 2026-06-02*