# How To: Validation

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test validation

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
cf.register_option('a', 1, 'doc', validator=cf.is_int)
```

### Step 2: Call cf.register_option()

```python
cf.register_option('d', 1, 'doc', validator=cf.is_nonnegative_int)
```

### Step 3: Call cf.register_option()

```python
cf.register_option('b.c', 'hullo', 'doc2', validator=cf.is_text)
```

### Step 4: Assign msg = "Value must have type '<class 'int'>'"

```python
msg = "Value must have type '<class 'int'>'"
```

### Step 5: Call cf.set_option()

```python
cf.set_option('a', 2)
```

### Step 6: Call cf.set_option()

```python
cf.set_option('b.c', 'wurld')
```

### Step 7: Call cf.set_option()

```python
cf.set_option('d', 2)
```

### Step 8: Call cf.set_option()

```python
cf.set_option('d', None)
```

### Step 9: Assign msg = 'Value must be a nonnegative integer or None'

```python
msg = 'Value must be a nonnegative integer or None'
```

### Step 10: Assign msg = "Value must be an instance of <class 'str'>\\|<class 'bytes'>"

```python
msg = "Value must be an instance of <class 'str'>\\|<class 'bytes'>"
```

### Step 11: Assign validator = cf.is_one_of_factory(...)

```python
validator = cf.is_one_of_factory([None, cf.is_callable])
```

### Step 12: Call cf.register_option()

```python
cf.register_option('b', lambda: None, 'doc', validator=validator)
```

### Step 13: Call cf.set_option()

```python
cf.set_option('b', '%.1f'.format)
```

### Step 14: Call cf.set_option()

```python
cf.set_option('b', None)
```

### Step 15: Call cf.register_option()

```python
cf.register_option('a.b.c.d2', 'NO', 'doc', validator=cf.is_int)
```

### Step 16: Call cf.set_option()

```python
cf.set_option('a', None)
```

### Step 17: Call cf.set_option()

```python
cf.set_option('a', 'ab')
```

### Step 18: Call cf.register_option()

```python
cf.register_option('a.b.c.d3', 'NO', 'doc', validator=cf.is_nonnegative_int)
```

### Step 19: Call cf.register_option()

```python
cf.register_option('a.b.c.d3', -2, 'doc', validator=cf.is_nonnegative_int)
```

### Step 20: Call cf.set_option()

```python
cf.set_option('b.c', 1)
```

### Step 21: Call cf.set_option()

```python
cf.set_option('b', '%.1f')
```


## Complete Example

```python
# Workflow
cf.register_option('a', 1, 'doc', validator=cf.is_int)
cf.register_option('d', 1, 'doc', validator=cf.is_nonnegative_int)
cf.register_option('b.c', 'hullo', 'doc2', validator=cf.is_text)
msg = "Value must have type '<class 'int'>'"
with pytest.raises(ValueError, match=msg):
    cf.register_option('a.b.c.d2', 'NO', 'doc', validator=cf.is_int)
cf.set_option('a', 2)
cf.set_option('b.c', 'wurld')
cf.set_option('d', 2)
cf.set_option('d', None)
with pytest.raises(ValueError, match=msg):
    cf.set_option('a', None)
with pytest.raises(ValueError, match=msg):
    cf.set_option('a', 'ab')
msg = 'Value must be a nonnegative integer or None'
with pytest.raises(ValueError, match=msg):
    cf.register_option('a.b.c.d3', 'NO', 'doc', validator=cf.is_nonnegative_int)
with pytest.raises(ValueError, match=msg):
    cf.register_option('a.b.c.d3', -2, 'doc', validator=cf.is_nonnegative_int)
msg = "Value must be an instance of <class 'str'>\\|<class 'bytes'>"
with pytest.raises(ValueError, match=msg):
    cf.set_option('b.c', 1)
validator = cf.is_one_of_factory([None, cf.is_callable])
cf.register_option('b', lambda: None, 'doc', validator=validator)
cf.set_option('b', '%.1f'.format)
cf.set_option('b', None)
with pytest.raises(ValueError, match='Value must be a callable'):
    cf.set_option('b', '%.1f')
```

## Next Steps


---

*Source: test_config.py:196 | Complexity: Advanced | Last updated: 2026-06-02*