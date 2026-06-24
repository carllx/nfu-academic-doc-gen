# How To: Mixed Depth Pop

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mixed depth pop

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arrays = value

```python
arrays = [['a', 'top', 'top', 'routine1', 'routine1', 'routine2'], ['', 'OD', 'OD', 'result1', 'result2', 'result1'], ['', 'wx', 'wy', '', '', '']]
```

**Verification:**
```python
assert result.name == 'a'
```

### Step 2: Assign tuples = sorted(...)

```python
tuples = sorted(zip(*arrays))
```

### Step 3: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples(tuples)
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((4, 6)), columns=index)
```

### Step 5: Assign df1 = df.copy(...)

```python
df1 = df.copy()
```

### Step 6: Assign df2 = df.copy(...)

```python
df2 = df.copy()
```

### Step 7: Assign result = df1.pop(...)

```python
result = df1.pop('a')
```

### Step 8: Assign expected = df2.pop(...)

```python
expected = df2.pop(('a', '', ''))
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result, check_names=False)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df1, df2)
```

**Verification:**
```python
assert result.name == 'a'
```

### Step 11: Assign expected = value

```python
expected = df1['top']
```

### Step 12: Assign df1 = df1.drop(...)

```python
df1 = df1.drop(['top'], axis=1)
```

### Step 13: Assign result = df2.pop(...)

```python
result = df2.pop('top')
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, result)
```

### Step 15: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df1, df2)
```


## Complete Example

```python
# Workflow
arrays = [['a', 'top', 'top', 'routine1', 'routine1', 'routine2'], ['', 'OD', 'OD', 'result1', 'result2', 'result1'], ['', 'wx', 'wy', '', '', '']]
tuples = sorted(zip(*arrays))
index = MultiIndex.from_tuples(tuples)
df = DataFrame(np.random.default_rng(2).standard_normal((4, 6)), columns=index)
df1 = df.copy()
df2 = df.copy()
result = df1.pop('a')
expected = df2.pop(('a', '', ''))
tm.assert_series_equal(expected, result, check_names=False)
tm.assert_frame_equal(df1, df2)
assert result.name == 'a'
expected = df1['top']
df1 = df1.drop(['top'], axis=1)
result = df2.pop('top')
tm.assert_frame_equal(expected, result)
tm.assert_frame_equal(df1, df2)
```

## Next Steps


---

*Source: test_pop.py:49 | Complexity: Advanced | Last updated: 2026-06-02*