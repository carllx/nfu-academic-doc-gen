# How To: Codes Dtypes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test codes dtypes

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign result = Categorical(...)

```python
result = Categorical(['foo', 'bar', 'baz'])
```

**Verification:**
```python
assert result.codes.dtype == 'int8'
```

### Step 2: Assign result = Categorical(...)

```python
result = Categorical([f'foo{i:05d}' for i in range(400)])
```

**Verification:**
```python
assert result.codes.dtype == 'int16'
```

### Step 3: Assign result = Categorical(...)

```python
result = Categorical([f'foo{i:05d}' for i in range(40000)])
```

**Verification:**
```python
assert result.codes.dtype == 'int32'
```

### Step 4: Assign result = Categorical(...)

```python
result = Categorical(['foo', 'bar', 'baz'])
```

**Verification:**
```python
assert result.codes.dtype == 'int8'
```

### Step 5: Assign result = result.add_categories(...)

```python
result = result.add_categories([f'foo{i:05d}' for i in range(400)])
```

**Verification:**
```python
assert result.codes.dtype == 'int16'
```

### Step 6: Assign result = result.remove_categories(...)

```python
result = result.remove_categories([f'foo{i:05d}' for i in range(300)])
```

**Verification:**
```python
assert result.codes.dtype == 'int8'
```


## Complete Example

```python
# Workflow
result = Categorical(['foo', 'bar', 'baz'])
assert result.codes.dtype == 'int8'
result = Categorical([f'foo{i:05d}' for i in range(400)])
assert result.codes.dtype == 'int16'
result = Categorical([f'foo{i:05d}' for i in range(40000)])
assert result.codes.dtype == 'int32'
result = Categorical(['foo', 'bar', 'baz'])
assert result.codes.dtype == 'int8'
result = result.add_categories([f'foo{i:05d}' for i in range(400)])
assert result.codes.dtype == 'int16'
result = result.remove_categories([f'foo{i:05d}' for i in range(300)])
assert result.codes.dtype == 'int8'
```

## Next Steps


---

*Source: test_dtypes.py:99 | Complexity: Intermediate | Last updated: 2026-06-02*