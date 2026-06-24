# How To: Drop Api Equivalence

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test drop api equivalence

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`

**Required Fixtures:**
- `api_client` fixture


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 2, 3], [3, 4, 5], [5, 6, 7]], index=['a', 'b', 'c'], columns=['d', 'e', 'f'])
```

### Step 2: Assign res1 = df.drop(...)

```python
res1 = df.drop('a')
```

### Step 3: Assign res2 = df.drop(...)

```python
res2 = df.drop(index='a')
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res1, res2)
```

### Step 5: Assign res1 = df.drop(...)

```python
res1 = df.drop('d', axis=1)
```

### Step 6: Assign res2 = df.drop(...)

```python
res2 = df.drop(columns='d')
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res1, res2)
```

### Step 8: Assign res1 = df.drop(...)

```python
res1 = df.drop(labels='e', axis=1)
```

### Step 9: Assign res2 = df.drop(...)

```python
res2 = df.drop(columns='e')
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res1, res2)
```

### Step 11: Assign res1 = df.drop(...)

```python
res1 = df.drop(['a'], axis=0)
```

### Step 12: Assign res2 = df.drop(...)

```python
res2 = df.drop(index=['a'])
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res1, res2)
```

### Step 14: Assign res1 = df.drop.drop(...)

```python
res1 = df.drop(['a'], axis=0).drop(['d'], axis=1)
```

### Step 15: Assign res2 = df.drop(...)

```python
res2 = df.drop(index=['a'], columns=['d'])
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res1, res2)
```

### Step 17: Assign msg = "Cannot specify both 'labels' and 'index'/'columns'"

```python
msg = "Cannot specify both 'labels' and 'index'/'columns'"
```

### Step 18: Assign msg = "Need to specify at least one of 'labels', 'index' or 'columns'"

```python
msg = "Need to specify at least one of 'labels', 'index' or 'columns'"
```

### Step 19: Call df.drop()

```python
df.drop(labels='a', index='b')
```

### Step 20: Call df.drop()

```python
df.drop(labels='a', columns='b')
```

### Step 21: Call df.drop()

```python
df.drop(axis=1)
```


## Complete Example

```python
# Workflow
df = DataFrame([[1, 2, 3], [3, 4, 5], [5, 6, 7]], index=['a', 'b', 'c'], columns=['d', 'e', 'f'])
res1 = df.drop('a')
res2 = df.drop(index='a')
tm.assert_frame_equal(res1, res2)
res1 = df.drop('d', axis=1)
res2 = df.drop(columns='d')
tm.assert_frame_equal(res1, res2)
res1 = df.drop(labels='e', axis=1)
res2 = df.drop(columns='e')
tm.assert_frame_equal(res1, res2)
res1 = df.drop(['a'], axis=0)
res2 = df.drop(index=['a'])
tm.assert_frame_equal(res1, res2)
res1 = df.drop(['a'], axis=0).drop(['d'], axis=1)
res2 = df.drop(index=['a'], columns=['d'])
tm.assert_frame_equal(res1, res2)
msg = "Cannot specify both 'labels' and 'index'/'columns'"
with pytest.raises(ValueError, match=msg):
    df.drop(labels='a', index='b')
with pytest.raises(ValueError, match=msg):
    df.drop(labels='a', columns='b')
msg = "Need to specify at least one of 'labels', 'index' or 'columns'"
with pytest.raises(ValueError, match=msg):
    df.drop(axis=1)
```

## Next Steps


---

*Source: test_drop.py:196 | Complexity: Advanced | Last updated: 2026-06-02*