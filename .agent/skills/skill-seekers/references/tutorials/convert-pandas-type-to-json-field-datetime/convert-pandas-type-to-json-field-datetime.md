# How To: Convert Pandas Type To Json Field Datetime

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test convert pandas type to json field datetime

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `io`
- `json`
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.json._table_schema`

**Setup Required:**
```python
# Fixtures: dt_args, extra_exp, wrapper
```

## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = [1.0, 2.0, 3.0]
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign data = pd.to_datetime(...)

```python
data = pd.to_datetime(data, **dt_args)
```

### Step 3: Assign result = convert_pandas_type_to_json_field(...)

```python
result = convert_pandas_type_to_json_field(data)
```

### Step 4: Assign expected = value

```python
expected = {'name': 'values', 'type': 'datetime'}
```

### Step 5: Call expected.update()

```python
expected.update(extra_exp)
```

**Verification:**
```python
assert result == expected
```

### Step 6: Assign data = pd.Series(...)

```python
data = pd.Series(data, name='values')
```


## Complete Example

```python
# Setup
# Fixtures: dt_args, extra_exp, wrapper

# Workflow
data = [1.0, 2.0, 3.0]
data = pd.to_datetime(data, **dt_args)
if wrapper is pd.Series:
    data = pd.Series(data, name='values')
result = convert_pandas_type_to_json_field(data)
expected = {'name': 'values', 'type': 'datetime'}
expected.update(extra_exp)
assert result == expected
```

## Next Steps


---

*Source: test_json_table_schema.py:485 | Complexity: Intermediate | Last updated: 2026-06-02*