# How To: Nlargest Duplicate Keep All Ties

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nlargest duplicate keep all ties

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
df = pd.DataFrame({'a': [5, 4, 4, 2, 3, 3, 3, 3], 'b': [10, 9, 8, 7, 5, 50, 10, 20]})
```

### Step 2: Assign result = df.nlargest(...)

```python
result = df.nlargest(4, 'a', keep='all')
```

### Step 3: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'a': {0: 5, 1: 4, 2: 4, 4: 3, 5: 3, 6: 3, 7: 3}, 'b': {0: 10, 1: 9, 2: 8, 4: 5, 5: 50, 6: 10, 7: 20}})
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = df.nsmallest(...)

```python
result = df.nsmallest(2, 'a', keep='all')
```

### Step 6: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'a': {3: 2, 4: 3, 5: 3, 6: 3, 7: 3}, 'b': {3: 7, 4: 5, 5: 50, 6: 10, 7: 20}})
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = pd.DataFrame({'a': [5, 4, 4, 2, 3, 3, 3, 3], 'b': [10, 9, 8, 7, 5, 50, 10, 20]})
result = df.nlargest(4, 'a', keep='all')
expected = pd.DataFrame({'a': {0: 5, 1: 4, 2: 4, 4: 3, 5: 3, 6: 3, 7: 3}, 'b': {0: 10, 1: 9, 2: 8, 4: 5, 5: 50, 6: 10, 7: 20}})
tm.assert_frame_equal(result, expected)
result = df.nsmallest(2, 'a', keep='all')
expected = pd.DataFrame({'a': {3: 2, 4: 3, 5: 3, 6: 3, 7: 3}, 'b': {3: 7, 4: 5, 5: 50, 6: 10, 7: 20}})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_nlargest.py:183 | Complexity: Intermediate | Last updated: 2026-06-02*