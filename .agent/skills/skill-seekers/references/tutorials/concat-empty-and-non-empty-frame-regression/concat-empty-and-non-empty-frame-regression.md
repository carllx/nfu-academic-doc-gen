# How To: Concat Empty And Non Empty Frame Regression

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat empty and non empty frame regression

## Prerequisites

**Required Modules:**
- `collections`
- `collections.abc`
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.tests.extension.decimal`


## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'foo': [1]})
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'foo': []})
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'foo': [1.0]})
```

### Step 4: Assign result = concat(...)

```python
result = concat([df1, df2])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df1 = DataFrame({'foo': [1]})
df2 = DataFrame({'foo': []})
expected = DataFrame({'foo': [1.0]})
result = concat([df1, df2])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_concat.py:571 | Complexity: Intermediate | Last updated: 2026-06-02*