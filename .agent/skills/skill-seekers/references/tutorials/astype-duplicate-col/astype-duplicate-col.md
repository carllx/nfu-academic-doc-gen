# How To: Astype Duplicate Col

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype duplicate col

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign a1 = Series(...)

```python
a1 = Series([1, 2, 3, 4, 5], name='a')
```

### Step 2: Assign b = Series(...)

```python
b = Series([0.1, 0.2, 0.4, 0.6, 0.8], name='b')
```

### Step 3: Assign a2 = Series(...)

```python
a2 = Series([0, 1, 2, 3, 4], name='a')
```

### Step 4: Assign df = concat(...)

```python
df = concat([a1, b, a2], axis=1)
```

### Step 5: Assign result = df.astype(...)

```python
result = df.astype('str')
```

### Step 6: Assign a1_str = Series(...)

```python
a1_str = Series(['1', '2', '3', '4', '5'], dtype='str', name='a')
```

### Step 7: Assign b_str = Series(...)

```python
b_str = Series(['0.1', '0.2', '0.4', '0.6', '0.8'], dtype='str', name='b')
```

### Step 8: Assign a2_str = Series(...)

```python
a2_str = Series(['0', '1', '2', '3', '4'], dtype='str', name='a')
```

### Step 9: Assign expected = concat(...)

```python
expected = concat([a1_str, b_str, a2_str], axis=1)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Assign result = df.astype(...)

```python
result = df.astype({'a': 'str'})
```

### Step 12: Assign expected = concat(...)

```python
expected = concat([a1_str, b, a2_str], axis=1)
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
a1 = Series([1, 2, 3, 4, 5], name='a')
b = Series([0.1, 0.2, 0.4, 0.6, 0.8], name='b')
a2 = Series([0, 1, 2, 3, 4], name='a')
df = concat([a1, b, a2], axis=1)
result = df.astype('str')
a1_str = Series(['1', '2', '3', '4', '5'], dtype='str', name='a')
b_str = Series(['0.1', '0.2', '0.4', '0.6', '0.8'], dtype='str', name='b')
a2_str = Series(['0', '1', '2', '3', '4'], dtype='str', name='a')
expected = concat([a1_str, b_str, a2_str], axis=1)
tm.assert_frame_equal(result, expected)
result = df.astype({'a': 'str'})
expected = concat([a1_str, b, a2_str], axis=1)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_astype.py:260 | Complexity: Advanced | Last updated: 2026-06-02*