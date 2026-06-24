# How To: Apply Mixed Dtype Corner Indexing

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test apply mixed dtype corner indexing

## Prerequisites

**Required Modules:**
- `datetime`
- `warnings`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.frame.common`
- `pandas.util.version`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': ['foo'], 'B': [1.0]})
```

### Step 2: Assign result = df.apply(...)

```python
result = df.apply(lambda x: x['A'], axis=1)
```

### Step 3: Assign expected = Series(...)

```python
expected = Series(['foo'], index=[0])
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = df.apply(...)

```python
result = df.apply(lambda x: x['B'], axis=1)
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([1.0], index=[0])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': ['foo'], 'B': [1.0]})
result = df.apply(lambda x: x['A'], axis=1)
expected = Series(['foo'], index=[0])
tm.assert_series_equal(result, expected)
result = df.apply(lambda x: x['B'], axis=1)
expected = Series([1.0], index=[0])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_frame_apply.py:337 | Complexity: Intermediate | Last updated: 2026-06-02*