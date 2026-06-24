# How To: Register Option

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test register option

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas._config`
- `pandas._config.config`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Call cf.register_option()

```python
cf.register_option('a', 1, 'doc')
```

### Step 2: Assign msg = "Option 'a' has already been registered"

```python
msg = "Option 'a' has already been registered"
```

### Step 3: Assign msg = "Path prefix to option 'a' is already an option"

```python
msg = "Path prefix to option 'a' is already an option"
```

### Step 4: Assign msg = 'for is a python keyword'

```python
msg = 'for is a python keyword'
```

### Step 5: Assign msg = 'oh my goddess! is not a valid identifier'

```python
msg = 'oh my goddess! is not a valid identifier'
```

### Step 6: Call cf.register_option()

```python
cf.register_option('k.b.c.d1', 1, 'doc')
```

### Step 7: Call cf.register_option()

```python
cf.register_option('k.b.c.d2', 1, 'doc')
```

### Step 8: Call cf.register_option()

```python
cf.register_option('a', 1, 'doc')
```

### Step 9: Call cf.register_option()

```python
cf.register_option('a.b.c.d1', 1, 'doc')
```

### Step 10: Call cf.register_option()

```python
cf.register_option('a.b.c.d2', 1, 'doc')
```

### Step 11: Call cf.register_option()

```python
cf.register_option('for', 0)
```

### Step 12: Call cf.register_option()

```python
cf.register_option('a.for.b', 0)
```

### Step 13: Call cf.register_option()

```python
cf.register_option('Oh my Goddess!', 0)
```


## Complete Example

```python
# Workflow
cf.register_option('a', 1, 'doc')
msg = "Option 'a' has already been registered"
with pytest.raises(OptionError, match=msg):
    cf.register_option('a', 1, 'doc')
msg = "Path prefix to option 'a' is already an option"
with pytest.raises(OptionError, match=msg):
    cf.register_option('a.b.c.d1', 1, 'doc')
with pytest.raises(OptionError, match=msg):
    cf.register_option('a.b.c.d2', 1, 'doc')
msg = 'for is a python keyword'
with pytest.raises(ValueError, match=msg):
    cf.register_option('for', 0)
with pytest.raises(ValueError, match=msg):
    cf.register_option('a.for.b', 0)
msg = 'oh my goddess! is not a valid identifier'
with pytest.raises(ValueError, match=msg):
    cf.register_option('Oh my Goddess!', 0)
cf.register_option('k.b.c.d1', 1, 'doc')
cf.register_option('k.b.c.d2', 1, 'doc')
```

## Next Steps


---

*Source: test_config.py:42 | Complexity: Advanced | Last updated: 2026-06-02*