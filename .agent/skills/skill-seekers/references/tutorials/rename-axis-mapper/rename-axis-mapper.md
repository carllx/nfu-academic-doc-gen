# How To: Rename Axis Mapper

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rename axis mapper

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign mi = MultiIndex.from_product(...)

```python
mi = MultiIndex.from_product([['a', 'b', 'c'], [1, 2]], names=['ll', 'nn'])
```

**Verification:**
```python
assert result.index.names == ['foo', 'nn']
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(list(range(len(mi))), index=mi)
```

**Verification:**
```python
assert result.index.names == ['LL', 'NN']
```

### Step 3: Assign result = ser.rename_axis(...)

```python
result = ser.rename_axis(index={'ll': 'foo'})
```

**Verification:**
```python
assert result.index.names == ['foo', 'goo']
```

### Step 4: Assign result = ser.rename_axis(...)

```python
result = ser.rename_axis(index=str.upper, axis=0)
```

**Verification:**
```python
assert result.index.names == ['LL', 'NN']
```

### Step 5: Assign result = ser.rename_axis(...)

```python
result = ser.rename_axis(index=['foo', 'goo'])
```

**Verification:**
```python
assert result.index.names == ['foo', 'goo']
```

### Step 6: Call ser.rename_axis()

```python
ser.rename_axis(columns='wrong')
```


## Complete Example

```python
# Workflow
mi = MultiIndex.from_product([['a', 'b', 'c'], [1, 2]], names=['ll', 'nn'])
ser = Series(list(range(len(mi))), index=mi)
result = ser.rename_axis(index={'ll': 'foo'})
assert result.index.names == ['foo', 'nn']
result = ser.rename_axis(index=str.upper, axis=0)
assert result.index.names == ['LL', 'NN']
result = ser.rename_axis(index=['foo', 'goo'])
assert result.index.names == ['foo', 'goo']
with pytest.raises(TypeError, match='unexpected'):
    ser.rename_axis(columns='wrong')
```

## Next Steps


---

*Source: test_rename_axis.py:12 | Complexity: Intermediate | Last updated: 2026-06-02*