# How To: Read Only Buffer Source Agg

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test read only buffer source agg

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.common`

**Setup Required:**
```python
# Fixtures: agg
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'sepal_length': [5.1, 4.9, 4.7, 4.6, 5.0], 'species': ['setosa', 'setosa', 'setosa', 'setosa', 'setosa']})
```

### Step 2: Assign unknown.flags.writeable = False

```python
df._mgr.arrays[0].flags.writeable = False
```

### Step 3: Assign result = df.groupby.agg(...)

```python
result = df.groupby(['species']).agg({'sepal_length': agg})
```

### Step 4: Assign expected = df.copy.groupby.agg(...)

```python
expected = df.copy().groupby(['species']).agg({'sepal_length': agg})
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: agg

# Workflow
df = DataFrame({'sepal_length': [5.1, 4.9, 4.7, 4.6, 5.0], 'species': ['setosa', 'setosa', 'setosa', 'setosa', 'setosa']})
df._mgr.arrays[0].flags.writeable = False
result = df.groupby(['species']).agg({'sepal_length': agg})
expected = df.copy().groupby(['species']).agg({'sepal_length': agg})
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_cython.py:304 | Complexity: Intermediate | Last updated: 2026-06-02*