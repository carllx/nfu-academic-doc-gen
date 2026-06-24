# How To: Comparison Ops

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test comparison ops

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
# Fixtures: request, comparison_op, left_fix, right_fix
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
testit()
```

### Step 5: Call expr.set_numexpr_threads()

```python
expr.set_numexpr_threads()
```

### Step 6: Call testit()

```python
testit()
```

### Step 7: Assign f12 = value

```python
f12 = left + 1
```

### Step 8: Assign f22 = value

```python
f22 = right + 1
```

### Step 9: Assign op = comparison_op

```python
op = comparison_op
```

### Step 10: Assign result = expr.evaluate(...)

```python
result = expr.evaluate(op, left, f12, use_numexpr=True)
```

### Step 11: Assign expected = expr.evaluate(...)

```python
expected = expr.evaluate(op, left, f12, use_numexpr=False)
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 13: Assign result = expr._can_use_numexpr(...)

```python
result = expr._can_use_numexpr(op, op, right, f22, 'evaluate')
```

**Verification:**
```python
assert not result
```

### Step 14: Call testit()

```python
testit()
```


## Complete Example

```python
# Setup
# Fixtures: request, comparison_op, left_fix, right_fix

# Workflow
left = request.getfixturevalue(left_fix)
right = request.getfixturevalue(right_fix)

def testit():
    f12 = left + 1
    f22 = right + 1
    op = comparison_op
    result = expr.evaluate(op, left, f12, use_numexpr=True)
    expected = expr.evaluate(op, left, f12, use_numexpr=False)
    tm.assert_numpy_array_equal(result, expected)
    result = expr._can_use_numexpr(op, op, right, f22, 'evaluate')
    assert not result
with option_context('compute.use_numexpr', False):
    testit()
expr.set_numexpr_threads(1)
testit()
expr.set_numexpr_threads()
testit()
```

## Next Steps


---

*Source: test_expressions.py:246 | Complexity: Advanced | Last updated: 2026-06-02*