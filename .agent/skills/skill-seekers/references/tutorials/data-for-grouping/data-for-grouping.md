# How To: Data For Grouping

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: data for grouping

## Prerequisites

**Required Modules:**
- `__future__`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`
- `pandas.tests.extension`
- `pandas.tests.extension.decimal.array`


## Step-by-Step Guide

### Step 1: Assign b = decimal.Decimal(...)

```python
b = decimal.Decimal('1.0')
```

### Step 2: Assign a = decimal.Decimal(...)

```python
a = decimal.Decimal('0.0')
```

### Step 3: Assign c = decimal.Decimal(...)

```python
c = decimal.Decimal('2.0')
```

### Step 4: Assign na = decimal.Decimal(...)

```python
na = decimal.Decimal('NaN')
```


## Complete Example

```python
# Workflow
b = decimal.Decimal('1.0')
a = decimal.Decimal('0.0')
c = decimal.Decimal('2.0')
na = decimal.Decimal('NaN')
return DecimalArray([b, b, na, na, a, a, b, c])
```

## Next Steps


---

*Source: test_decimal.py:62 | Complexity: Intermediate | Last updated: 2026-06-02*