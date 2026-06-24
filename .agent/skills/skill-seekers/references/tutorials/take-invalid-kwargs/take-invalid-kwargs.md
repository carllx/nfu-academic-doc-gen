# How To: Take Invalid Kwargs

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test take invalid kwargs

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`
- `enum`

**Setup Required:**
```python
# Fixtures: index
```

## Step-by-Step Guide

### Step 1: Assign indices = value

```python
indices = [1, 2]
```

### Step 2: Assign msg = "take\\(\\) got an unexpected keyword argument 'foo'"

```python
msg = "take\\(\\) got an unexpected keyword argument 'foo'"
```

### Step 3: Assign msg = "the 'out' parameter is not supported"

```python
msg = "the 'out' parameter is not supported"
```

### Step 4: Assign msg = "the 'mode' parameter is not supported"

```python
msg = "the 'mode' parameter is not supported"
```

### Step 5: Call index.take()

```python
index.take(indices, foo=2)
```

### Step 6: Call index.take()

```python
index.take(indices, out=indices)
```

### Step 7: Call index.take()

```python
index.take(indices, mode='clip')
```


## Complete Example

```python
# Setup
# Fixtures: index

# Workflow
indices = [1, 2]
msg = "take\\(\\) got an unexpected keyword argument 'foo'"
with pytest.raises(TypeError, match=msg):
    index.take(indices, foo=2)
msg = "the 'out' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    index.take(indices, out=indices)
msg = "the 'mode' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    index.take(indices, mode='clip')
```

## Next Steps


---

*Source: test_indexing.py:42 | Complexity: Intermediate | Last updated: 2026-06-02*