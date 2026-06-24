# How To: Display Max Dir Items

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test display max dir items

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

### Step 1: Assign columns = value

```python
columns = ['a' + str(i) for i in range(420)]
```

**Verification:**
```python
assert 'a99' in dir(df)
```

### Step 2: Assign values = value

```python
values = [range(420), range(420)]
```

**Verification:**
```python
assert 'a100' not in dir(df)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(values, columns=columns)
```

**Verification:**
```python
assert 'a299' in dir(df)
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(values, columns=columns)
```

**Verification:**
```python
assert 'a300' not in dir(df)
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame(values, columns=columns)
```

**Verification:**
```python
assert 'a419' in dir(df)
```


## Complete Example

```python
# Workflow
columns = ['a' + str(i) for i in range(420)]
values = [range(420), range(420)]
df = DataFrame(values, columns=columns)
assert 'a99' in dir(df)
assert 'a100' not in dir(df)
with option_context('display.max_dir_items', 300):
    df = DataFrame(values, columns=columns)
    assert 'a299' in dir(df)
    assert 'a300' not in dir(df)
with option_context('display.max_dir_items', None):
    df = DataFrame(values, columns=columns)
    assert 'a419' in dir(df)
```

## Next Steps


---

*Source: test_api.py:89 | Complexity: Intermediate | Last updated: 2026-06-02*