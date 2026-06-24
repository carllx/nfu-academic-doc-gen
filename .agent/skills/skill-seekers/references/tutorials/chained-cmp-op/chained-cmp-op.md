# How To: Chained Cmp Op

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test chained cmp op

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `functools`
- `itertools`
- `operator`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat._optional`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.computation`
- `pandas.core.computation.engines`
- `pandas.core.computation.expr`
- `pandas.core.computation.expressions`
- `pandas.core.computation.ops`
- `pandas.core.computation.scope`
- `pandas.util.version`
- `pandas.core.computation.eval`
- `numexpr`
- `numexpr`

**Setup Required:**
```python
# Fixtures: cmp1, cmp2, lhs, midhs, rhs, engine, parser
```

## Step-by-Step Guide

### Step 1: Assign mid = midhs

```python
mid = midhs
```

### Step 2: Assign lhs_new = _eval_single_bin(...)

```python
lhs_new = _eval_single_bin(lhs, cmp1, mid, engine)
```

### Step 3: Assign rhs_new = _eval_single_bin(...)

```python
rhs_new = _eval_single_bin(mid, cmp2, rhs, engine)
```

### Step 4: Assign ex1 = value

```python
ex1 = f'lhs {cmp1} mid {cmp2} rhs'
```

### Step 5: Assign msg = "'BoolOp' nodes are not implemented"

```python
msg = "'BoolOp' nodes are not implemented"
```

### Step 6: Assign ex1 = value

```python
ex1 = f'lhs {cmp1} mid {cmp2} rhs'
```

### Step 7: Assign ex2 = value

```python
ex2 = f'lhs {cmp1} mid and mid {cmp2} rhs'
```

### Step 8: Assign ex3 = value

```python
ex3 = f'(lhs {cmp1} mid) & (mid {cmp2} rhs)'
```

### Step 9: Assign expected = _eval_single_bin(...)

```python
expected = _eval_single_bin(lhs_new, '&', rhs_new, engine)
```

### Step 10: Call pd.eval()

```python
pd.eval(ex1, engine=engine, parser=parser)
```

### Step 11: Assign result = pd.eval(...)

```python
result = pd.eval(ex, engine=engine, parser=parser)
```

### Step 12: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: cmp1, cmp2, lhs, midhs, rhs, engine, parser

# Workflow
mid = midhs
if parser == 'python':
    ex1 = f'lhs {cmp1} mid {cmp2} rhs'
    msg = "'BoolOp' nodes are not implemented"
    with pytest.raises(NotImplementedError, match=msg):
        pd.eval(ex1, engine=engine, parser=parser)
    return
lhs_new = _eval_single_bin(lhs, cmp1, mid, engine)
rhs_new = _eval_single_bin(mid, cmp2, rhs, engine)
if lhs_new is not None and rhs_new is not None:
    ex1 = f'lhs {cmp1} mid {cmp2} rhs'
    ex2 = f'lhs {cmp1} mid and mid {cmp2} rhs'
    ex3 = f'(lhs {cmp1} mid) & (mid {cmp2} rhs)'
    expected = _eval_single_bin(lhs_new, '&', rhs_new, engine)
    for ex in (ex1, ex2, ex3):
        result = pd.eval(ex, engine=engine, parser=parser)
        tm.assert_almost_equal(result, expected)
```

## Next Steps


---

*Source: test_eval.py:250 | Complexity: Advanced | Last updated: 2026-06-02*