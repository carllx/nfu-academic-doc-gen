# How To: Binary Ops

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test binary ops

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.api`
- `pandas.core.computation`

**Setup Required:**
```python
# Fixtures: request, opname, op_str, left_fix, right_fix
```

## Step-by-Step Guide

### Step 1: Assign left = request.getfixturevalue(...)

```python
left = request.getfixturevalue(left_fix)
```

**Verification:**
```python
assert not result
```

### Step 2: Assign right = request.getfixturevalue(...)

```python
right = request.getfixturevalue(right_fix)
```

### Step 3: Call expr.set_numexpr_threads()

```python
expr.set_numexpr_threads(1)
```

### Step 4: Call testit()

```python
testit(left, right, opname, op_str)
```

### Step 5: Call expr.set_numexpr_threads()

```python
expr.set_numexpr_threads()
```

### Step 6: Call testit()

```python
testit(left, right, opname, op_str)
```

### Step 7: Assign op = getattr(...)

```python
op = getattr(operator, opname)
```

### Step 8: Assign result = expr.evaluate(...)

```python
result = expr.evaluate(op, left, left, use_numexpr=True)
```

### Step 9: Assign expected = expr.evaluate(...)

```python
expected = expr.evaluate(op, left, left, use_numexpr=False)
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 11: Assign result = expr._can_use_numexpr(...)

```python
result = expr._can_use_numexpr(op, op_str, right, right, 'evaluate')
```

**Verification:**
```python
assert not result
```

### Step 12: Call testit()

```python
testit(left, right, opname, op_str)
```

### Step 13: Assign left = np.abs(...)

```python
left = np.abs(left)
```


## Complete Example

```python
# Setup
# Fixtures: request, opname, op_str, left_fix, right_fix

# Workflow
left = request.getfixturevalue(left_fix)
right = request.getfixturevalue(right_fix)

def testit(left, right, opname, op_str):
    if opname == 'pow':
        left = np.abs(left)
    op = getattr(operator, opname)
    result = expr.evaluate(op, left, left, use_numexpr=True)
    expected = expr.evaluate(op, left, left, use_numexpr=False)
    tm.assert_numpy_array_equal(result, expected)
    result = expr._can_use_numexpr(op, op_str, right, right, 'evaluate')
    assert not result
with option_context('compute.use_numexpr', False):
    testit(left, right, opname, op_str)
expr.set_numexpr_threads(1)
testit(left, right, opname, op_str)
expr.set_numexpr_threads()
testit(left, right, opname, op_str)
```

## Next Steps


---

*Source: test_expressions.py:217 | Complexity: Advanced | Last updated: 2026-06-02*