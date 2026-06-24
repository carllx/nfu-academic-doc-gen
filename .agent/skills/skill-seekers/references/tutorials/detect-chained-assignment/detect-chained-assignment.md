# How To: Detect Chained Assignment

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test detect chained assignment

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign a = value

```python
a = [12, 23]
```

### Step 2: Assign b = value

```python
b = [123, None]
```

### Step 3: Assign c = value

```python
c = [1234, 2345]
```

### Step 4: Assign d = value

```python
d = [12345, 23456]
```

### Step 5: Assign tuples = value

```python
tuples = [('eyes', 'left'), ('eyes', 'right'), ('ears', 'left'), ('ears', 'right')]
```

### Step 6: Assign events = value

```python
events = {('eyes', 'left'): a, ('eyes', 'right'): b, ('ears', 'left'): c, ('ears', 'right'): d}
```

### Step 7: Assign multiind = MultiIndex.from_tuples(...)

```python
multiind = MultiIndex.from_tuples(tuples, names=['part', 'side'])
```

### Step 8: Assign zed = DataFrame(...)

```python
zed = DataFrame(events, index=['a', 'b'], columns=multiind)
```

### Step 9: Call unknown.fillna()

```python
zed['eyes']['right'].fillna(value=555, inplace=True)
```

### Step 10: Assign msg = 'A value is trying to be set on a copy of a slice from a DataFrame'

```python
msg = 'A value is trying to be set on a copy of a slice from a DataFrame'
```

### Step 11: Call unknown.fillna()

```python
zed['eyes']['right'].fillna(value=555, inplace=True)
```

### Step 12: Call unknown.fillna()

```python
zed['eyes']['right'].fillna(value=555, inplace=True)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, warn_copy_on_write

# Workflow
a = [12, 23]
b = [123, None]
c = [1234, 2345]
d = [12345, 23456]
tuples = [('eyes', 'left'), ('eyes', 'right'), ('ears', 'left'), ('ears', 'right')]
events = {('eyes', 'left'): a, ('eyes', 'right'): b, ('ears', 'left'): c, ('ears', 'right'): d}
multiind = MultiIndex.from_tuples(tuples, names=['part', 'side'])
zed = DataFrame(events, index=['a', 'b'], columns=multiind)
if using_copy_on_write:
    with tm.raises_chained_assignment_error():
        zed['eyes']['right'].fillna(value=555, inplace=True)
elif warn_copy_on_write:
    with tm.assert_produces_warning(None):
        zed['eyes']['right'].fillna(value=555, inplace=True)
else:
    msg = 'A value is trying to be set on a copy of a slice from a DataFrame'
    with pytest.raises(SettingWithCopyError, match=msg):
        with tm.assert_produces_warning(None):
            zed['eyes']['right'].fillna(value=555, inplace=True)
```

## Next Steps


---

*Source: test_chaining_and_caching.py:16 | Complexity: Advanced | Last updated: 2026-06-02*