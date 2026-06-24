# How To: Validate Bool Args

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test validate bool args

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas.core.frame`

**Setup Required:**
```python
# Fixtures: dataframe, func, inplace
```

## Step-by-Step Guide

### Step 1: Assign msg = 'For argument "inplace" expected type bool'

```python
msg = 'For argument "inplace" expected type bool'
```

### Step 2: Assign kwargs = value

```python
kwargs = {'inplace': inplace}
```

### Step 3: Assign unknown = 'a > b'

```python
kwargs['expr'] = 'a > b'
```

### Step 4: Call getattr()

```python
getattr(dataframe, func)(**kwargs)
```

### Step 5: Assign unknown = 'a + b'

```python
kwargs['expr'] = 'a + b'
```

### Step 6: Assign unknown = value

```python
kwargs['keys'] = ['a']
```

### Step 7: Assign unknown = value

```python
kwargs['by'] = ['a']
```


## Complete Example

```python
# Setup
# Fixtures: dataframe, func, inplace

# Workflow
msg = 'For argument "inplace" expected type bool'
kwargs = {'inplace': inplace}
if func == 'query':
    kwargs['expr'] = 'a > b'
elif func == 'eval':
    kwargs['expr'] = 'a + b'
elif func == 'set_index':
    kwargs['keys'] = ['a']
elif func == 'sort_values':
    kwargs['by'] = ['a']
with pytest.raises(ValueError, match=msg):
    getattr(dataframe, func)(**kwargs)
```

## Next Steps


---

*Source: test_validate.py:27 | Complexity: Intermediate | Last updated: 2026-06-02*