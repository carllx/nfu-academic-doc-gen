# How To: Roundtrip Series To Dataframe

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test roundtrip series to dataframe

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign categories = Series(...)

```python
categories = Series(['a', 'b', 'c', 'a'])
```

### Step 2: Assign dummies = get_dummies(...)

```python
dummies = get_dummies(categories)
```

### Step 3: Assign result = from_dummies(...)

```python
result = from_dummies(dummies)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'': ['a', 'b', 'c', 'a']})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
categories = Series(['a', 'b', 'c', 'a'])
dummies = get_dummies(categories)
result = from_dummies(dummies)
expected = DataFrame({'': ['a', 'b', 'c', 'a']})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_from_dummies.py:203 | Complexity: Intermediate | Last updated: 2026-06-02*