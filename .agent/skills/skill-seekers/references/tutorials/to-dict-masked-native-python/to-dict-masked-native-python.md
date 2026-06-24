# How To: To Dict Masked Native Python

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to dict masked native python

## Prerequisites

**Required Modules:**
- `collections`
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': Series([1, 2], dtype='Int64'), 'B': 1})
```

**Verification:**
```python
assert isinstance(result[0]['a'], int)
```

### Step 2: Assign result = df.to_dict(...)

```python
result = df.to_dict(orient='records')
```

**Verification:**
```python
assert isinstance(result[0]['a'], int)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'a': Series([1, NA], dtype='Int64'), 'B': 1})
```

### Step 4: Assign result = df.to_dict(...)

```python
result = df.to_dict(orient='records')
```

**Verification:**
```python
assert isinstance(result[0]['a'], int)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': Series([1, 2], dtype='Int64'), 'B': 1})
result = df.to_dict(orient='records')
assert isinstance(result[0]['a'], int)
df = DataFrame({'a': Series([1, NA], dtype='Int64'), 'B': 1})
result = df.to_dict(orient='records')
assert isinstance(result[0]['a'], int)
```

## Next Steps


---

*Source: test_to_dict.py:506 | Complexity: Intermediate | Last updated: 2026-06-02*