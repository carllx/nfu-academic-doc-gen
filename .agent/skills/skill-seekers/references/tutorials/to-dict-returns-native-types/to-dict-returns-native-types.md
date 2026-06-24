# How To: To Dict Returns Native Types

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test to dict returns native types

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: orient, data, expected_types
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(data)
```

**Verification:**
```python
assertion_iterator = ((i, key, value) for key, index_value_map in result.items() for i, value in index_value_map.items())
```

### Step 2: Assign result = df.to_dict(...)

```python
result = df.to_dict(orient)
```

**Verification:**
```python
assertion_iterator = ((i, key, value) for key, values in result.items() for i, value in enumerate(values))
```

### Step 3: Assign assertion_iterator = value

```python
assertion_iterator = ((i, key, value) for key, index_value_map in result.items() for i, value in index_value_map.items())
```

**Verification:**
```python
assertion_iterator = ((i, key, result['data'][i][j]) for i in result['index'] for j, key in enumerate(result['columns']))
```

### Step 4: Assign assertion_iterator = value

```python
assertion_iterator = ((i, key, value) for key, values in result.items() for i, value in enumerate(values))
```

**Verification:**
```python
assertion_iterator = ((i, key, value) for i, record in enumerate(result) for key, value in record.items())
```

### Step 5: Assign assertion_iterator = value

```python
assertion_iterator = ((i, key, result['data'][i][j]) for i in result['index'] for j, key in enumerate(result['columns']))
```

**Verification:**
```python
assertion_iterator = ((i, key, value) for i, record in result.items() for key, value in record.items())
```

### Step 6: Assign assertion_iterator = value

```python
assertion_iterator = ((i, key, value) for i, record in enumerate(result) for key, value in record.items())
```

**Verification:**
```python
assert value == data[key][i]
```

### Step 7: Assign assertion_iterator = value

```python
assertion_iterator = ((i, key, value) for i, record in result.items() for key, value in record.items())
```

**Verification:**
```python
assert type(value) is expected_types[key][i]
```


## Complete Example

```python
# Setup
# Fixtures: orient, data, expected_types

# Workflow
df = DataFrame(data)
result = df.to_dict(orient)
if orient == 'dict':
    assertion_iterator = ((i, key, value) for key, index_value_map in result.items() for i, value in index_value_map.items())
elif orient == 'list':
    assertion_iterator = ((i, key, value) for key, values in result.items() for i, value in enumerate(values))
elif orient in {'split', 'tight'}:
    assertion_iterator = ((i, key, result['data'][i][j]) for i in result['index'] for j, key in enumerate(result['columns']))
elif orient == 'records':
    assertion_iterator = ((i, key, value) for i, record in enumerate(result) for key, value in record.items())
elif orient == 'index':
    assertion_iterator = ((i, key, value) for i, record in result.items() for key, value in record.items())
for i, key, value in assertion_iterator:
    assert value == data[key][i]
    assert type(value) is expected_types[key][i]
```

## Next Steps


---

*Source: test_to_dict.py:412 | Complexity: Intermediate | Last updated: 2026-06-02*