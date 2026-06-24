# How To: Td64 To Tdstruct

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test td64 to tdstruct

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs.dtypes`
- `pandas._libs.tslibs.np_datetime`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign val = 12454636234

```python
val = 12454636234
```

**Verification:**
```python
assert res1 == exp1
```

### Step 2: Assign res1 = py_td64_to_tdstruct(...)

```python
res1 = py_td64_to_tdstruct(val, NpyDatetimeUnit.NPY_FR_ns.value)
```

**Verification:**
```python
assert res2 == exp2
```

### Step 3: Assign exp1 = value

```python
exp1 = {'days': 0, 'hrs': 0, 'min': 0, 'sec': 12, 'ms': 454, 'us': 636, 'ns': 234, 'seconds': 12, 'microseconds': 454636, 'nanoseconds': 234}
```

**Verification:**
```python
assert res3 == exp3
```

### Step 4: Assign res2 = py_td64_to_tdstruct(...)

```python
res2 = py_td64_to_tdstruct(val, NpyDatetimeUnit.NPY_FR_us.value)
```

**Verification:**
```python
assert res4 == exp4
```

### Step 5: Assign exp2 = value

```python
exp2 = {'days': 0, 'hrs': 3, 'min': 27, 'sec': 34, 'ms': 636, 'us': 234, 'ns': 0, 'seconds': 12454, 'microseconds': 636234, 'nanoseconds': 0}
```

**Verification:**
```python
assert res2 == exp2
```

### Step 6: Assign res3 = py_td64_to_tdstruct(...)

```python
res3 = py_td64_to_tdstruct(val, NpyDatetimeUnit.NPY_FR_ms.value)
```

### Step 7: Assign exp3 = value

```python
exp3 = {'days': 144, 'hrs': 3, 'min': 37, 'sec': 16, 'ms': 234, 'us': 0, 'ns': 0, 'seconds': 13036, 'microseconds': 234000, 'nanoseconds': 0}
```

**Verification:**
```python
assert res3 == exp3
```

### Step 8: Assign res4 = py_td64_to_tdstruct(...)

```python
res4 = py_td64_to_tdstruct(val, NpyDatetimeUnit.NPY_FR_s.value)
```

### Step 9: Assign exp4 = value

```python
exp4 = {'days': 144150, 'hrs': 21, 'min': 10, 'sec': 34, 'ms': 0, 'us': 0, 'ns': 0, 'seconds': 76234, 'microseconds': 0, 'nanoseconds': 0}
```

**Verification:**
```python
assert res4 == exp4
```


## Complete Example

```python
# Workflow
val = 12454636234
res1 = py_td64_to_tdstruct(val, NpyDatetimeUnit.NPY_FR_ns.value)
exp1 = {'days': 0, 'hrs': 0, 'min': 0, 'sec': 12, 'ms': 454, 'us': 636, 'ns': 234, 'seconds': 12, 'microseconds': 454636, 'nanoseconds': 234}
assert res1 == exp1
res2 = py_td64_to_tdstruct(val, NpyDatetimeUnit.NPY_FR_us.value)
exp2 = {'days': 0, 'hrs': 3, 'min': 27, 'sec': 34, 'ms': 636, 'us': 234, 'ns': 0, 'seconds': 12454, 'microseconds': 636234, 'nanoseconds': 0}
assert res2 == exp2
res3 = py_td64_to_tdstruct(val, NpyDatetimeUnit.NPY_FR_ms.value)
exp3 = {'days': 144, 'hrs': 3, 'min': 37, 'sec': 16, 'ms': 234, 'us': 0, 'ns': 0, 'seconds': 13036, 'microseconds': 234000, 'nanoseconds': 0}
assert res3 == exp3
res4 = py_td64_to_tdstruct(val, NpyDatetimeUnit.NPY_FR_s.value)
exp4 = {'days': 144150, 'hrs': 21, 'min': 10, 'sec': 34, 'ms': 0, 'us': 0, 'ns': 0, 'seconds': 76234, 'microseconds': 0, 'nanoseconds': 0}
assert res4 == exp4
```

## Next Steps


---

*Source: test_np_datetime.py:73 | Complexity: Advanced | Last updated: 2026-06-02*