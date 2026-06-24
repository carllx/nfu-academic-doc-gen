# How To: Nlargest N Identical Values

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nlargest n identical values

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
df = pd.DataFrame({'a': [1] * 5, 'b': [1, 2, 3, 4, 5]})
```

### Step 2: Assign result = df.nlargest(...)

```python
result = df.nlargest(3, 'a')
```

### Step 3: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'a': [1] * 3, 'b': [1, 2, 3]}, index=[0, 1, 2])
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = df.nsmallest(...)

```python
result = df.nsmallest(3, 'a')
```

### Step 6: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'a': [1] * 3, 'b': [1, 2, 3]})
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = pd.DataFrame({'a': [1] * 5, 'b': [1, 2, 3, 4, 5]})
result = df.nlargest(3, 'a')
expected = pd.DataFrame({'a': [1] * 3, 'b': [1, 2, 3]}, index=[0, 1, 2])
tm.assert_frame_equal(result, expected)
result = df.nsmallest(3, 'a')
expected = pd.DataFrame({'a': [1] * 3, 'b': [1, 2, 3]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_nlargest.py:142 | Complexity: Intermediate | Last updated: 2026-06-02*