# How To: Metadata Propagation Indiv

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test metadata propagation indiv

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: monkeypatch
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(range(3), range(3))
```

**Verification:**
```python
assert result.filename == 'foo+bar'
```

### Step 2: Assign ser.name = 'foo'

```python
ser.name = 'foo'
```

**Verification:**
```python
assert result.name is None
```

### Step 3: Assign ser2 = Series(...)

```python
ser2 = Series(range(3), range(3))
```

### Step 4: Assign ser2.name = 'bar'

```python
ser2.name = 'bar'
```

### Step 5: Assign result = value

```python
result = ser.T
```

### Step 6: Call tm.assert_metadata_equivalent()

```python
tm.assert_metadata_equivalent(ser, result)
```

### Step 7: Call m.setattr()

```python
m.setattr(Series, '_metadata', ['name', 'filename'])
```

### Step 8: Call m.setattr()

```python
m.setattr(Series, '__finalize__', finalize)
```

### Step 9: Assign ser.filename = 'foo'

```python
ser.filename = 'foo'
```

### Step 10: Assign ser2.filename = 'bar'

```python
ser2.filename = 'bar'
```

### Step 11: Assign result = pd.concat(...)

```python
result = pd.concat([ser, ser2])
```

**Verification:**
```python
assert result.filename == 'foo+bar'
```

### Step 12: Assign value = unknown.join(...)

```python
value = '+'.join([getattr(obj, name) for obj in other.objs if getattr(obj, name, None)])
```

### Step 13: Call object.__setattr__()

```python
object.__setattr__(self, name, value)
```

### Step 14: Call object.__setattr__()

```python
object.__setattr__(self, name, getattr(other, name, None))
```


## Complete Example

```python
# Setup
# Fixtures: monkeypatch

# Workflow
ser = Series(range(3), range(3))
ser.name = 'foo'
ser2 = Series(range(3), range(3))
ser2.name = 'bar'
result = ser.T
tm.assert_metadata_equivalent(ser, result)

def finalize(self, other, method=None, **kwargs):
    for name in self._metadata:
        if method == 'concat' and name == 'filename':
            value = '+'.join([getattr(obj, name) for obj in other.objs if getattr(obj, name, None)])
            object.__setattr__(self, name, value)
        else:
            object.__setattr__(self, name, getattr(other, name, None))
    return self
with monkeypatch.context() as m:
    m.setattr(Series, '_metadata', ['name', 'filename'])
    m.setattr(Series, '__finalize__', finalize)
    ser.filename = 'foo'
    ser2.filename = 'bar'
    result = pd.concat([ser, ser2])
    assert result.filename == 'foo+bar'
    assert result.name is None
```

## Next Steps


---

*Source: test_series.py:123 | Complexity: Advanced | Last updated: 2026-06-02*