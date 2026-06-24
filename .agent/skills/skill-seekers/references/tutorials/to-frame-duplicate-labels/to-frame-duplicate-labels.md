# How To: To Frame Duplicate Labels

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to frame duplicate labels

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = [(1, 2), (3, 4)]
```

### Step 2: Assign names = value

```python
names = ['a', 'a']
```

### Step 3: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples(data, names=names)
```

### Step 4: Assign result = index.to_frame(...)

```python
result = index.to_frame(allow_duplicates=True)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame(data, index=index, columns=names)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign names = value

```python
names = [None, 0]
```

### Step 8: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples(data, names=names)
```

### Step 9: Assign result = index.to_frame(...)

```python
result = index.to_frame(allow_duplicates=True)
```

### Step 10: Assign expected = DataFrame(...)

```python
expected = DataFrame(data, index=index, columns=[0, 0])
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 12: Call index.to_frame()

```python
index.to_frame()
```

### Step 13: Call index.to_frame()

```python
index.to_frame()
```


## Complete Example

```python
# Workflow
data = [(1, 2), (3, 4)]
names = ['a', 'a']
index = MultiIndex.from_tuples(data, names=names)
with pytest.raises(ValueError, match='Cannot create duplicate column labels'):
    index.to_frame()
result = index.to_frame(allow_duplicates=True)
expected = DataFrame(data, index=index, columns=names)
tm.assert_frame_equal(result, expected)
names = [None, 0]
index = MultiIndex.from_tuples(data, names=names)
with pytest.raises(ValueError, match='Cannot create duplicate column labels'):
    index.to_frame()
result = index.to_frame(allow_duplicates=True)
expected = DataFrame(data, index=index, columns=[0, 0])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_conversion.py:166 | Complexity: Advanced | Last updated: 2026-06-02*