# How To: Supported For Subclass Dataframe

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test supported for subclass dataframe

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
data = {'a': [1, 2], 'b': [3, 4]}
```

### Step 2: Assign sdf = tm.SubclassedDataFrame(...)

```python
sdf = tm.SubclassedDataFrame(data, dtype=np.intp)
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame(data, dtype=np.intp)
```

### Step 4: Assign path = value

```python
path = tmp_path / 'temp.h5'
```

### Step 5: Call sdf.to_hdf()

```python
sdf.to_hdf(path, key='df')
```

### Step 6: Assign result = read_hdf(...)

```python
result = read_hdf(path, 'df')
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign path = value

```python
path = tmp_path / 'temp.h5'
```

### Step 9: Assign result = read_hdf(...)

```python
result = read_hdf(path, 'df')
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Call store.put()

```python
store.put('df', sdf)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
data = {'a': [1, 2], 'b': [3, 4]}
sdf = tm.SubclassedDataFrame(data, dtype=np.intp)
expected = DataFrame(data, dtype=np.intp)
path = tmp_path / 'temp.h5'
sdf.to_hdf(path, key='df')
result = read_hdf(path, 'df')
tm.assert_frame_equal(result, expected)
path = tmp_path / 'temp.h5'
with HDFStore(path) as store:
    store.put('df', sdf)
result = read_hdf(path, 'df')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_subclass.py:20 | Complexity: Advanced | Last updated: 2026-06-02*