# How To: Duplicated On Empty Frame

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test duplicated on empty frame

## Prerequisites

**Required Modules:**
- `re`
- `sys`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(columns=['a', 'b'])
```

### Step 2: Assign dupes = df.duplicated(...)

```python
dupes = df.duplicated('a')
```

### Step 3: Assign result = value

```python
result = df[dupes]
```

### Step 4: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame(columns=['a', 'b'])
dupes = df.duplicated('a')
result = df[dupes]
expected = df.copy()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_duplicated.py:97 | Complexity: Intermediate | Last updated: 2026-06-02*