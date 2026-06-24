# How To: Fwf Thousands

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test fwf thousands

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `io`
- `pathlib`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.common`
- `pandas.io.parsers`
- `pandas.arrays`

**Setup Required:**
```python
# Fixtures: thousands
```

## Step-by-Step Guide

### Step 1: Assign data = ' 1 2,334.0    5\n10   13     10.\n'

```python
data = ' 1 2,334.0    5\n10   13     10.\n'
```

### Step 2: Assign data = data.replace(...)

```python
data = data.replace(',', thousands)
```

### Step 3: Assign colspecs = value

```python
colspecs = [(0, 3), (3, 11), (12, 16)]
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 2334.0, 5], [10, 13, 10.0]])
```

### Step 5: Assign result = read_fwf(...)

```python
result = read_fwf(StringIO(data), header=None, colspecs=colspecs, thousands=thousands)
```

### Step 6: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: thousands

# Workflow
data = ' 1 2,334.0    5\n10   13     10.\n'
data = data.replace(',', thousands)
colspecs = [(0, 3), (3, 11), (12, 16)]
expected = DataFrame([[1, 2334.0, 5], [10, 13, 10.0]])
result = read_fwf(StringIO(data), header=None, colspecs=colspecs, thousands=thousands)
tm.assert_almost_equal(result, expected)
```

## Next Steps


---

*Source: test_read_fwf.py:413 | Complexity: Intermediate | Last updated: 2026-06-02*