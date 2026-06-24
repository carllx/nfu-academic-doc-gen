# How To: Set Value Resize

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set value resize

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: float_frame, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign res = float_frame._set_value(...)

```python
res = float_frame._set_value('foobar', 'B', 0)
```

**Verification:**
```python
assert res is None
```

### Step 2: Assign unknown = 0

```python
float_frame.loc['foobar', 'qux'] = 0
```

**Verification:**
```python
assert float_frame.index[-1] == 'foobar'
```

### Step 3: Assign res = float_frame.copy(...)

```python
res = float_frame.copy()
```

**Verification:**
```python
assert float_frame._get_value('foobar', 'B') == 0
```

### Step 4: Call res._set_value()

```python
res._set_value('foobar', 'baz', 'sam')
```

**Verification:**
```python
assert float_frame._get_value('foobar', 'qux') == 0
```

### Step 5: Assign res = float_frame.copy(...)

```python
res = float_frame.copy()
```

**Verification:**
```python
assert res['baz'].dtype == 'str'
```

### Step 6: Call res._set_value()

```python
res._set_value('foobar', 'baz', True)
```

**Verification:**
```python
assert res['baz'].dtype == np.object_
```

### Step 7: Assign res = float_frame.copy(...)

```python
res = float_frame.copy()
```

**Verification:**
```python
assert res['baz'].dtype == np.object_
```

### Step 8: Call res._set_value()

```python
res._set_value('foobar', 'baz', 5)
```

**Verification:**
```python
assert is_float_dtype(res['baz'])
```

### Step 9: Call res._set_value()

```python
res._set_value('foobar', 'baz', 'sam')
```

**Verification:**
```python
assert isna(res['baz'].drop(['foobar'])).all()
```


## Complete Example

```python
# Setup
# Fixtures: float_frame, using_infer_string

# Workflow
res = float_frame._set_value('foobar', 'B', 0)
assert res is None
assert float_frame.index[-1] == 'foobar'
assert float_frame._get_value('foobar', 'B') == 0
float_frame.loc['foobar', 'qux'] = 0
assert float_frame._get_value('foobar', 'qux') == 0
res = float_frame.copy()
res._set_value('foobar', 'baz', 'sam')
if using_infer_string:
    assert res['baz'].dtype == 'str'
else:
    assert res['baz'].dtype == np.object_
res = float_frame.copy()
res._set_value('foobar', 'baz', True)
assert res['baz'].dtype == np.object_
res = float_frame.copy()
res._set_value('foobar', 'baz', 5)
assert is_float_dtype(res['baz'])
assert isna(res['baz'].drop(['foobar'])).all()
with tm.assert_produces_warning(FutureWarning, match='Setting an item of incompatible dtype'):
    res._set_value('foobar', 'baz', 'sam')
assert res.loc['foobar', 'baz'] == 'sam'
```

## Next Steps


---

*Source: test_set_value.py:19 | Complexity: Advanced | Last updated: 2026-06-02*