# How To: Mi Data Columns

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mi data columns

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
# Fixtures: setup_path
```

## Step-by-Step Guide

### Step 1: Assign idx = MultiIndex.from_arrays(...)

```python
idx = MultiIndex.from_arrays([date_range('2000-01-01', periods=5), range(5)], names=['date', 'id'])
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1.1, 1.2, 1.3, 1.4, 1.5]}, index=idx)
```

### Step 3: Call store.append()

```python
store.append('df', df, data_columns=True)
```

### Step 4: Assign actual = store.select(...)

```python
actual = store.select('df', where='id == 1')
```

### Step 5: Assign expected = value

```python
expected = df.iloc[[1], :]
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(actual, expected)
```


## Complete Example

```python
# Setup
# Fixtures: setup_path

# Workflow
idx = MultiIndex.from_arrays([date_range('2000-01-01', periods=5), range(5)], names=['date', 'id'])
df = DataFrame({'a': [1.1, 1.2, 1.3, 1.4, 1.5]}, index=idx)
with ensure_clean_store(setup_path) as store:
    store.append('df', df, data_columns=True)
    actual = store.select('df', where='id == 1')
    expected = df.iloc[[1], :]
    tm.assert_frame_equal(actual, expected)
```

## Next Steps


---

*Source: test_store.py:484 | Complexity: Intermediate | Last updated: 2026-06-02*