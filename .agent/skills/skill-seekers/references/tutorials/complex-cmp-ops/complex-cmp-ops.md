# How To: Complex Cmp Ops

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test complex cmp ops

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
# Fixtures: cmp1, cmp2, binop, lhs, rhs, engine, parser
```

## Step-by-Step Guide

### Step 1: Assign lhs_new = _eval_single_bin(...)

```python
lhs_new = _eval_single_bin(lhs, cmp1, rhs, engine)
```

### Step 2: Assign rhs_new = _eval_single_bin(...)

```python
rhs_new = _eval_single_bin(lhs, cmp2, rhs, engine)
```

### Step 3: Assign expected = _eval_single_bin(...)

```python
expected = _eval_single_bin(lhs_new, binop, rhs_new, engine)
```

### Step 4: Assign ex = value

```python
ex = f'(lhs {cmp1} rhs) {binop} (lhs {cmp2} rhs)'
```

### Step 5: Assign result = pd.eval(...)

```python
result = pd.eval(ex, engine=engine, parser=parser)
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 7: Assign msg = "'BoolOp' nodes are not implemented"

```python
msg = "'BoolOp' nodes are not implemented"
```

### Step 8: Assign ex = value

```python
ex = f'(lhs {cmp1} rhs) {binop} (lhs {cmp2} rhs)'
```

### Step 9: Call pd.eval()

```python
pd.eval(ex, engine=engine, parser=parser)
```


## Complete Example

```python
# Setup
# Fixtures: cmp1, cmp2, binop, lhs, rhs, engine, parser

# Workflow
if parser == 'python' and binop in ['and', 'or']:
    msg = "'BoolOp' nodes are not implemented"
    with pytest.raises(NotImplementedError, match=msg):
        ex = f'(lhs {cmp1} rhs) {binop} (lhs {cmp2} rhs)'
        pd.eval(ex, engine=engine, parser=parser)
    return
lhs_new = _eval_single_bin(lhs, cmp1, rhs, engine)
rhs_new = _eval_single_bin(lhs, cmp2, rhs, engine)
expected = _eval_single_bin(lhs_new, binop, rhs_new, engine)
ex = f'(lhs {cmp1} rhs) {binop} (lhs {cmp2} rhs)'
result = pd.eval(ex, engine=engine, parser=parser)
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_eval.py:145 | Complexity: Advanced | Last updated: 2026-06-02*