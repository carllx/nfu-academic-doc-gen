# How To: Double Precision

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test double precision

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

### Step 1: Assign double_input = 30.012345678901234

```python
double_input = 30.012345678901234
```

**Verification:**
```python
assert double_input == json.loads(output)
```

### Step 2: Assign output = ujson.ujson_dumps(...)

```python
output = ujson.ujson_dumps(double_input, double_precision=15)
```

**Verification:**
```python
assert double_input == ujson.ujson_loads(output)
```

### Step 3: Assign output = ujson.ujson_dumps(...)

```python
output = ujson.ujson_dumps(double_input, double_precision=double_precision)
```

**Verification:**
```python
assert rounded_input == json.loads(output)
```

### Step 4: Assign rounded_input = round(...)

```python
rounded_input = round(double_input, double_precision)
```

**Verification:**
```python
assert rounded_input == ujson.ujson_loads(output)
```


## Complete Example

```python
# Workflow
double_input = 30.012345678901234
output = ujson.ujson_dumps(double_input, double_precision=15)
assert double_input == json.loads(output)
assert double_input == ujson.ujson_loads(output)
for double_precision in (3, 9):
    output = ujson.ujson_dumps(double_input, double_precision=double_precision)
    rounded_input = round(double_input, double_precision)
    assert rounded_input == json.loads(output)
    assert rounded_input == ujson.ujson_loads(output)
```

## Next Steps


---

*Source: test_ujson.py:208 | Complexity: Intermediate | Last updated: 2026-06-02*