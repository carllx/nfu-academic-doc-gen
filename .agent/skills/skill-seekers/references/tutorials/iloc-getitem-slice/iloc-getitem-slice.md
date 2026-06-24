# How To: Iloc Getitem Slice

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test iloc getitem slice

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.tests.indexing.common`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([{'A': 1, 'B': 2, 'C': 3}, {'A': 100, 'B': 200, 'C': 300}, {'A': 1000, 'B': 2000, 'C': 3000}])
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame([{'A': 1, 'B': 2, 'C': 3}, {'A': 100, 'B': 200, 'C': 300}])
```

### Step 3: Assign result = value

```python
result = df.iloc[:2]
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame([{'A': 100, 'B': 200}], index=[1])
```

### Step 6: Assign result = value

```python
result = df.iloc[1:2, 0:2]
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign expected = DataFrame(...)

```python
expected = DataFrame([{'A': 1, 'C': 3}, {'A': 100, 'C': 300}, {'A': 1000, 'C': 3000}])
```

### Step 9: Assign result = value

```python
result = df.iloc[:, lambda df: [0, 2]]
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame([{'A': 1, 'B': 2, 'C': 3}, {'A': 100, 'B': 200, 'C': 300}, {'A': 1000, 'B': 2000, 'C': 3000}])
expected = DataFrame([{'A': 1, 'B': 2, 'C': 3}, {'A': 100, 'B': 200, 'C': 300}])
result = df.iloc[:2]
tm.assert_frame_equal(result, expected)
expected = DataFrame([{'A': 100, 'B': 200}], index=[1])
result = df.iloc[1:2, 0:2]
tm.assert_frame_equal(result, expected)
expected = DataFrame([{'A': 1, 'C': 3}, {'A': 100, 'C': 300}, {'A': 1000, 'C': 3000}])
result = df.iloc[:, lambda df: [0, 2]]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_iloc.py:384 | Complexity: Advanced | Last updated: 2026-06-02*