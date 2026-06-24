# How To: Count

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test count

## Prerequisites

**Required Modules:**
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign frame = DataFrame(...)

```python
frame = DataFrame()
```

**Verification:**
```python
assert isinstance(ct1, Series)
```

### Step 2: Assign ct1 = frame.count(...)

```python
ct1 = frame.count(1)
```

**Verification:**
```python
assert isinstance(ct2, Series)
```

### Step 3: Assign ct2 = frame.count(...)

```python
ct2 = frame.count(0)
```

**Verification:**
```python
assert isinstance(ct2, Series)
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(index=range(10))
```

### Step 5: Assign result = df.count(...)

```python
result = df.count(1)
```

### Step 6: Assign expected = Series(...)

```python
expected = Series(0, index=df.index)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign df = DataFrame(...)

```python
df = DataFrame(columns=range(10))
```

### Step 9: Assign result = df.count(...)

```python
result = df.count(0)
```

### Step 10: Assign expected = Series(...)

```python
expected = Series(0, index=df.columns)
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 12: Assign df = DataFrame(...)

```python
df = DataFrame()
```

### Step 13: Assign result = df.count(...)

```python
result = df.count()
```

### Step 14: Assign expected = Series(...)

```python
expected = Series(dtype='int64')
```

### Step 15: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
frame = DataFrame()
ct1 = frame.count(1)
assert isinstance(ct1, Series)
ct2 = frame.count(0)
assert isinstance(ct2, Series)
df = DataFrame(index=range(10))
result = df.count(1)
expected = Series(0, index=df.index)
tm.assert_series_equal(result, expected)
df = DataFrame(columns=range(10))
result = df.count(0)
expected = Series(0, index=df.columns)
tm.assert_series_equal(result, expected)
df = DataFrame()
result = df.count()
expected = Series(dtype='int64')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_count.py:9 | Complexity: Advanced | Last updated: 2026-06-02*