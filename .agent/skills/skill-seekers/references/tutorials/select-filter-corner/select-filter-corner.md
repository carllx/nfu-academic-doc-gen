# How To: Select Filter Corner

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test select filter corner

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
df = DataFrame(np.random.default_rng(2).standard_normal((50, 100)))
```

### Step 2: Assign df.index = value

```python
df.index = [f'{c:3d}' for c in df.index]
```

### Step 3: Assign df.columns = value

```python
df.columns = [f'{c:3d}' for c in df.columns]
```

### Step 4: Call store.put()

```python
store.put('frame', df, format='table')
```

### Step 5: Assign crit = 'columns=df.columns[:75]'

```python
crit = 'columns=df.columns[:75]'
```

### Step 6: Assign result = store.select(...)

```python
result = store.select('frame', [crit])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df.loc[:, df.columns[:75]])
```

### Step 8: Assign crit = 'columns=df.columns[:75:2]'

```python
crit = 'columns=df.columns[:75:2]'
```

### Step 9: Assign result = store.select(...)

```python
result = store.select('frame', [crit])
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df.loc[:, df.columns[:75:2]])
```


## Complete Example

```python
# Setup
# Fixtures: setup_path

# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((50, 100)))
df.index = [f'{c:3d}' for c in df.index]
df.columns = [f'{c:3d}' for c in df.columns]
with ensure_clean_store(setup_path) as store:
    store.put('frame', df, format='table')
    crit = 'columns=df.columns[:75]'
    result = store.select('frame', [crit])
    tm.assert_frame_equal(result, df.loc[:, df.columns[:75]])
    crit = 'columns=df.columns[:75:2]'
    result = store.select('frame', [crit])
    tm.assert_frame_equal(result, df.loc[:, df.columns[:75:2]])
```

## Next Steps


---

*Source: test_store.py:893 | Complexity: Advanced | Last updated: 2026-06-02*