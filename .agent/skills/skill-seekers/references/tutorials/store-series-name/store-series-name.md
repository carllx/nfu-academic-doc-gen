# How To: Store Series Name

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test store series name

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

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=Index(list('ABCD')), index=Index([f'i-{i}' for i in range(30)]))
```

### Step 2: Assign series = value

```python
series = df['A']
```

### Step 3: Assign unknown = series

```python
store['series'] = series
```

### Step 4: Assign recons = value

```python
recons = store['series']
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(recons, series)
```


## Complete Example

```python
# Setup
# Fixtures: setup_path

# Workflow
df = DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=Index(list('ABCD')), index=Index([f'i-{i}' for i in range(30)]))
series = df['A']
with ensure_clean_store(setup_path) as store:
    store['series'] = series
    recons = store['series']
    tm.assert_series_equal(recons, series)
```

## Next Steps


---

*Source: test_store.py:663 | Complexity: Intermediate | Last updated: 2026-06-02*