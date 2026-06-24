# How To: Encode Double Tiny Exponential

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test encode double tiny exponential

## Prerequisites

**Required Modules:**
- `calendar`
- `datetime`
- `decimal`
- `json`
- `locale`
- `math`
- `re`
- `time`
- `dateutil`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.json`
- `pandas.compat`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign num = 1e-40

```python
num = 1e-40
```

**Verification:**
```python
assert num == ujson.ujson_loads(ujson.ujson_dumps(num))
```

### Step 2: Assign num = 1e-100

```python
num = 1e-100
```

**Verification:**
```python
assert num == ujson.ujson_loads(ujson.ujson_dumps(num))
```

### Step 3: Assign num = value

```python
num = -1e-45
```

**Verification:**
```python
assert num == ujson.ujson_loads(ujson.ujson_dumps(num))
```

### Step 4: Assign num = value

```python
num = -1e-145
```

**Verification:**
```python
assert np.allclose(num, ujson.ujson_loads(ujson.ujson_dumps(num)))
```


## Complete Example

```python
# Workflow
num = 1e-40
assert num == ujson.ujson_loads(ujson.ujson_dumps(num))
num = 1e-100
assert num == ujson.ujson_loads(ujson.ujson_dumps(num))
num = -1e-45
assert num == ujson.ujson_loads(ujson.ujson_dumps(num))
num = -1e-145
assert np.allclose(num, ujson.ujson_loads(ujson.ujson_dumps(num)))
```

## Next Steps


---

*Source: test_ujson.py:165 | Complexity: Intermediate | Last updated: 2026-06-02*