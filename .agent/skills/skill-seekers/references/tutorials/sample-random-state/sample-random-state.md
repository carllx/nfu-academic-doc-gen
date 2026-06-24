# How To: Sample Random State

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test sample random state

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.common`

**Setup Required:**
```python
# Fixtures: func_str, arg, frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign obj = DataFrame(...)

```python
obj = DataFrame({'col1': range(10, 20), 'col2': range(20, 30)})
```

### Step 2: Assign obj = tm.get_obj(...)

```python
obj = tm.get_obj(obj, frame_or_series)
```

### Step 3: Assign result = obj.sample(...)

```python
result = obj.sample(n=3, random_state=eval(func_str)(arg))
```

### Step 4: Assign expected = obj.sample(...)

```python
expected = obj.sample(n=3, random_state=com.random_state(eval(func_str)(arg)))
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: func_str, arg, frame_or_series

# Workflow
obj = DataFrame({'col1': range(10, 20), 'col2': range(20, 30)})
obj = tm.get_obj(obj, frame_or_series)
result = obj.sample(n=3, random_state=eval(func_str)(arg))
expected = obj.sample(n=3, random_state=com.random_state(eval(func_str)(arg)))
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_sample.py:172 | Complexity: Intermediate | Last updated: 2026-06-02*