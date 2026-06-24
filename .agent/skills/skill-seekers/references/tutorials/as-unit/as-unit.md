# How To: As Unit

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test as unit

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas._libs.tslibs.dtypes`
- `pandas.errors`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign ts = Timestamp.as_unit(...)

```python
ts = Timestamp('1970-01-01').as_unit('ns')
```

**Verification:**
```python
assert ts.unit == 'ns'
```

### Step 2: Assign res = ts.as_unit(...)

```python
res = ts.as_unit('us')
```

**Verification:**
```python
assert ts.as_unit('ns') is ts
```

### Step 3: Assign rt = res.as_unit(...)

```python
rt = res.as_unit('ns')
```

**Verification:**
```python
assert res._value == ts._value // 1000
```

### Step 4: Assign res = ts.as_unit(...)

```python
res = ts.as_unit('ms')
```

**Verification:**
```python
assert res._creso == NpyDatetimeUnit.NPY_FR_us.value
```

### Step 5: Assign rt = res.as_unit(...)

```python
rt = res.as_unit('ns')
```

**Verification:**
```python
assert rt._value == ts._value
```

### Step 6: Assign res = ts.as_unit(...)

```python
res = ts.as_unit('s')
```

**Verification:**
```python
assert rt._creso == ts._creso
```

### Step 7: Assign rt = res.as_unit(...)

```python
rt = res.as_unit('ns')
```

**Verification:**
```python
assert res._value == ts._value // 1000000
```


## Complete Example

```python
# Workflow
ts = Timestamp('1970-01-01').as_unit('ns')
assert ts.unit == 'ns'
assert ts.as_unit('ns') is ts
res = ts.as_unit('us')
assert res._value == ts._value // 1000
assert res._creso == NpyDatetimeUnit.NPY_FR_us.value
rt = res.as_unit('ns')
assert rt._value == ts._value
assert rt._creso == ts._creso
res = ts.as_unit('ms')
assert res._value == ts._value // 1000000
assert res._creso == NpyDatetimeUnit.NPY_FR_ms.value
rt = res.as_unit('ns')
assert rt._value == ts._value
assert rt._creso == ts._creso
res = ts.as_unit('s')
assert res._value == ts._value // 1000000000
assert res._creso == NpyDatetimeUnit.NPY_FR_s.value
rt = res.as_unit('ns')
assert rt._value == ts._value
assert rt._creso == ts._creso
```

## Next Steps


---

*Source: test_as_unit.py:10 | Complexity: Intermediate | Last updated: 2026-06-02*