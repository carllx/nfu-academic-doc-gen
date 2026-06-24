# How To: Set Attribute

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set attribute

## Prerequisites

**Required Modules:**
- `copy`
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'x': [1, 2, 3]})
```

**Verification:**
```python
assert df.y == 5
```

### Step 2: Assign df.y = 2

```python
df.y = 2
```

### Step 3: Assign unknown = value

```python
df['y'] = [2, 4, 6]
```

### Step 4: Assign df.y = 5

```python
df.y = 5
```

**Verification:**
```python
assert df.y == 5
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(df['y'], Series([2, 4, 6], name='y'))
```


## Complete Example

```python
# Workflow
df = DataFrame({'x': [1, 2, 3]})
df.y = 2
df['y'] = [2, 4, 6]
df.y = 5
assert df.y == 5
tm.assert_series_equal(df['y'], Series([2, 4, 6], name='y'))
```

## Next Steps


---

*Source: test_frame.py:140 | Complexity: Intermediate | Last updated: 2026-06-02*