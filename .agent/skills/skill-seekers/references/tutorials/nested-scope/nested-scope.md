# How To: Nested Scope

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nested scope

## Prerequisites

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.computation.check`


## Step-by-Step Guide

### Step 1: Assign x = 1

```python
x = 1
```

**Verification:**
```python
assert result == 2
```

### Step 2: Assign result = pd.eval(...)

```python
result = pd.eval('x + 1', engine=engine, parser=parser)
```

**Verification:**
```python
assert result == 2
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((5, 3)))
```

### Step 4: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(np.random.default_rng(2).standard_normal((5, 3)))
```

### Step 5: Assign msg = "The '@' prefix is only supported by the pandas parser"

```python
msg = "The '@' prefix is only supported by the pandas parser"
```

### Step 6: Assign expected = value

```python
expected = df[(df > 0) & (df2 > 0)]
```

### Step 7: Assign result = pd.eval(...)

```python
result = pd.eval('df[(df > 0) & (df2 > 0)]', engine=engine, parser=parser)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, result)
```

### Step 9: Assign expected = value

```python
expected = df[(df > 0) & (df2 > 0) & (df[df > 0] > 0)]
```

### Step 10: Assign result = pd.eval(...)

```python
result = pd.eval('df[(df > 0) & (df2 > 0) & (df[df > 0] > 0)]', engine=engine, parser=parser)
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, result)
```

### Step 12: Call df.query()

```python
df.query('(@df>0) & (@df2>0)', engine=engine, parser=parser)
```

### Step 13: Call df.query()

```python
df.query('(df>0) & (df2>0)', engine=engine, parser=parser)
```


## Complete Example

```python
# Workflow
x = 1
result = pd.eval('x + 1', engine=engine, parser=parser)
assert result == 2
df = DataFrame(np.random.default_rng(2).standard_normal((5, 3)))
df2 = DataFrame(np.random.default_rng(2).standard_normal((5, 3)))
msg = "The '@' prefix is only supported by the pandas parser"
with pytest.raises(SyntaxError, match=msg):
    df.query('(@df>0) & (@df2>0)', engine=engine, parser=parser)
with pytest.raises(UndefinedVariableError, match="name 'df' is not defined"):
    df.query('(df>0) & (df2>0)', engine=engine, parser=parser)
expected = df[(df > 0) & (df2 > 0)]
result = pd.eval('df[(df > 0) & (df2 > 0)]', engine=engine, parser=parser)
tm.assert_frame_equal(expected, result)
expected = df[(df > 0) & (df2 > 0) & (df[df > 0] > 0)]
result = pd.eval('df[(df > 0) & (df2 > 0) & (df[df > 0] > 0)]', engine=engine, parser=parser)
tm.assert_frame_equal(expected, result)
```

## Next Steps


---

*Source: test_query_eval.py:868 | Complexity: Advanced | Last updated: 2026-06-02*