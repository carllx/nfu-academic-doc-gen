# How To: Numpy Min Max Unsupported Kwargs Raises

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test numpy min max unsupported kwargs raises

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `sys`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.api.types`

**Setup Required:**
```python
# Fixtures: method, kwarg
```

## Step-by-Step Guide

### Step 1: Assign cat = Categorical(...)

```python
cat = Categorical(['a', 'b', 'c', 'b'], ordered=True)
```

### Step 2: Assign msg = value

```python
msg = f"the '{kwarg}' parameter is not supported in the pandas implementation of {method}"
```

### Step 3: Assign kwargs = value

```python
kwargs = {kwarg: 42}
```

### Step 4: Assign method = getattr(...)

```python
method = getattr(np, method)
```

### Step 5: Assign msg = '`axis` must be fewer than the number of dimensions \\(1\\)'

```python
msg = '`axis` must be fewer than the number of dimensions \\(1\\)'
```

### Step 6: Call method()

```python
method(cat, **kwargs)
```


## Complete Example

```python
# Setup
# Fixtures: method, kwarg

# Workflow
cat = Categorical(['a', 'b', 'c', 'b'], ordered=True)
msg = f"the '{kwarg}' parameter is not supported in the pandas implementation of {method}"
if kwarg == 'axis':
    msg = '`axis` must be fewer than the number of dimensions \\(1\\)'
kwargs = {kwarg: 42}
method = getattr(np, method)
with pytest.raises(ValueError, match=msg):
    method(cat, **kwargs)
```

## Next Steps


---

*Source: test_analytics.py:143 | Complexity: Intermediate | Last updated: 2026-06-02*