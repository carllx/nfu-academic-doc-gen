# How To: Assert Attr Equal Different Nulls

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test assert attr equal different nulls

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `types`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: nulls_fixture, nulls_fixture2
```

## Step-by-Step Guide

### Step 1: Assign obj = SimpleNamespace(...)

```python
obj = SimpleNamespace()
```

### Step 2: Assign obj.na_value = nulls_fixture

```python
obj.na_value = nulls_fixture
```

### Step 3: Assign obj2 = SimpleNamespace(...)

```python
obj2 = SimpleNamespace()
```

### Step 4: Assign obj2.na_value = nulls_fixture2

```python
obj2.na_value = nulls_fixture2
```

### Step 5: Call tm.assert_attr_equal()

```python
tm.assert_attr_equal('na_value', obj, obj2)
```

### Step 6: Call tm.assert_attr_equal()

```python
tm.assert_attr_equal('na_value', obj, obj2)
```

### Step 7: Call tm.assert_attr_equal()

```python
tm.assert_attr_equal('na_value', obj, obj2)
```

### Step 8: Call tm.assert_attr_equal()

```python
tm.assert_attr_equal('na_value', obj, obj2)
```


## Complete Example

```python
# Setup
# Fixtures: nulls_fixture, nulls_fixture2

# Workflow
obj = SimpleNamespace()
obj.na_value = nulls_fixture
obj2 = SimpleNamespace()
obj2.na_value = nulls_fixture2
if nulls_fixture is nulls_fixture2:
    tm.assert_attr_equal('na_value', obj, obj2)
elif is_float(nulls_fixture) and is_float(nulls_fixture2):
    tm.assert_attr_equal('na_value', obj, obj2)
elif type(nulls_fixture) is type(nulls_fixture2):
    tm.assert_attr_equal('na_value', obj, obj2)
else:
    with pytest.raises(AssertionError, match='"na_value" are different'):
        tm.assert_attr_equal('na_value', obj, obj2)
```

## Next Steps


---

*Source: test_assert_attr_equal.py:16 | Complexity: Advanced | Last updated: 2026-06-02*