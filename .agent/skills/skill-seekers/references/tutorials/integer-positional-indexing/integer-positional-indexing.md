# How To: Integer Positional Indexing

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: make sure that we are raising on positional indexing
w.r.t. an integer index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: idx
```

## Step-by-Step Guide

### Step 1: 'make sure that we are raising on positional indexing\n        w.r.t. an integer index\n        '

```python
'make sure that we are raising on positional indexing\n        w.r.t. an integer index\n        '
```

### Step 2: Assign s = Series(...)

```python
s = Series(range(2, 6), index=range(2, 6))
```

### Step 3: Assign result = value

```python
result = s[2:4]
```

### Step 4: Assign expected = value

```python
expected = s.iloc[2:4]
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign klass = RangeIndex

```python
klass = RangeIndex
```

### Step 7: Assign msg = value

```python
msg = f'cannot do (slice|positional) indexing on {klass.__name__} with these indexers \\[(2|4)\\.0\\] of type float'
```

### Step 8: s[idx]

```python
s[idx]
```

### Step 9: s.iloc[idx]

```python
s.iloc[idx]
```


## Complete Example

```python
# Setup
# Fixtures: idx

# Workflow
'make sure that we are raising on positional indexing\n        w.r.t. an integer index\n        '
s = Series(range(2, 6), index=range(2, 6))
result = s[2:4]
expected = s.iloc[2:4]
tm.assert_series_equal(result, expected)
klass = RangeIndex
msg = f'cannot do (slice|positional) indexing on {klass.__name__} with these indexers \\[(2|4)\\.0\\] of type float'
with pytest.raises(TypeError, match=msg):
    s[idx]
with pytest.raises(TypeError, match=msg):
    s.iloc[idx]
```

## Next Steps


---

*Source: test_floats.py:333 | Complexity: Advanced | Last updated: 2026-06-02*