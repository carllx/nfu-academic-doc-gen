# How To: Modulus

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test modulus

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
# Fixtures: lhs, rhs, engine, parser
```

## Step-by-Step Guide

### Step 1: Assign ex = 'lhs % rhs'

```python
ex = 'lhs % rhs'
```

### Step 2: Assign result = pd.eval(...)

```python
result = pd.eval(ex, engine=engine, parser=parser)
```

### Step 3: Assign expected = value

```python
expected = lhs % rhs
```

### Step 4: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```

### Step 5: Assign expected = ne.evaluate(...)

```python
expected = ne.evaluate('expected % rhs')
```

### Step 6: Assign expected = _eval_single_bin(...)

```python
expected = _eval_single_bin(expected, '%', rhs, engine)
```

### Step 7: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```

### Step 8: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result.values, expected)
```

### Step 9: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected.item())
```


## Complete Example

```python
# Setup
# Fixtures: lhs, rhs, engine, parser

# Workflow
ex = 'lhs % rhs'
result = pd.eval(ex, engine=engine, parser=parser)
expected = lhs % rhs
tm.assert_almost_equal(result, expected)
if engine == 'numexpr':
    import numexpr as ne
    expected = ne.evaluate('expected % rhs')
    if isinstance(result, (DataFrame, Series)):
        tm.assert_almost_equal(result.values, expected)
    else:
        tm.assert_almost_equal(result, expected.item())
else:
    expected = _eval_single_bin(expected, '%', rhs, engine)
    tm.assert_almost_equal(result, expected)
```

## Next Steps


---

*Source: test_eval.py:308 | Complexity: Advanced | Last updated: 2026-06-02*