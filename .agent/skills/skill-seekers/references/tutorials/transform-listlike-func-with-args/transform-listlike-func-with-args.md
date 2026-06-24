# How To: Transform Listlike Func With Args

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test transform listlike func with args

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tests.apply.common`
- `pandas.tests.frame.common`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'x': [1, 2, 3]})
```

### Step 2: Assign msg = "foo1\\(\\) got an unexpected keyword argument 'b'"

```python
msg = "foo1\\(\\) got an unexpected keyword argument 'b'"
```

### Step 3: Assign result = df.transform(...)

```python
result = df.transform([foo1, foo2], 0, 3, c=4)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[8, 8], [9, 9], [10, 10]], columns=MultiIndex.from_tuples([('x', 'foo1'), ('x', 'foo2')]))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Call df.transform()

```python
df.transform([foo1, foo2], 0, 3, b=3, c=4)
```


## Complete Example

```python
# Workflow
df = DataFrame({'x': [1, 2, 3]})

def foo1(x, a=1, c=0):
    return x + a + c

def foo2(x, b=2, c=0):
    return x + b + c
msg = "foo1\\(\\) got an unexpected keyword argument 'b'"
with pytest.raises(TypeError, match=msg):
    df.transform([foo1, foo2], 0, 3, b=3, c=4)
result = df.transform([foo1, foo2], 0, 3, c=4)
expected = DataFrame([[8, 8], [9, 9], [10, 10]], columns=MultiIndex.from_tuples([('x', 'foo1'), ('x', 'foo2')]))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_frame_transform.py:69 | Complexity: Intermediate | Last updated: 2026-06-02*