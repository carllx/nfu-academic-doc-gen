# How To: Mean Mixed String Decimal

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mean mixed string decimal

## Prerequisites

**Required Modules:**
- `datetime`
- `decimal`
- `re`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`


## Step-by-Step Guide

### Step 1: Assign d = value

```python
d = [{'A': 2, 'B': None, 'C': Decimal('628.00')}, {'A': 1, 'B': None, 'C': Decimal('383.00')}, {'A': 3, 'B': None, 'C': Decimal('651.00')}, {'A': 2, 'B': None, 'C': Decimal('575.00')}, {'A': 4, 'B': None, 'C': Decimal('1114.00')}, {'A': 1, 'B': 'TEST', 'C': Decimal('241.00')}, {'A': 2, 'B': None, 'C': Decimal('572.00')}, {'A': 4, 'B': None, 'C': Decimal('609.00')}, {'A': 3, 'B': None, 'C': Decimal('820.00')}, {'A': 5, 'B': None, 'C': Decimal('1223.00')}]
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(d)
```

### Step 3: Assign result = unknown.mean(...)

```python
result = df[['A', 'C']].mean()
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([2.7, 681.6], index=['A', 'C'], dtype=object)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Call df.mean()

```python
df.mean()
```


## Complete Example

```python
# Workflow
d = [{'A': 2, 'B': None, 'C': Decimal('628.00')}, {'A': 1, 'B': None, 'C': Decimal('383.00')}, {'A': 3, 'B': None, 'C': Decimal('651.00')}, {'A': 2, 'B': None, 'C': Decimal('575.00')}, {'A': 4, 'B': None, 'C': Decimal('1114.00')}, {'A': 1, 'B': 'TEST', 'C': Decimal('241.00')}, {'A': 2, 'B': None, 'C': Decimal('572.00')}, {'A': 4, 'B': None, 'C': Decimal('609.00')}, {'A': 3, 'B': None, 'C': Decimal('820.00')}, {'A': 5, 'B': None, 'C': Decimal('1223.00')}]
df = DataFrame(d)
with pytest.raises(TypeError, match='unsupported operand type|does not support|Cannot perform'):
    df.mean()
result = df[['A', 'C']].mean()
expected = Series([2.7, 681.6], index=['A', 'C'], dtype=object)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_reductions.py:500 | Complexity: Intermediate | Last updated: 2026-06-02*