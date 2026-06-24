# How To: Supported For Subclass Series

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test supported for subclass series

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.io.pytables`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = [1, 2, 3]
```

### Step 2: Assign sser = tm.SubclassedSeries(...)

```python
sser = tm.SubclassedSeries(data, dtype=np.intp)
```

### Step 3: Assign expected = Series(...)

```python
expected = Series(data, dtype=np.intp)
```

### Step 4: Assign path = value

```python
path = tmp_path / 'temp.h5'
```

### Step 5: Call sser.to_hdf()

```python
sser.to_hdf(path, key='ser')
```

### Step 6: Assign result = read_hdf(...)

```python
result = read_hdf(path, 'ser')
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign path = value

```python
path = tmp_path / 'temp.h5'
```

### Step 9: Assign result = read_hdf(...)

```python
result = read_hdf(path, 'ser')
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 11: Call store.put()

```python
store.put('ser', sser)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
data = [1, 2, 3]
sser = tm.SubclassedSeries(data, dtype=np.intp)
expected = Series(data, dtype=np.intp)
path = tmp_path / 'temp.h5'
sser.to_hdf(path, key='ser')
result = read_hdf(path, 'ser')
tm.assert_series_equal(result, expected)
path = tmp_path / 'temp.h5'
with HDFStore(path) as store:
    store.put('ser', sser)
result = read_hdf(path, 'ser')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_subclass.py:37 | Complexity: Advanced | Last updated: 2026-06-02*