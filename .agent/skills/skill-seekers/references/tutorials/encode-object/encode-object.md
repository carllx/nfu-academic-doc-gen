# How To: Encode Object

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test encode object

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

### Step 1: Assign test_object = _TestObject(...)

```python
test_object = _TestObject(a=1, b=2, _c=3, d=4)
```

**Verification:**
```python
assert ujson.ujson_loads(ujson.ujson_dumps(test_object)) == {'a': 1, 'b': 2, 'd': 4}
```

### Step 2: Assign self.a = a

```python
self.a = a
```

### Step 3: Assign self.b = b

```python
self.b = b
```

### Step 4: Assign self._c = _c

```python
self._c = _c
```

### Step 5: Assign self.d = d

```python
self.d = d
```


## Complete Example

```python
# Workflow
class _TestObject:

    def __init__(self, a, b, _c, d) -> None:
        self.a = a
        self.b = b
        self._c = _c
        self.d = d

    def e(self):
        return 5
test_object = _TestObject(a=1, b=2, _c=3, d=4)
assert ujson.ujson_loads(ujson.ujson_dumps(test_object)) == {'a': 1, 'b': 2, 'd': 4}
```

## Next Steps


---

*Source: test_ujson.py:682 | Complexity: Intermediate | Last updated: 2026-06-02*