# How To: Run Binary

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: tests solely that the result is the same whether or not numexpr is
enabled.  Need to test whether the function does the correct thing
elsewhere.

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
# Fixtures: request, fixture, flex, comparison_op, monkeypatch
```

## Step-by-Step Guide

### Step 1: '\n        tests solely that the result is the same whether or not numexpr is\n        enabled.  Need to test whether the function does the correct thing\n        elsewhere.\n        '

```python
'\n        tests solely that the result is the same whether or not numexpr is\n        enabled.  Need to test whether the function does the correct thing\n        elsewhere.\n        '
```

**Verification:**
```python
assert used_numexpr, 'Did not use numexpr as expected.'
```

### Step 2: Assign df = request.getfixturevalue(...)

```python
df = request.getfixturevalue(fixture)
```

### Step 3: Assign arith = value

```python
arith = comparison_op.__name__
```

### Step 4: Assign other = value

```python
other = df.copy() + 1
```

### Step 5: Call m.setattr()

```python
m.setattr(expr, '_MIN_ELEMENTS', 0)
```

### Step 6: Call expr.set_test_mode()

```python
expr.set_test_mode(True)
```

### Step 7: Assign unknown = self.call_op(...)

```python
result, expected = self.call_op(df, other, flex, arith)
```

### Step 8: Assign used_numexpr = expr.get_test_result(...)

```python
used_numexpr = expr.get_test_result()
```

**Verification:**
```python
assert used_numexpr, 'Did not use numexpr as expected.'
```

### Step 9: Call tm.assert_equal()

```python
tm.assert_equal(expected, result)
```

### Step 10: Assign binary_comp = value

```python
binary_comp = other.iloc[:, i] + 1
```

### Step 11: Call self.call_op()

```python
self.call_op(df.iloc[:, i], binary_comp, flex, 'add')
```


## Complete Example

```python
# Setup
# Fixtures: request, fixture, flex, comparison_op, monkeypatch

# Workflow
'\n        tests solely that the result is the same whether or not numexpr is\n        enabled.  Need to test whether the function does the correct thing\n        elsewhere.\n        '
df = request.getfixturevalue(fixture)
arith = comparison_op.__name__
with option_context('compute.use_numexpr', False):
    other = df.copy() + 1
with monkeypatch.context() as m:
    m.setattr(expr, '_MIN_ELEMENTS', 0)
    expr.set_test_mode(True)
    result, expected = self.call_op(df, other, flex, arith)
    used_numexpr = expr.get_test_result()
    assert used_numexpr, 'Did not use numexpr as expected.'
    tm.assert_equal(expected, result)
    for i in range(len(df.columns)):
        binary_comp = other.iloc[:, i] + 1
        self.call_op(df.iloc[:, i], binary_comp, flex, 'add')
```

## Next Steps


---

*Source: test_expressions.py:168 | Complexity: Advanced | Last updated: 2026-06-02*