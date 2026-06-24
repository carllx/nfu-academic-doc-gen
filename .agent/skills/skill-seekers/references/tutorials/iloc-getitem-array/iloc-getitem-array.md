# How To: Iloc Getitem Array

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test iloc getitem array

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
expected = DataFrame([{'A': 1, 'B': 2, 'C': 3}])
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df.iloc[[0]], expected)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([{'A': 1, 'B': 2, 'C': 3}, {'A': 100, 'B': 200, 'C': 300}])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df.iloc[[0, 1]], expected)
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame([{'B': 2, 'C': 3}, {'B': 2000, 'C': 3000}], index=[0, 2])
```

### Step 7: Assign result = value

```python
result = df.iloc[[0, 2], [1, 2]]
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame([{'A': 1, 'B': 2, 'C': 3}, {'A': 100, 'B': 200, 'C': 300}, {'A': 1000, 'B': 2000, 'C': 3000}])
expected = DataFrame([{'A': 1, 'B': 2, 'C': 3}])
tm.assert_frame_equal(df.iloc[[0]], expected)
expected = DataFrame([{'A': 1, 'B': 2, 'C': 3}, {'A': 100, 'B': 200, 'C': 300}])
tm.assert_frame_equal(df.iloc[[0, 1]], expected)
expected = DataFrame([{'B': 2, 'C': 3}, {'B': 2000, 'C': 3000}], index=[0, 2])
result = df.iloc[[0, 2], [1, 2]]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_iloc.py:338 | Complexity: Advanced | Last updated: 2026-06-02*