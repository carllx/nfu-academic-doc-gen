# How To: Precise Conversion

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test precise conversion

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `decimal`
- `io`
- `mmap`
- `os`
- `tarfile`
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: c_parser_only, num
```

## Step-by-Step Guide

### Step 1: Assign parser = c_parser_only

```python
parser = c_parser_only
```

**Verification:**
```python
assert roundtrip_val == float(text[2:])
```

### Step 2: Assign normal_errors = value

```python
normal_errors = []
```

**Verification:**
```python
assert sum(precise_errors) <= sum(normal_errors)
```

### Step 3: Assign precise_errors = value

```python
precise_errors = []
```

**Verification:**
```python
assert max(precise_errors) <= max(normal_errors)
```

### Step 4: Assign text = value

```python
text = f'a\n{num:.25}'
```

### Step 5: Assign normal_val = float(...)

```python
normal_val = float(parser.read_csv(StringIO(text), float_precision='legacy')['a'][0])
```

### Step 6: Assign precise_val = float(...)

```python
precise_val = float(parser.read_csv(StringIO(text), float_precision='high')['a'][0])
```

### Step 7: Assign roundtrip_val = float(...)

```python
roundtrip_val = float(parser.read_csv(StringIO(text), float_precision='round_trip')['a'][0])
```

### Step 8: Assign actual_val = Decimal(...)

```python
actual_val = Decimal(text[2:])
```

### Step 9: Call normal_errors.append()

```python
normal_errors.append(error(normal_val, actual_val))
```

### Step 10: Call precise_errors.append()

```python
precise_errors.append(error(precise_val, actual_val))
```

**Verification:**
```python
assert roundtrip_val == float(text[2:])
```


## Complete Example

```python
# Setup
# Fixtures: c_parser_only, num

# Workflow
parser = c_parser_only
normal_errors = []
precise_errors = []

def error(val: float, actual_val: Decimal) -> Decimal:
    return abs(Decimal(f'{val:.100}') - actual_val)
text = f'a\n{num:.25}'
normal_val = float(parser.read_csv(StringIO(text), float_precision='legacy')['a'][0])
precise_val = float(parser.read_csv(StringIO(text), float_precision='high')['a'][0])
roundtrip_val = float(parser.read_csv(StringIO(text), float_precision='round_trip')['a'][0])
actual_val = Decimal(text[2:])
normal_errors.append(error(normal_val, actual_val))
precise_errors.append(error(precise_val, actual_val))
assert roundtrip_val == float(text[2:])
assert sum(precise_errors) <= sum(normal_errors)
assert max(precise_errors) <= max(normal_errors)
```

## Next Steps


---

*Source: test_c_parser_only.py:155 | Complexity: Advanced | Last updated: 2026-06-02*