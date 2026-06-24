# How To: Getitem List Of Labels Categoricalindex Cols

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem list of labels categoricalindex cols

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign cats = Categorical(...)

```python
cats = Categorical([Timestamp('12-31-1999'), Timestamp('12-31-2000')])
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 0], [0, 1]], dtype='bool', index=[0, 1], columns=cats)
```

### Step 3: Assign dummies = get_dummies(...)

```python
dummies = get_dummies(cats)
```

### Step 4: Assign result = value

```python
result = dummies[list(dummies.columns)]
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
cats = Categorical([Timestamp('12-31-1999'), Timestamp('12-31-2000')])
expected = DataFrame([[1, 0], [0, 1]], dtype='bool', index=[0, 1], columns=cats)
dummies = get_dummies(cats)
result = dummies[list(dummies.columns)]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_getitem.py:48 | Complexity: Intermediate | Last updated: 2026-06-02*