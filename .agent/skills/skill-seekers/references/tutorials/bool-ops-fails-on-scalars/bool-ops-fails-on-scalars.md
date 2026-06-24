# How To: Bool Ops Fails On Scalars

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test bool ops fails on scalars

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
# Fixtures: lhs, cmp, rhs, engine, parser
```

## Step-by-Step Guide

### Step 1: Assign gen = value

```python
gen = {int: lambda: np.random.default_rng(2).integers(10), float: np.random.default_rng(2).standard_normal}
```

### Step 2: Assign mid = unknown(...)

```python
mid = gen[lhs]()
```

### Step 3: Assign lhs = unknown(...)

```python
lhs = gen[lhs]()
```

### Step 4: Assign rhs = unknown(...)

```python
rhs = gen[rhs]()
```

### Step 5: Assign ex1 = value

```python
ex1 = f'lhs {cmp} mid {cmp} rhs'
```

### Step 6: Assign ex2 = value

```python
ex2 = f'lhs {cmp} mid and mid {cmp} rhs'
```

### Step 7: Assign ex3 = value

```python
ex3 = f'(lhs {cmp} mid) & (mid {cmp} rhs)'
```

### Step 8: Assign msg = "cannot evaluate scalar only bool ops|'BoolOp' nodes are not"

```python
msg = "cannot evaluate scalar only bool ops|'BoolOp' nodes are not"
```

### Step 9: Call pd.eval()

```python
pd.eval(ex, engine=engine, parser=parser)
```


## Complete Example

```python
# Setup
# Fixtures: lhs, cmp, rhs, engine, parser

# Workflow
gen = {int: lambda: np.random.default_rng(2).integers(10), float: np.random.default_rng(2).standard_normal}
mid = gen[lhs]()
lhs = gen[lhs]()
rhs = gen[rhs]()
ex1 = f'lhs {cmp} mid {cmp} rhs'
ex2 = f'lhs {cmp} mid and mid {cmp} rhs'
ex3 = f'(lhs {cmp} mid) & (mid {cmp} rhs)'
for ex in (ex1, ex2, ex3):
    msg = "cannot evaluate scalar only bool ops|'BoolOp' nodes are not"
    with pytest.raises(NotImplementedError, match=msg):
        pd.eval(ex, engine=engine, parser=parser)
```

## Next Steps


---

*Source: test_eval.py:1885 | Complexity: Advanced | Last updated: 2026-06-02*