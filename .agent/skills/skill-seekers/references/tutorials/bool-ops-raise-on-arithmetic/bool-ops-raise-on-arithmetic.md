# How To: Bool Ops Raise On Arithmetic

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test bool ops raise on arithmetic

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
# Fixtures: op_str, opname
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': np.random.default_rng(2).random(10) > 0.5, 'b': np.random.default_rng(2).random(10) > 0.5})
```

### Step 2: Assign msg = value

```python
msg = f"operator '{opname}' not implemented for bool dtypes"
```

### Step 3: Assign f = getattr(...)

```python
f = getattr(operator, opname)
```

### Step 4: Assign err_msg = re.escape(...)

```python
err_msg = re.escape(msg)
```

### Step 5: Call f()

```python
f(df, df)
```

### Step 6: Call f()

```python
f(df.a, df.b)
```

### Step 7: Call f()

```python
f(df.a, True)
```

### Step 8: Call f()

```python
f(False, df.a)
```

### Step 9: Call f()

```python
f(False, df)
```

### Step 10: Call f()

```python
f(df, True)
```


## Complete Example

```python
# Setup
# Fixtures: op_str, opname

# Workflow
df = DataFrame({'a': np.random.default_rng(2).random(10) > 0.5, 'b': np.random.default_rng(2).random(10) > 0.5})
msg = f"operator '{opname}' not implemented for bool dtypes"
f = getattr(operator, opname)
err_msg = re.escape(msg)
with pytest.raises(NotImplementedError, match=err_msg):
    f(df, df)
with pytest.raises(NotImplementedError, match=err_msg):
    f(df.a, df.b)
with pytest.raises(NotImplementedError, match=err_msg):
    f(df.a, True)
with pytest.raises(NotImplementedError, match=err_msg):
    f(False, df.a)
with pytest.raises(NotImplementedError, match=err_msg):
    f(False, df)
with pytest.raises(NotImplementedError, match=err_msg):
    f(df, True)
```

## Next Steps


---

*Source: test_expressions.py:294 | Complexity: Advanced | Last updated: 2026-06-02*