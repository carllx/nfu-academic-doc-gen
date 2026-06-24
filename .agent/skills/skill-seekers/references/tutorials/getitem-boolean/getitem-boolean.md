# How To: Getitem Boolean

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem boolean

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `datetime`
- `decimal`
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._libs`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: mixed_float_frame, mixed_int_frame, datetime_frame
```

## Step-by-Step Guide

### Step 1: Assign d = value

```python
d = datetime_frame.index[10]
```

**Verification:**
```python
assert bif[c].dtype == df[c].dtype
```

### Step 2: Assign indexer = value

```python
indexer = datetime_frame.index > d
```

### Step 3: Assign indexer_obj = indexer.astype(...)

```python
indexer_obj = indexer.astype(object)
```

### Step 4: Assign subindex = value

```python
subindex = datetime_frame.index[indexer]
```

### Step 5: Assign subframe = value

```python
subframe = datetime_frame[indexer]
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(subindex, subframe.index)
```

### Step 7: Assign subframe_obj = value

```python
subframe_obj = datetime_frame[indexer_obj]
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(subframe_obj, subframe)
```

### Step 9: Assign indexer_obj = Series(...)

```python
indexer_obj = Series(indexer_obj, datetime_frame.index)
```

### Step 10: Assign subframe_obj = value

```python
subframe_obj = datetime_frame[indexer_obj]
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(subframe_obj, subframe)
```

### Step 12: datetime_frame[indexer[:-1]]

```python
datetime_frame[indexer[:-1]]
```

### Step 13: datetime_frame[datetime_frame]

```python
datetime_frame[datetime_frame]
```

### Step 14: Assign indexer_obj = indexer_obj.reindex(...)

```python
indexer_obj = indexer_obj.reindex(datetime_frame.index[::-1])
```

### Step 15: Assign subframe_obj = value

```python
subframe_obj = datetime_frame[indexer_obj]
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(subframe_obj, subframe)
```

### Step 17: Assign data = df._get_numeric_data(...)

```python
data = df._get_numeric_data()
```

### Step 18: Assign bif = value

```python
bif = df[df > 0]
```

### Step 19: Assign bifw = DataFrame(...)

```python
bifw = DataFrame({c: np.where(data[c] > 0, data[c], np.nan) for c in data.columns}, index=data.index, columns=data.columns)
```

### Step 20: Assign bifw = bifw.reindex(...)

```python
bifw = bifw.reindex(columns=df.columns)
```

### Step 21: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(bif, bifw, check_dtype=False)
```

### Step 22: Assign unknown = value

```python
bifw[c] = df[c]
```

**Verification:**
```python
assert bif[c].dtype == df[c].dtype
```


## Complete Example

```python
# Setup
# Fixtures: mixed_float_frame, mixed_int_frame, datetime_frame

# Workflow
d = datetime_frame.index[10]
indexer = datetime_frame.index > d
indexer_obj = indexer.astype(object)
subindex = datetime_frame.index[indexer]
subframe = datetime_frame[indexer]
tm.assert_index_equal(subindex, subframe.index)
with pytest.raises(ValueError, match='Item wrong length'):
    datetime_frame[indexer[:-1]]
subframe_obj = datetime_frame[indexer_obj]
tm.assert_frame_equal(subframe_obj, subframe)
with pytest.raises(ValueError, match='Boolean array expected'):
    datetime_frame[datetime_frame]
indexer_obj = Series(indexer_obj, datetime_frame.index)
subframe_obj = datetime_frame[indexer_obj]
tm.assert_frame_equal(subframe_obj, subframe)
with tm.assert_produces_warning(UserWarning):
    indexer_obj = indexer_obj.reindex(datetime_frame.index[::-1])
    subframe_obj = datetime_frame[indexer_obj]
    tm.assert_frame_equal(subframe_obj, subframe)
for df in [datetime_frame, mixed_float_frame, mixed_int_frame]:
    data = df._get_numeric_data()
    bif = df[df > 0]
    bifw = DataFrame({c: np.where(data[c] > 0, data[c], np.nan) for c in data.columns}, index=data.index, columns=data.columns)
    for c in df.columns:
        if c not in bifw:
            bifw[c] = df[c]
    bifw = bifw.reindex(columns=df.columns)
    tm.assert_frame_equal(bif, bifw, check_dtype=False)
    for c in df.columns:
        if bif[c].dtype != bifw[c].dtype:
            assert bif[c].dtype == df[c].dtype
```

## Next Steps


---

*Source: test_indexing.py:126 | Complexity: Advanced | Last updated: 2026-06-02*