# How To: Diff Readonly

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test diff readonly

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arr = np.random.default_rng.standard_normal(...)

```python
arr = np.random.default_rng(2).standard_normal((5, 2))
```

### Step 2: Assign arr.flags.writeable = False

```python
arr.flags.writeable = False
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(arr)
```

### Step 4: Assign result = df.diff(...)

```python
result = df.diff()
```

### Step 5: Assign expected = DataFrame.diff(...)

```python
expected = DataFrame(np.array(df)).diff()
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
arr = np.random.default_rng(2).standard_normal((5, 2))
arr.flags.writeable = False
df = DataFrame(arr)
result = df.diff()
expected = DataFrame(np.array(df)).diff()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_diff.py:290 | Complexity: Intermediate | Last updated: 2026-06-02*