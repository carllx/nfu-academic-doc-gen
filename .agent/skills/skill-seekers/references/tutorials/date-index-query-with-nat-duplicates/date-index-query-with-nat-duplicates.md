# How To: Date Index Query With Nat Duplicates

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test date index query with NaT duplicates

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

### Step 1: Assign n = 10

```python
n = 10
```

**Verification:**
```python
assert return_value is None
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((n, 3)))
```

### Step 3: Assign unknown = date_range(...)

```python
df['dates1'] = date_range('1/1/2012', periods=n)
```

### Step 4: Assign unknown = date_range(...)

```python
df['dates3'] = date_range('1/1/2014', periods=n)
```

### Step 5: Assign unknown = value

```python
df.loc[np.random.default_rng(2).random(n) > 0.5, 'dates1'] = pd.NaT
```

### Step 6: Assign return_value = df.set_index(...)

```python
return_value = df.set_index('dates1', inplace=True, drop=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 7: Assign msg = "'BoolOp' nodes are not implemented"

```python
msg = "'BoolOp' nodes are not implemented"
```

### Step 8: Call df.query()

```python
df.query('index < 20130101 < dates3', engine=engine, parser=parser)
```


## Complete Example

```python
# Workflow
n = 10
df = DataFrame(np.random.default_rng(2).standard_normal((n, 3)))
df['dates1'] = date_range('1/1/2012', periods=n)
df['dates3'] = date_range('1/1/2014', periods=n)
df.loc[np.random.default_rng(2).random(n) > 0.5, 'dates1'] = pd.NaT
return_value = df.set_index('dates1', inplace=True, drop=True)
assert return_value is None
msg = "'BoolOp' nodes are not implemented"
with pytest.raises(NotImplementedError, match=msg):
    df.query('index < 20130101 < dates3', engine=engine, parser=parser)
```

## Next Steps


---

*Source: test_query_eval.py:856 | Complexity: Advanced | Last updated: 2026-06-02*