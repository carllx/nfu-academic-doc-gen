# How To: Set Name Attribute

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set name attribute

## Prerequisites

**Required Modules:**
- `datetime`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([1, 2, 3])
```

**Verification:**
```python
assert ser.name == name
```

### Step 2: Assign ser2 = Series(...)

```python
ser2 = Series([1, 2, 3], name='bar')
```

**Verification:**
```python
assert ser2.name == name
```

### Step 3: Assign ser.name = name

```python
ser.name = name
```

**Verification:**
```python
assert ser.name == name
```

### Step 4: Assign ser2.name = name

```python
ser2.name = name
```

**Verification:**
```python
assert ser2.name == name
```


## Complete Example

```python
# Workflow
ser = Series([1, 2, 3])
ser2 = Series([1, 2, 3], name='bar')
for name in [7, 7.0, 'name', datetime(2001, 1, 1), (1,), 'א']:
    ser.name = name
    assert ser.name == name
    ser2.name = name
    assert ser2.name == name
```

## Next Steps


---

*Source: test_set_name.py:14 | Complexity: Intermediate | Last updated: 2026-06-02*