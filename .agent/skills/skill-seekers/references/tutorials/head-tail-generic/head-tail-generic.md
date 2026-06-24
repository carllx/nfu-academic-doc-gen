# How To: Head Tail Generic

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test head tail generic

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: index, frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign ndim = value

```python
ndim = 2 if frame_or_series is DataFrame else 1
```

### Step 2: Assign shape = value

```python
shape = (len(index),) * ndim
```

### Step 3: Assign vals = np.random.default_rng.standard_normal(...)

```python
vals = np.random.default_rng(2).standard_normal(shape)
```

### Step 4: Assign obj = frame_or_series(...)

```python
obj = frame_or_series(vals, index=index)
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(obj.head(), obj.iloc[:5])
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(obj.tail(), obj.iloc[-5:])
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(obj.head(0), obj.iloc[0:0])
```

### Step 8: Call tm.assert_equal()

```python
tm.assert_equal(obj.tail(0), obj.iloc[0:0])
```

### Step 9: Call tm.assert_equal()

```python
tm.assert_equal(obj.head(len(obj) + 1), obj)
```

### Step 10: Call tm.assert_equal()

```python
tm.assert_equal(obj.tail(len(obj) + 1), obj)
```

### Step 11: Call tm.assert_equal()

```python
tm.assert_equal(obj.head(-3), obj.head(len(index) - 3))
```

### Step 12: Call tm.assert_equal()

```python
tm.assert_equal(obj.tail(-3), obj.tail(len(index) - 3))
```


## Complete Example

```python
# Setup
# Fixtures: index, frame_or_series

# Workflow
ndim = 2 if frame_or_series is DataFrame else 1
shape = (len(index),) * ndim
vals = np.random.default_rng(2).standard_normal(shape)
obj = frame_or_series(vals, index=index)
tm.assert_equal(obj.head(), obj.iloc[:5])
tm.assert_equal(obj.tail(), obj.iloc[-5:])
tm.assert_equal(obj.head(0), obj.iloc[0:0])
tm.assert_equal(obj.tail(0), obj.iloc[0:0])
tm.assert_equal(obj.head(len(obj) + 1), obj)
tm.assert_equal(obj.tail(len(obj) + 1), obj)
tm.assert_equal(obj.head(-3), obj.head(len(index) - 3))
tm.assert_equal(obj.tail(-3), obj.tail(len(index) - 3))
```

## Next Steps


---

*Source: test_head_tail.py:7 | Complexity: Advanced | Last updated: 2026-06-02*