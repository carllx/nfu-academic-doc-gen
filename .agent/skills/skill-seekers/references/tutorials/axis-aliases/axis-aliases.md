# How To: Axis Aliases

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test axis aliases

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `copy`
- `inspect`
- `pydoc`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._config.config`
- `pandas.compat`
- `pandas`
- `pandas`
- `pandas._testing`
- `IPython.core.completer`

**Setup Required:**
```python
# Fixtures: float_frame
```

## Step-by-Step Guide

### Step 1: Assign f = float_frame

```python
f = float_frame
```

### Step 2: Assign expected = f.sum(...)

```python
expected = f.sum(axis=0)
```

### Step 3: Assign result = f.sum(...)

```python
result = f.sum(axis='index')
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign expected = f.sum(...)

```python
expected = f.sum(axis=1)
```

### Step 6: Assign result = f.sum(...)

```python
result = f.sum(axis='columns')
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: float_frame

# Workflow
f = float_frame
expected = f.sum(axis=0)
result = f.sum(axis='index')
tm.assert_series_equal(result, expected)
expected = f.sum(axis=1)
result = f.sum(axis='columns')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_api.py:166 | Complexity: Intermediate | Last updated: 2026-06-02*