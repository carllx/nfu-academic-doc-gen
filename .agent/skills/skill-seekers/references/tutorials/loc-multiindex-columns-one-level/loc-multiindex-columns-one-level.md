# How To: Loc Multiindex Columns One Level

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc multiindex columns one level

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 2]], columns=[['a', 'b']])
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame([1], columns=[['a']])
```

### Step 3: Assign result = value

```python
result = df['a']
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = value

```python
result = df.loc[:, 'a']
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame([[1, 2]], columns=[['a', 'b']])
expected = DataFrame([1], columns=[['a']])
result = df['a']
tm.assert_frame_equal(result, expected)
result = df.loc[:, 'a']
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_getitem.py:233 | Complexity: Intermediate | Last updated: 2026-06-02*