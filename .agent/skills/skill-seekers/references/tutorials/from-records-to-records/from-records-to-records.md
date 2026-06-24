# How To: From Records To Records

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from records to records

## Prerequisites

**Required Modules:**
- `collections.abc`
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pytz`
- `pandas._config`
- `pandas.compat`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arr = np.zeros(...)

```python
arr = np.zeros((2,), dtype='i4,f4,S10')
```

**Verification:**
```python
assert len(records.dtype.names) == 3
```

### Step 2: Assign unknown = value

```python
arr[:] = [(1, 2.0, 'Hello'), (2, 3.0, 'World')]
```

**Verification:**
```python
assert len(records.dtype.names) == 2
```

### Step 3: Call DataFrame.from_records()

```python
DataFrame.from_records(arr)
```

**Verification:**
```python
assert 'index' not in records.dtype.names
```

### Step 4: Assign index = Index(...)

```python
index = Index(np.arange(len(arr))[::-1])
```

### Step 5: Assign indexed_frame = DataFrame.from_records(...)

```python
indexed_frame = DataFrame.from_records(arr, index=index)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(indexed_frame.index, index)
```

### Step 7: Assign arr2 = np.zeros(...)

```python
arr2 = np.zeros((2, 3))
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(DataFrame.from_records(arr2), DataFrame(arr2))
```

### Step 9: Assign msg = unknown.join(...)

```python
msg = '|'.join(['Length of values \\(2\\) does not match length of index \\(1\\)'])
```

### Step 10: Assign indexed_frame = DataFrame.from_records(...)

```python
indexed_frame = DataFrame.from_records(arr, index='f1')
```

### Step 11: Assign records = indexed_frame.to_records(...)

```python
records = indexed_frame.to_records()
```

**Verification:**
```python
assert len(records.dtype.names) == 3
```

### Step 12: Assign records = indexed_frame.to_records(...)

```python
records = indexed_frame.to_records(index=False)
```

**Verification:**
```python
assert len(records.dtype.names) == 2
```

### Step 13: Call DataFrame.from_records()

```python
DataFrame.from_records(arr, index=index[:-1])
```


## Complete Example

```python
# Workflow
arr = np.zeros((2,), dtype='i4,f4,S10')
arr[:] = [(1, 2.0, 'Hello'), (2, 3.0, 'World')]
DataFrame.from_records(arr)
index = Index(np.arange(len(arr))[::-1])
indexed_frame = DataFrame.from_records(arr, index=index)
tm.assert_index_equal(indexed_frame.index, index)
arr2 = np.zeros((2, 3))
tm.assert_frame_equal(DataFrame.from_records(arr2), DataFrame(arr2))
msg = '|'.join(['Length of values \\(2\\) does not match length of index \\(1\\)'])
with pytest.raises(ValueError, match=msg):
    DataFrame.from_records(arr, index=index[:-1])
indexed_frame = DataFrame.from_records(arr, index='f1')
records = indexed_frame.to_records()
assert len(records.dtype.names) == 3
records = indexed_frame.to_records(index=False)
assert len(records.dtype.names) == 2
assert 'index' not in records.dtype.names
```

## Next Steps


---

*Source: test_from_records.py:285 | Complexity: Advanced | Last updated: 2026-06-02*