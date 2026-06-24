# How To: Nlargest Multiindex Column Lookup

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nlargest multiindex column lookup

## Prerequisites

**Required Modules:**
- `string`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.util.version`


## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame(columns=pd.MultiIndex.from_product([['x'], ['a', 'b']]), data=[[0.33, 0.13], [0.86, 0.25], [0.25, 0.7], [0.85, 0.91]])
```

### Step 2: Assign result = df.nsmallest(...)

```python
result = df.nsmallest(3, ('x', 'a'))
```

### Step 3: Assign expected = value

```python
expected = df.iloc[[2, 0, 3]]
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = df.nlargest(...)

```python
result = df.nlargest(3, ('x', 'b'))
```

### Step 6: Assign expected = value

```python
expected = df.iloc[[3, 2, 1]]
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = pd.DataFrame(columns=pd.MultiIndex.from_product([['x'], ['a', 'b']]), data=[[0.33, 0.13], [0.86, 0.25], [0.25, 0.7], [0.85, 0.91]])
result = df.nsmallest(3, ('x', 'a'))
expected = df.iloc[[2, 0, 3]]
tm.assert_frame_equal(result, expected)
result = df.nlargest(3, ('x', 'b'))
expected = df.iloc[[3, 2, 1]]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_nlargest.py:206 | Complexity: Intermediate | Last updated: 2026-06-02*