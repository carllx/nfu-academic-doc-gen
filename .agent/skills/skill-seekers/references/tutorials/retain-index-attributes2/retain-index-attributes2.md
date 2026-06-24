# How To: Retain Index Attributes2

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test retain index attributes2

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas.tests.io.pytables.common`

**Setup Required:**
```python
# Fixtures: tmp_path, setup_path
```

## Step-by-Step Guide

### Step 1: Assign path = value

```python
path = tmp_path / setup_path
```

**Verification:**
```python
assert read_hdf(path, key='data').index.name == 'foo'
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': Series(range(3), index=date_range('2000-1-1', periods=3, freq='h'))})
```

**Verification:**
```python
assert read_hdf(path, 'data').index.name is None
```

### Step 3: Call df.to_hdf()

```python
df.to_hdf(path, key='data', mode='w', append=True)
```

### Step 4: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'A': Series(range(3), index=date_range('2002-1-1', periods=3, freq='D'))})
```

### Step 5: Call df2.to_hdf()

```python
df2.to_hdf(path, key='data', append=True)
```

### Step 6: Assign idx = date_range(...)

```python
idx = date_range('2000-1-1', periods=3, freq='h')
```

### Step 7: Assign idx.name = 'foo'

```python
idx.name = 'foo'
```

### Step 8: Assign df = DataFrame(...)

```python
df = DataFrame({'A': Series(range(3), index=idx)})
```

### Step 9: Call df.to_hdf()

```python
df.to_hdf(path, key='data', mode='w', append=True)
```

### Step 10: Assign idx2 = date_range(...)

```python
idx2 = date_range('2001-1-1', periods=3, freq='h')
```

### Step 11: Assign idx2.name = 'bar'

```python
idx2.name = 'bar'
```

### Step 12: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'A': Series(range(3), index=idx2)})
```

### Step 13: Call df2.to_hdf()

```python
df2.to_hdf(path, key='data', append=True)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, setup_path

# Workflow
path = tmp_path / setup_path
with tm.assert_produces_warning(errors.AttributeConflictWarning):
    df = DataFrame({'A': Series(range(3), index=date_range('2000-1-1', periods=3, freq='h'))})
    df.to_hdf(path, key='data', mode='w', append=True)
    df2 = DataFrame({'A': Series(range(3), index=date_range('2002-1-1', periods=3, freq='D'))})
    df2.to_hdf(path, key='data', append=True)
    idx = date_range('2000-1-1', periods=3, freq='h')
    idx.name = 'foo'
    df = DataFrame({'A': Series(range(3), index=idx)})
    df.to_hdf(path, key='data', mode='w', append=True)
assert read_hdf(path, key='data').index.name == 'foo'
with tm.assert_produces_warning(errors.AttributeConflictWarning):
    idx2 = date_range('2001-1-1', periods=3, freq='h')
    idx2.name = 'bar'
    df2 = DataFrame({'A': Series(range(3), index=idx2)})
    df2.to_hdf(path, key='data', append=True)
assert read_hdf(path, 'data').index.name is None
```

## Next Steps


---

*Source: test_retain_attributes.py:65 | Complexity: Advanced | Last updated: 2026-06-02*