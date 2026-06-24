# How To: To Dict Index Dtypes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test to dict index dtypes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: into, expected
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'int_col': [1, 2, 3], 'float_col': [1.0, 2.0, 3.0]})
```

### Step 2: Assign result = df.to_dict(...)

```python
result = df.to_dict(orient='index', into=into)
```

### Step 3: Assign cols = value

```python
cols = ['int_col', 'float_col']
```

### Step 4: Assign result = value

```python
result = DataFrame.from_dict(result, orient='index')[cols]
```

### Step 5: Assign expected = value

```python
expected = DataFrame.from_dict(expected, orient='index')[cols]
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: into, expected

# Workflow
df = DataFrame({'int_col': [1, 2, 3], 'float_col': [1.0, 2.0, 3.0]})
result = df.to_dict(orient='index', into=into)
cols = ['int_col', 'float_col']
result = DataFrame.from_dict(result, orient='index')[cols]
expected = DataFrame.from_dict(expected, orient='index')[cols]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_to_dict.py:259 | Complexity: Intermediate | Last updated: 2026-06-02*