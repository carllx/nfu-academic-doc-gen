# How To: Append Misc Chunksize

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test append misc chunksize

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
# Fixtures: setup_path, chunksize
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=Index(list('ABCD')), index=Index([f'i-{i}' for i in range(30)]))
```

### Step 2: Assign unknown = 'foo'

```python
df['string'] = 'foo'
```

### Step 3: Assign unknown = 1.0

```python
df['float322'] = 1.0
```

### Step 4: Assign unknown = unknown.astype(...)

```python
df['float322'] = df['float322'].astype('float32')
```

### Step 5: Assign unknown = value

```python
df['bool'] = df['float322'] > 0
```

### Step 6: Assign unknown = Timestamp.as_unit(...)

```python
df['time1'] = Timestamp('20130101').as_unit('ns')
```

### Step 7: Assign unknown = Timestamp.as_unit(...)

```python
df['time2'] = Timestamp('20130102').as_unit('ns')
```

### Step 8: Call store.append()

```python
store.append('obj', df, chunksize=chunksize)
```

### Step 9: Assign result = store.select(...)

```python
result = store.select('obj')
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df)
```


## Complete Example

```python
# Setup
# Fixtures: setup_path, chunksize

# Workflow
df = DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=Index(list('ABCD')), index=Index([f'i-{i}' for i in range(30)]))
df['string'] = 'foo'
df['float322'] = 1.0
df['float322'] = df['float322'].astype('float32')
df['bool'] = df['float322'] > 0
df['time1'] = Timestamp('20130101').as_unit('ns')
df['time2'] = Timestamp('20130102').as_unit('ns')
with ensure_clean_store(setup_path, mode='w') as store:
    store.append('obj', df, chunksize=chunksize)
    result = store.select('obj')
    tm.assert_frame_equal(result, df)
```

## Next Steps


---

*Source: test_append.py:701 | Complexity: Advanced | Last updated: 2026-06-02*