# How To: Attribute Access

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test attribute access

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas._config`
- `pandas._config.config`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign holder = value

```python
holder = []
```

**Verification:**
```python
assert options.a == 0
```

### Step 2: Call cf.register_option()

```python
cf.register_option('a', 0)
```

**Verification:**
```python
assert options.a == 15
```

### Step 3: Call cf.register_option()

```python
cf.register_option('c', 0, cb=f3)
```

**Verification:**
```python
assert cf.get_option('a') == 500
```

### Step 4: Assign options = value

```python
options = cf.options
```

**Verification:**
```python
assert options.a == cf.get_option('a', 0)
```

### Step 5: Assign options.a = 500

```python
options.a = 500
```

**Verification:**
```python
assert len(holder) == 1
```

### Step 6: Call cf.reset_option()

```python
cf.reset_option('a')
```

**Verification:**
```python
assert options.a == cf.get_option('a', 0)
```

### Step 7: Assign msg = 'You can only set the value of existing options'

```python
msg = 'You can only set the value of existing options'
```

### Step 8: Assign options.c = 1

```python
options.c = 1
```

**Verification:**
```python
assert len(holder) == 1
```

### Step 9: Call holder.append()

```python
holder.append(True)
```

**Verification:**
```python
assert options.a == 15
```

### Step 10: Assign options.b = 1

```python
options.b = 1
```

### Step 11: Assign options.display = 1

```python
options.display = 1
```


## Complete Example

```python
# Workflow
holder = []

def f3(key):
    holder.append(True)
cf.register_option('a', 0)
cf.register_option('c', 0, cb=f3)
options = cf.options
assert options.a == 0
with cf.option_context('a', 15):
    assert options.a == 15
options.a = 500
assert cf.get_option('a') == 500
cf.reset_option('a')
assert options.a == cf.get_option('a', 0)
msg = 'You can only set the value of existing options'
with pytest.raises(OptionError, match=msg):
    options.b = 1
with pytest.raises(OptionError, match=msg):
    options.display = 1
options.c = 1
assert len(holder) == 1
```

## Next Steps


---

*Source: test_config.py:380 | Complexity: Advanced | Last updated: 2026-06-02*