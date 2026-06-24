# How To: Iloc Getitem Slice Dups

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test iloc getitem slice dups

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.tests.indexing.common`


## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=['A', 'A', 'B', 'B'])
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(np.random.default_rng(2).integers(0, 10, size=20).reshape(10, 2), columns=['A', 'C'])
```

### Step 3: Assign df = concat(...)

```python
df = concat([df1, df2], axis=1)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df.iloc[:, :4], df1)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df.iloc[:, 4:], df2)
```

### Step 6: Assign df = concat(...)

```python
df = concat([df2, df1], axis=1)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df.iloc[:, :2], df2)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df.iloc[:, 2:], df1)
```

### Step 9: Assign exp = concat(...)

```python
exp = concat([df2, df1.iloc[:, [0]]], axis=1)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df.iloc[:, 0:3], exp)
```

### Step 11: Assign df = concat(...)

```python
df = concat([df, df], axis=0)
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df.iloc[0:10, :2], df2)
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df.iloc[0:10, 2:], df1)
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df.iloc[10:, :2], df2)
```

### Step 15: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df.iloc[10:, 2:], df1)
```


## Complete Example

```python
# Workflow
df1 = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=['A', 'A', 'B', 'B'])
df2 = DataFrame(np.random.default_rng(2).integers(0, 10, size=20).reshape(10, 2), columns=['A', 'C'])
df = concat([df1, df2], axis=1)
tm.assert_frame_equal(df.iloc[:, :4], df1)
tm.assert_frame_equal(df.iloc[:, 4:], df2)
df = concat([df2, df1], axis=1)
tm.assert_frame_equal(df.iloc[:, :2], df2)
tm.assert_frame_equal(df.iloc[:, 2:], df1)
exp = concat([df2, df1.iloc[:, [0]]], axis=1)
tm.assert_frame_equal(df.iloc[:, 0:3], exp)
df = concat([df, df], axis=0)
tm.assert_frame_equal(df.iloc[0:10, :2], df2)
tm.assert_frame_equal(df.iloc[0:10, 2:], df1)
tm.assert_frame_equal(df.iloc[10:, :2], df2)
tm.assert_frame_equal(df.iloc[10:, 2:], df1)
```

## Next Steps


---

*Source: test_iloc.py:407 | Complexity: Advanced | Last updated: 2026-06-02*