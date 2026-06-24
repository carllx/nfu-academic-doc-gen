# How To: Constructor Infer Nat Dt Like

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test constructor infer nat dt like

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.timezones`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: pos, klass, dtype, ctor, nulls_fixture, request
```

## Step-by-Step Guide

### Step 1: Assign expected = klass(...)

```python
expected = klass([NaT, NaT])
```

**Verification:**
```python
assert expected.dtype == dtype
```

### Step 2: Assign data = value

```python
data = [ctor]
```

### Step 3: Call data.insert()

```python
data.insert(pos, nulls_fixture)
```

### Step 4: Assign warn = None

```python
warn = None
```

### Step 5: Assign result = Index(...)

```python
result = Index(data)
```

### Step 6: Assign result = Index(...)

```python
result = Index(np.array(data, dtype=object))
```

### Step 7: Call pytest.skip()

```python
pytest.skip(f"We don't cast {type(nulls_fixture).__name__} to datetime64/timedelta64")
```

### Step 8: Assign expected = Index(...)

```python
expected = Index([NA, NaT])
```

### Step 9: Assign mark = pytest.mark.xfail(...)

```python
mark = pytest.mark.xfail(reason='Broken with np.NaT ctor; see GH 31884')
```

### Step 10: Call request.applymarker()

```python
request.applymarker(mark)
```

### Step 11: Assign warn = DeprecationWarning

```python
warn = DeprecationWarning
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 13: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: pos, klass, dtype, ctor, nulls_fixture, request

# Workflow
if isinstance(nulls_fixture, Decimal):
    pytest.skip(f"We don't cast {type(nulls_fixture).__name__} to datetime64/timedelta64")
expected = klass([NaT, NaT])
assert expected.dtype == dtype
data = [ctor]
data.insert(pos, nulls_fixture)
warn = None
if nulls_fixture is NA:
    expected = Index([NA, NaT])
    mark = pytest.mark.xfail(reason='Broken with np.NaT ctor; see GH 31884')
    request.applymarker(mark)
    warn = DeprecationWarning
result = Index(data)
with tm.assert_produces_warning(warn):
    tm.assert_index_equal(result, expected)
result = Index(np.array(data, dtype=object))
with tm.assert_produces_warning(warn):
    tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_index_new.py:133 | Complexity: Advanced | Last updated: 2026-06-02*