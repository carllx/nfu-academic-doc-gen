# How To: Store Index Name

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test store index name

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

### Step 2: Assign df.index.name = 'foo'

```python
df.index.name = 'foo'
```

### Step 3: Assign unknown = df

```python
store['frame'] = df
```

### Step 4: Assign recons = value

```python
recons = store['frame']
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(recons, df)
```


## Complete Example

```python
# Setup
# Fixtures: setup_path

# Workflow
df = DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=Index(list('ABCD')), index=Index([f'i-{i}' for i in range(30)]))
df.index.name = 'foo'
with ensure_clean_store(setup_path) as store:
    store['frame'] = df
    recons = store['frame']
    tm.assert_frame_equal(recons, df)
```

## Next Steps


---

*Source: test_store.py:620 | Complexity: Intermediate | Last updated: 2026-06-02*