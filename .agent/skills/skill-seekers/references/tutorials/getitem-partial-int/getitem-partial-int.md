# How To: Getitem Partial Int

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem partial int

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign l1 = value

```python
l1 = [10, 20]
```

### Step 2: Assign l2 = value

```python
l2 = ['a', 'b']
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(index=range(2), columns=MultiIndex.from_product([l1, l2]))
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(index=range(2), columns=l2)
```

### Step 5: Assign result = value

```python
result = df[20]
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame(index=range(2), columns=MultiIndex.from_product([l1[1:], l2]))
```

### Step 8: Assign result = value

```python
result = df[[20]]
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: df[1]

```python
df[1]
```

### Step 11: df[[1]]

```python
df[[1]]
```


## Complete Example

```python
# Workflow
l1 = [10, 20]
l2 = ['a', 'b']
df = DataFrame(index=range(2), columns=MultiIndex.from_product([l1, l2]))
expected = DataFrame(index=range(2), columns=l2)
result = df[20]
tm.assert_frame_equal(result, expected)
expected = DataFrame(index=range(2), columns=MultiIndex.from_product([l1[1:], l2]))
result = df[[20]]
tm.assert_frame_equal(result, expected)
with pytest.raises(KeyError, match='1'):
    df[1]
with pytest.raises(KeyError, match="'\\[1\\] not in index'"):
    df[[1]]
```

## Next Steps


---

*Source: test_partial.py:16 | Complexity: Advanced | Last updated: 2026-06-02*