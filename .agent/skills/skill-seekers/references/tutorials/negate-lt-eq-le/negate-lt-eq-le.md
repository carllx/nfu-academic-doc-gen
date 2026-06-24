# How To: Negate Lt Eq Le

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test negate lt eq le

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
# Fixtures: engine, parser
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[0, 10], [1, 20]], columns=['cat', 'count'])
```

### Step 2: Assign expected = value

```python
expected = df[~(df.cat > 0)]
```

### Step 3: Assign result = df.query(...)

```python
result = df.query('~(cat > 0)', engine=engine, parser=parser)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign msg = "'Not' nodes are not implemented"

```python
msg = "'Not' nodes are not implemented"
```

### Step 6: Assign result = df.query(...)

```python
result = df.query('not (cat > 0)', engine=engine, parser=parser)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Call df.query()

```python
df.query('not (cat > 0)', engine=engine, parser=parser)
```


## Complete Example

```python
# Setup
# Fixtures: engine, parser

# Workflow
df = DataFrame([[0, 10], [1, 20]], columns=['cat', 'count'])
expected = df[~(df.cat > 0)]
result = df.query('~(cat > 0)', engine=engine, parser=parser)
tm.assert_frame_equal(result, expected)
if parser == 'python':
    msg = "'Not' nodes are not implemented"
    with pytest.raises(NotImplementedError, match=msg):
        df.query('not (cat > 0)', engine=engine, parser=parser)
else:
    result = df.query('not (cat > 0)', engine=engine, parser=parser)
    tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_eval.py:1941 | Complexity: Advanced | Last updated: 2026-06-02*