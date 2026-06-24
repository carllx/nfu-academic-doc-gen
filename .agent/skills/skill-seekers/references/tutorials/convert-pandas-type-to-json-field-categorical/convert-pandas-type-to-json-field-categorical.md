# How To: Convert Pandas Type To Json Field Categorical

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test convert pandas type to json field categorical

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
# Fixtures: kind, ordered
```

## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = ['a', 'b', 'c']
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign result = convert_pandas_type_to_json_field(...)

```python
result = convert_pandas_type_to_json_field(arr)
```

### Step 3: Assign expected = value

```python
expected = {'name': 'cats', 'type': 'any', 'constraints': {'enum': data}, 'ordered': ordered}
```

**Verification:**
```python
assert result == expected
```

### Step 4: Assign arr = pd.Series(...)

```python
arr = pd.Series(kind(data, ordered=ordered), name='cats')
```

### Step 5: Assign arr = kind(...)

```python
arr = kind(data, ordered=ordered, name='cats')
```


## Complete Example

```python
# Setup
# Fixtures: kind, ordered

# Workflow
data = ['a', 'b', 'c']
if kind is pd.Categorical:
    arr = pd.Series(kind(data, ordered=ordered), name='cats')
elif kind is pd.CategoricalIndex:
    arr = kind(data, ordered=ordered, name='cats')
result = convert_pandas_type_to_json_field(arr)
expected = {'name': 'cats', 'type': 'any', 'constraints': {'enum': data}, 'ordered': ordered}
assert result == expected
```

## Next Steps


---

*Source: test_json_table_schema.py:505 | Complexity: Intermediate | Last updated: 2026-06-02*