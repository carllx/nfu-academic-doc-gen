# How To: Labels Dtypes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test labels dtypes

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.core.dtypes.cast`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign i = MultiIndex.from_tuples(...)

```python
i = MultiIndex.from_tuples([('A', 1), ('A', 2)])
```

**Verification:**
```python
assert i.codes[0].dtype == 'int8'
```

### Step 2: Assign i = MultiIndex.from_product(...)

```python
i = MultiIndex.from_product([['a'], range(40)])
```

**Verification:**
```python
assert i.codes[1].dtype == 'int8'
```

### Step 3: Assign i = MultiIndex.from_product(...)

```python
i = MultiIndex.from_product([['a'], range(400)])
```

**Verification:**
```python
assert i.codes[1].dtype == 'int8'
```

### Step 4: Assign i = MultiIndex.from_product(...)

```python
i = MultiIndex.from_product([['a'], range(40000)])
```

**Verification:**
```python
assert i.codes[1].dtype == 'int16'
```

### Step 5: Assign i = MultiIndex.from_product(...)

```python
i = MultiIndex.from_product([['a'], range(1000)])
```

**Verification:**
```python
assert i.codes[1].dtype == 'int32'
```


## Complete Example

```python
# Workflow
i = MultiIndex.from_tuples([('A', 1), ('A', 2)])
assert i.codes[0].dtype == 'int8'
assert i.codes[1].dtype == 'int8'
i = MultiIndex.from_product([['a'], range(40)])
assert i.codes[1].dtype == 'int8'
i = MultiIndex.from_product([['a'], range(400)])
assert i.codes[1].dtype == 'int16'
i = MultiIndex.from_product([['a'], range(40000)])
assert i.codes[1].dtype == 'int32'
i = MultiIndex.from_product([['a'], range(1000)])
assert (i.codes[0] >= 0).all()
assert (i.codes[1] >= 0).all()
```

## Next Steps


---

*Source: test_integrity.py:20 | Complexity: Intermediate | Last updated: 2026-06-02*