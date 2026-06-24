# How To: Agg Callables

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test agg callables

## Prerequisites

**Required Modules:**
- `datetime`
- `functools`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.formats.printing`
- `pandas.tests.extension.decimal.array`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame.astype(...)

```python
df = DataFrame({'foo': [1, 2], 'bar': [3, 4]}).astype(np.int64)
```

### Step 2: Assign equiv_callables = value

```python
equiv_callables = [sum, np.sum, lambda x: sum(x), lambda x: x.sum(), partial(sum), fn_class()]
```

### Step 3: Assign expected = df.groupby.agg(...)

```python
expected = df.groupby('foo').agg('sum')
```

### Step 4: Assign warn = value

```python
warn = FutureWarning if ecall is sum or ecall is np.sum else None
```

### Step 5: Assign msg = 'using DataFrameGroupBy.sum'

```python
msg = 'using DataFrameGroupBy.sum'
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign result = df.groupby.agg(...)

```python
result = df.groupby('foo').agg(ecall)
```


## Complete Example

```python
# Workflow
df = DataFrame({'foo': [1, 2], 'bar': [3, 4]}).astype(np.int64)

class fn_class:

    def __call__(self, x):
        return sum(x)
equiv_callables = [sum, np.sum, lambda x: sum(x), lambda x: x.sum(), partial(sum), fn_class()]
expected = df.groupby('foo').agg('sum')
for ecall in equiv_callables:
    warn = FutureWarning if ecall is sum or ecall is np.sum else None
    msg = 'using DataFrameGroupBy.sum'
    with tm.assert_produces_warning(warn, match=msg):
        result = df.groupby('foo').agg(ecall)
    tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_other.py:395 | Complexity: Intermediate | Last updated: 2026-06-02*