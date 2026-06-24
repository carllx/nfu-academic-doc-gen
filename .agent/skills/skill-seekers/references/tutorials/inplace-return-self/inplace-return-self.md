# How To: Inplace Return Self

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test inplace return self

## Prerequisites

**Required Modules:**
- `copy`
- `inspect`
- `pydoc`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._config.config`
- `pandas.compat`
- `pandas`
- `pandas`
- `pandas._testing`
- `IPython.core.completer`


## Step-by-Step Guide

### Step 1: Assign data = DataFrame(...)

```python
data = DataFrame({'a': ['foo', 'bar', 'baz', 'qux'], 'b': [0, 0, 1, 1], 'c': [1, 2, 3, 4]})
```

**Verification:**
```python
assert result is None
```

### Step 2: Assign f = value

```python
f = lambda x: x.set_index('a', inplace=True)
```

### Step 3: Call _check_f()

```python
_check_f(data.copy(), f)
```

### Step 4: Assign f = value

```python
f = lambda x: x.reset_index(inplace=True)
```

### Step 5: Call _check_f()

```python
_check_f(data.set_index('a'), f)
```

### Step 6: Assign f = value

```python
f = lambda x: x.drop_duplicates(inplace=True)
```

### Step 7: Call _check_f()

```python
_check_f(data.copy(), f)
```

### Step 8: Assign f = value

```python
f = lambda x: x.sort_values('b', inplace=True)
```

### Step 9: Call _check_f()

```python
_check_f(data.copy(), f)
```

### Step 10: Assign f = value

```python
f = lambda x: x.sort_index(inplace=True)
```

### Step 11: Call _check_f()

```python
_check_f(data.copy(), f)
```

### Step 12: Assign f = value

```python
f = lambda x: x.fillna(0, inplace=True)
```

### Step 13: Call _check_f()

```python
_check_f(data.copy(), f)
```

### Step 14: Assign f = value

```python
f = lambda x: x.replace(1, 0, inplace=True)
```

### Step 15: Call _check_f()

```python
_check_f(data.copy(), f)
```

### Step 16: Assign f = value

```python
f = lambda x: x.rename({1: 'foo'}, inplace=True)
```

### Step 17: Call _check_f()

```python
_check_f(data.copy(), f)
```

### Step 18: Assign d = value

```python
d = data.copy()['c']
```

### Step 19: Assign f = value

```python
f = lambda x: x.reset_index(inplace=True, drop=True)
```

### Step 20: Call _check_f()

```python
_check_f(data.set_index('a')['c'], f)
```

### Step 21: Assign f = value

```python
f = lambda x: x.fillna(0, inplace=True)
```

### Step 22: Call _check_f()

```python
_check_f(d.copy(), f)
```

### Step 23: Assign f = value

```python
f = lambda x: x.replace(1, 0, inplace=True)
```

### Step 24: Call _check_f()

```python
_check_f(d.copy(), f)
```

### Step 25: Assign f = value

```python
f = lambda x: x.rename({1: 'foo'}, inplace=True)
```

### Step 26: Call _check_f()

```python
_check_f(d.copy(), f)
```

### Step 27: Assign result = f(...)

```python
result = f(base)
```

**Verification:**
```python
assert result is None
```


## Complete Example

```python
# Workflow
data = DataFrame({'a': ['foo', 'bar', 'baz', 'qux'], 'b': [0, 0, 1, 1], 'c': [1, 2, 3, 4]})

def _check_f(base, f):
    result = f(base)
    assert result is None
f = lambda x: x.set_index('a', inplace=True)
_check_f(data.copy(), f)
f = lambda x: x.reset_index(inplace=True)
_check_f(data.set_index('a'), f)
f = lambda x: x.drop_duplicates(inplace=True)
_check_f(data.copy(), f)
f = lambda x: x.sort_values('b', inplace=True)
_check_f(data.copy(), f)
f = lambda x: x.sort_index(inplace=True)
_check_f(data.copy(), f)
f = lambda x: x.fillna(0, inplace=True)
_check_f(data.copy(), f)
f = lambda x: x.replace(1, 0, inplace=True)
_check_f(data.copy(), f)
f = lambda x: x.rename({1: 'foo'}, inplace=True)
_check_f(data.copy(), f)
d = data.copy()['c']
f = lambda x: x.reset_index(inplace=True, drop=True)
_check_f(data.set_index('a')['c'], f)
f = lambda x: x.fillna(0, inplace=True)
_check_f(d.copy(), f)
f = lambda x: x.replace(1, 0, inplace=True)
_check_f(d.copy(), f)
f = lambda x: x.rename({1: 'foo'}, inplace=True)
_check_f(d.copy(), f)
```

## Next Steps


---

*Source: test_api.py:229 | Complexity: Advanced | Last updated: 2026-06-02*