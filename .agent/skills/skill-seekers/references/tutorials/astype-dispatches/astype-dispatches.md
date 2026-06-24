# How To: Astype Dispatches

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: test astype dispatches

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: frame
```

## Step-by-Step Guide

### Step 1: Assign data = pd.Series(...)

```python
data = pd.Series(DecimalArray([decimal.Decimal(2)]), name='a')
```

**Verification:**
```python
assert result.dtype.context.prec == ctx.prec
```

### Step 2: Assign ctx = decimal.Context(...)

```python
ctx = decimal.Context()
```

### Step 3: Assign ctx.prec = 5

```python
ctx.prec = 5
```

### Step 4: Assign result = data.astype(...)

```python
result = data.astype(DecimalDtype(ctx))
```

**Verification:**
```python
assert result.dtype.context.prec == ctx.prec
```

### Step 5: Assign data = data.to_frame(...)

```python
data = data.to_frame()
```

### Step 6: Assign result = value

```python
result = result['a']
```


## Complete Example

```python
# Setup
# Fixtures: frame

# Workflow
data = pd.Series(DecimalArray([decimal.Decimal(2)]), name='a')
ctx = decimal.Context()
ctx.prec = 5
if frame:
    data = data.to_frame()
result = data.astype(DecimalDtype(ctx))
if frame:
    result = result['a']
assert result.dtype.context.prec == ctx.prec
```

## Next Steps


---

*Source: test_decimal.py:357 | Complexity: Intermediate | Last updated: 2026-06-02*