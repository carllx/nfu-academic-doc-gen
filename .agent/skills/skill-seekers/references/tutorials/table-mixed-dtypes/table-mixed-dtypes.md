# How To: Table Mixed Dtypes

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test table mixed dtypes

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

### Step 15: Call store.append()

```python
store.append('df1_mixed', df)
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(store.select('df1_mixed'), df)
```


## Complete Example

```python
# Setup
# Fixtures: setup_path

# Workflow
df = DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=Index(list('ABCD')), index=Index([f'i-{i}' for i in range(30)]))
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
    store.append('df1_mixed', df)
    tm.assert_frame_equal(store.select('df1_mixed'), df)
```

## Next Steps


---

*Source: test_store.py:499 | Complexity: Advanced | Last updated: 2026-06-02*