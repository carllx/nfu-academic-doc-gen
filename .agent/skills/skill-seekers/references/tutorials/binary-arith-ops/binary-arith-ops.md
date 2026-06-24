# How To: Binary Arith Ops

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test binary arith ops

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
# Fixtures: arith1, lhs, rhs, engine, parser
```

## Step-by-Step Guide

### Step 1: Assign ex = value

```python
ex = f'lhs {arith1} rhs'
```

### Step 2: Assign result = pd.eval(...)

```python
result = pd.eval(ex, engine=engine, parser=parser)
```

### Step 3: Assign expected = _eval_single_bin(...)

```python
expected = _eval_single_bin(lhs, arith1, rhs, engine)
```

### Step 4: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```

### Step 5: Assign ex = value

```python
ex = f'lhs {arith1} rhs {arith1} rhs'
```

### Step 6: Assign result = pd.eval(...)

```python
result = pd.eval(ex, engine=engine, parser=parser)
```

### Step 7: Assign nlhs = _eval_single_bin(...)

```python
nlhs = _eval_single_bin(lhs, arith1, rhs, engine)
```

### Step 8: Assign unknown = nlhs.align(...)

```python
nlhs, ghs = nlhs.align(rhs)
```

### Step 9: Assign expected = ne.evaluate(...)

```python
expected = ne.evaluate(f'nlhs {arith1} ghs')
```

### Step 10: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result.values, expected)
```

### Step 11: Assign expected = eval(...)

```python
expected = eval(f'nlhs {arith1} ghs')
```

### Step 12: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: arith1, lhs, rhs, engine, parser

# Workflow
ex = f'lhs {arith1} rhs'
result = pd.eval(ex, engine=engine, parser=parser)
expected = _eval_single_bin(lhs, arith1, rhs, engine)
tm.assert_almost_equal(result, expected)
ex = f'lhs {arith1} rhs {arith1} rhs'
result = pd.eval(ex, engine=engine, parser=parser)
nlhs = _eval_single_bin(lhs, arith1, rhs, engine)
try:
    nlhs, ghs = nlhs.align(rhs)
except (ValueError, TypeError, AttributeError):
    return
else:
    if engine == 'numexpr':
        import numexpr as ne
        expected = ne.evaluate(f'nlhs {arith1} ghs')
        tm.assert_almost_equal(result.values, expected)
    else:
        expected = eval(f'nlhs {arith1} ghs')
        tm.assert_almost_equal(result, expected)
```

## Next Steps


---

*Source: test_eval.py:276 | Complexity: Advanced | Last updated: 2026-06-02*