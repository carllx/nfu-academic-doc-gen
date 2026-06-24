# How To: Series Mask Boolean

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test series mask boolean

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: values, dtype, mask, indexer_class, frame
```

## Step-by-Step Guide

### Step 1: Assign index = value

```python
index = ['a', 'b', 'c'][:len(values)]
```

### Step 2: Assign mask = value

```python
mask = mask[:len(values)]
```

### Step 3: Assign obj = pd.Series(...)

```python
obj = pd.Series(values, dtype=dtype, index=index)
```

### Step 4: Assign expected = value

```python
expected = obj[mask]
```

### Step 5: Assign result = value

```python
result = obj[mask]
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 7: Assign result = value

```python
result = obj.loc[mask]
```

### Step 8: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 9: Assign mask = pd.array(...)

```python
mask = pd.array(mask, dtype='boolean')
```

### Step 10: Assign msg = 'iLocation based boolean indexing cannot use an indexable as a mask'

```python
msg = 'iLocation based boolean indexing cannot use an indexable as a mask'
```

### Step 11: Assign result = value

```python
result = obj.iloc[mask]
```

### Step 12: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 13: Assign obj = pd.DataFrame(...)

```python
obj = pd.DataFrame(dtype=dtype, index=index)
```

### Step 14: Assign obj = obj.to_frame(...)

```python
obj = obj.to_frame()
```

### Step 15: Assign mask = pd.Series(...)

```python
mask = pd.Series(mask, index=obj.index, dtype='boolean')
```

### Step 16: Assign mask = indexer_class(...)

```python
mask = indexer_class(mask)
```

### Step 17: Assign result = value

```python
result = obj.iloc[mask]
```

### Step 18: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: values, dtype, mask, indexer_class, frame

# Workflow
index = ['a', 'b', 'c'][:len(values)]
mask = mask[:len(values)]
obj = pd.Series(values, dtype=dtype, index=index)
if frame:
    if len(values) == 0:
        obj = pd.DataFrame(dtype=dtype, index=index)
    else:
        obj = obj.to_frame()
if indexer_class is pd.array:
    mask = pd.array(mask, dtype='boolean')
elif indexer_class is pd.Series:
    mask = pd.Series(mask, index=obj.index, dtype='boolean')
else:
    mask = indexer_class(mask)
expected = obj[mask]
result = obj[mask]
tm.assert_equal(result, expected)
if indexer_class is pd.Series:
    msg = 'iLocation based boolean indexing cannot use an indexable as a mask'
    with pytest.raises(ValueError, match=msg):
        result = obj.iloc[mask]
        tm.assert_equal(result, expected)
else:
    result = obj.iloc[mask]
    tm.assert_equal(result, expected)
result = obj.loc[mask]
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_na_indexing.py:28 | Complexity: Advanced | Last updated: 2026-06-02*