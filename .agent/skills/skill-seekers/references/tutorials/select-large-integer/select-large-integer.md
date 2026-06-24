# How To: Select Large Integer

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test select large integer

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas.tests.io.pytables.common`
- `pandas.io.pytables`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: Assign path = value

```python
path = tmp_path / 'large_int.h5'
```

**Verification:**
```python
assert expected == result
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(zip(['a', 'b', 'c', 'd'], [-9223372036854775801, -9223372036854775802, -9223372036854775803, 123]), columns=['x', 'y'])
```

### Step 3: Assign expected = value

```python
expected = df['y'][0]
```

**Verification:**
```python
assert expected == result
```

### Step 4: Call s.append()

```python
s.append('data', df, data_columns=True, index=False)
```

### Step 5: Assign result = s.select.get.get(...)

```python
result = s.select('data', where='y==-9223372036854775801').get('y').get(0)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
path = tmp_path / 'large_int.h5'
df = DataFrame(zip(['a', 'b', 'c', 'd'], [-9223372036854775801, -9223372036854775802, -9223372036854775803, 123]), columns=['x', 'y'])
with HDFStore(path) as s:
    s.append('data', df, data_columns=True, index=False)
    result = s.select('data', where='y==-9223372036854775801').get('y').get(0)
expected = df['y'][0]
assert expected == result
```

## Next Steps


---

*Source: test_select.py:1031 | Complexity: Intermediate | Last updated: 2026-06-02*