# How To: Dups Index

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dups index

## Prerequisites

**Required Modules:**
- `copy`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).integers(0, 10, size=40).reshape(10, 4), columns=['A', 'A', 'C', 'C'])
```

### Step 2: Assign result = concat(...)

```python
result = concat([df, df], axis=1)
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result.iloc[:, :4], df)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result.iloc[:, 4:], df)
```

### Step 5: Assign result = concat(...)

```python
result = concat([df, df], axis=0)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result.iloc[:10], df)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result.iloc[10:], df)
```

### Step 8: Assign df = concat(...)

```python
df = concat([DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=['A', 'A', 'B', 'B']), DataFrame(np.random.default_rng(2).integers(0, 10, size=20).reshape(10, 2), columns=['A', 'C'])], axis=1)
```

### Step 9: Assign result = concat(...)

```python
result = concat([df, df], axis=1)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result.iloc[:, :6], df)
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result.iloc[:, 6:], df)
```

### Step 12: Assign result = concat(...)

```python
result = concat([df, df], axis=0)
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result.iloc[:10], df)
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result.iloc[10:], df)
```

### Step 15: Assign result = unknown._append(...)

```python
result = df.iloc[0:8, :]._append(df.iloc[8:])
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df)
```

### Step 17: Assign result = unknown._append._append(...)

```python
result = df.iloc[0:8, :]._append(df.iloc[8:9])._append(df.iloc[9:10])
```

### Step 18: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df)
```

### Step 19: Assign expected = concat(...)

```python
expected = concat([df, df], axis=0)
```

### Step 20: Assign result = df._append(...)

```python
result = df._append(df)
```

### Step 21: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).integers(0, 10, size=40).reshape(10, 4), columns=['A', 'A', 'C', 'C'])
result = concat([df, df], axis=1)
tm.assert_frame_equal(result.iloc[:, :4], df)
tm.assert_frame_equal(result.iloc[:, 4:], df)
result = concat([df, df], axis=0)
tm.assert_frame_equal(result.iloc[:10], df)
tm.assert_frame_equal(result.iloc[10:], df)
df = concat([DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=['A', 'A', 'B', 'B']), DataFrame(np.random.default_rng(2).integers(0, 10, size=20).reshape(10, 2), columns=['A', 'C'])], axis=1)
result = concat([df, df], axis=1)
tm.assert_frame_equal(result.iloc[:, :6], df)
tm.assert_frame_equal(result.iloc[:, 6:], df)
result = concat([df, df], axis=0)
tm.assert_frame_equal(result.iloc[:10], df)
tm.assert_frame_equal(result.iloc[10:], df)
result = df.iloc[0:8, :]._append(df.iloc[8:])
tm.assert_frame_equal(result, df)
result = df.iloc[0:8, :]._append(df.iloc[8:9])._append(df.iloc[9:10])
tm.assert_frame_equal(result, df)
expected = concat([df, df], axis=0)
result = df._append(df)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_index.py:158 | Complexity: Advanced | Last updated: 2026-06-02*