# How To: Datetime Units

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test datetime units

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

### Step 1: Assign val = datetime.datetime(...)

```python
val = datetime.datetime(2013, 8, 17, 21, 17, 12, 215504)
```

**Verification:**
```python
assert roundtrip == stamp._value // 10 ** 9
```

### Step 2: Assign stamp = Timestamp.as_unit(...)

```python
stamp = Timestamp(val).as_unit('ns')
```

**Verification:**
```python
assert roundtrip == stamp._value // 10 ** 6
```

### Step 3: Assign roundtrip = ujson.ujson_loads(...)

```python
roundtrip = ujson.ujson_loads(ujson.ujson_dumps(val, date_unit='s'))
```

**Verification:**
```python
assert roundtrip == stamp._value // 10 ** 3
```

### Step 4: Assign roundtrip = ujson.ujson_loads(...)

```python
roundtrip = ujson.ujson_loads(ujson.ujson_dumps(val, date_unit='ms'))
```

**Verification:**
```python
assert roundtrip == stamp._value
```

### Step 5: Assign roundtrip = ujson.ujson_loads(...)

```python
roundtrip = ujson.ujson_loads(ujson.ujson_dumps(val, date_unit='us'))
```

**Verification:**
```python
assert roundtrip == stamp._value // 10 ** 3
```

### Step 6: Assign roundtrip = ujson.ujson_loads(...)

```python
roundtrip = ujson.ujson_loads(ujson.ujson_dumps(val, date_unit='ns'))
```

**Verification:**
```python
assert roundtrip == stamp._value
```

### Step 7: Assign msg = "Invalid value 'foo' for option 'date_unit'"

```python
msg = "Invalid value 'foo' for option 'date_unit'"
```

### Step 8: Call ujson.ujson_dumps()

```python
ujson.ujson_dumps(val, date_unit='foo')
```


## Complete Example

```python
# Workflow
val = datetime.datetime(2013, 8, 17, 21, 17, 12, 215504)
stamp = Timestamp(val).as_unit('ns')
roundtrip = ujson.ujson_loads(ujson.ujson_dumps(val, date_unit='s'))
assert roundtrip == stamp._value // 10 ** 9
roundtrip = ujson.ujson_loads(ujson.ujson_dumps(val, date_unit='ms'))
assert roundtrip == stamp._value // 10 ** 6
roundtrip = ujson.ujson_loads(ujson.ujson_dumps(val, date_unit='us'))
assert roundtrip == stamp._value // 10 ** 3
roundtrip = ujson.ujson_loads(ujson.ujson_dumps(val, date_unit='ns'))
assert roundtrip == stamp._value
msg = "Invalid value 'foo' for option 'date_unit'"
with pytest.raises(ValueError, match=msg):
    ujson.ujson_dumps(val, date_unit='foo')
```

## Next Steps


---

*Source: test_ujson.py:393 | Complexity: Advanced | Last updated: 2026-06-02*