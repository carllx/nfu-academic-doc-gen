# How To: Get Callable Name

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get callable name

## Prerequisites

**Required Modules:**
- `collections`
- `functools`
- `string`
- `subprocess`
- `sys`
- `textwrap`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.common`
- `pandas.util.version`


## Step-by-Step Guide

### Step 1: Assign getname = value

```python
getname = com.get_callable_name
```

**Verification:**
```python
assert getname(fn) == 'fn'
```

### Step 2: Assign lambda_ = value

```python
lambda_ = lambda x: x
```

**Verification:**
```python
assert getname(lambda_)
```

### Step 3: Assign part1 = partial(...)

```python
part1 = partial(fn)
```

**Verification:**
```python
assert getname(part1) == 'fn'
```

### Step 4: Assign part2 = partial(...)

```python
part2 = partial(part1)
```

**Verification:**
```python
assert getname(part2) == 'fn'
```


## Complete Example

```python
# Workflow
getname = com.get_callable_name

def fn(x):
    return x
lambda_ = lambda x: x
part1 = partial(fn)
part2 = partial(part1)

class somecall:

    def __call__(self):
        raise NotImplementedError
assert getname(fn) == 'fn'
assert getname(lambda_)
assert getname(part1) == 'fn'
assert getname(part2) == 'fn'
assert getname(somecall()) == 'somecall'
assert getname(1) is None
```

## Next Steps


---

*Source: test_common.py:19 | Complexity: Intermediate | Last updated: 2026-06-02*