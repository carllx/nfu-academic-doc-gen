# How To: Encode Null Character

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test encode null character

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

### Step 1: Assign wrapped_input = '31337 \x00 1337'

```python
wrapped_input = '31337 \x00 1337'
```

**Verification:**
```python
assert wrapped_input == json.loads(output)
```

### Step 2: Assign output = ujson.ujson_dumps(...)

```python
output = ujson.ujson_dumps(wrapped_input)
```

**Verification:**
```python
assert output == json.dumps(wrapped_input)
```

### Step 3: Assign alone_input = '\x00'

```python
alone_input = '\x00'
```

**Verification:**
```python
assert wrapped_input == ujson.ujson_loads(output)
```

### Step 4: Assign output = ujson.ujson_dumps(...)

```python
output = ujson.ujson_dumps(alone_input)
```

**Verification:**
```python
assert alone_input == json.loads(output)
```


## Complete Example

```python
# Workflow
wrapped_input = '31337 \x00 1337'
output = ujson.ujson_dumps(wrapped_input)
assert wrapped_input == json.loads(output)
assert output == json.dumps(wrapped_input)
assert wrapped_input == ujson.ujson_loads(output)
alone_input = '\x00'
output = ujson.ujson_dumps(alone_input)
assert alone_input == json.loads(output)
assert output == json.dumps(alone_input)
assert alone_input == ujson.ujson_loads(output)
assert '"  \\u0000\\r\\n "' == ujson.ujson_dumps('  \x00\r\n ')
```

## Next Steps


---

*Source: test_ujson.py:528 | Complexity: Intermediate | Last updated: 2026-06-02*