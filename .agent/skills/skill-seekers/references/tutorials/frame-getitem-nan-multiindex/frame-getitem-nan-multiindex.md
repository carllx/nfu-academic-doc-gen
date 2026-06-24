# How To: Frame Getitem Nan Multiindex

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test frame getitem nan multiindex

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.indexing`

**Setup Required:**
```python
# Fixtures: nulls_fixture
```

## Step-by-Step Guide

### Step 1: Assign n = nulls_fixture

```python
n = nulls_fixture
```

### Step 2: Assign cols = value

```python
cols = ['a', 'b', 'c']
```

### Step 3: Assign df = DataFrame.set_index(...)

```python
df = DataFrame([[11, n, 13], [21, n, 23], [31, n, 33], [41, n, 43]], columns=cols).set_index(['a', 'b'])
```

### Step 4: Assign unknown = unknown.astype(...)

```python
df['c'] = df['c'].astype('int64')
```

### Step 5: Assign idx = value

```python
idx = (21, n)
```

### Step 6: Assign result = value

```python
result = df.loc[:idx]
```

### Step 7: Assign expected = DataFrame.set_index(...)

```python
expected = DataFrame([[11, n, 13], [21, n, 23]], columns=cols).set_index(['a', 'b'])
```

### Step 8: Assign unknown = unknown.astype(...)

```python
expected['c'] = expected['c'].astype('int64')
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign result = value

```python
result = df.loc[idx:]
```

### Step 11: Assign expected = DataFrame.set_index(...)

```python
expected = DataFrame([[21, n, 23], [31, n, 33], [41, n, 43]], columns=cols).set_index(['a', 'b'])
```

### Step 12: Assign unknown = unknown.astype(...)

```python
expected['c'] = expected['c'].astype('int64')
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 14: Assign unknown = value

```python
idx1, idx2 = ((21, n), (31, n))
```

### Step 15: Assign result = value

```python
result = df.loc[idx1:idx2]
```

### Step 16: Assign expected = DataFrame.set_index(...)

```python
expected = DataFrame([[21, n, 23], [31, n, 33]], columns=cols).set_index(['a', 'b'])
```

### Step 17: Assign unknown = unknown.astype(...)

```python
expected['c'] = expected['c'].astype('int64')
```

### Step 18: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: nulls_fixture

# Workflow
n = nulls_fixture
cols = ['a', 'b', 'c']
df = DataFrame([[11, n, 13], [21, n, 23], [31, n, 33], [41, n, 43]], columns=cols).set_index(['a', 'b'])
df['c'] = df['c'].astype('int64')
idx = (21, n)
result = df.loc[:idx]
expected = DataFrame([[11, n, 13], [21, n, 23]], columns=cols).set_index(['a', 'b'])
expected['c'] = expected['c'].astype('int64')
tm.assert_frame_equal(result, expected)
result = df.loc[idx:]
expected = DataFrame([[21, n, 23], [31, n, 33], [41, n, 43]], columns=cols).set_index(['a', 'b'])
expected['c'] = expected['c'].astype('int64')
tm.assert_frame_equal(result, expected)
idx1, idx2 = ((21, n), (31, n))
result = df.loc[idx1:idx2]
expected = DataFrame([[21, n, 23], [31, n, 33]], columns=cols).set_index(['a', 'b'])
expected['c'] = expected['c'].astype('int64')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_getitem.py:219 | Complexity: Advanced | Last updated: 2026-06-02*