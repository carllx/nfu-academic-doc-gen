# How To: Custom Asserts

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test custom asserts

## Prerequisites

**Required Modules:**
- `collections`
- `operator`
- `sys`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tests.extension`
- `pandas.tests.extension.json.array`


## Step-by-Step Guide

### Step 1: Assign data = JSONArray(...)

```python
data = JSONArray([collections.UserDict({'a': 1}), collections.UserDict({'b': 2}), collections.UserDict({'c': 3})])
```

### Step 2: Assign a = pd.Series(...)

```python
a = pd.Series(data)
```

### Step 3: Call custom_assert_series_equal()

```python
custom_assert_series_equal(a, a)
```

### Step 4: Call custom_assert_frame_equal()

```python
custom_assert_frame_equal(a.to_frame(), a.to_frame())
```

### Step 5: Assign b = pd.Series(...)

```python
b = pd.Series(data.take([0, 0, 1]))
```

### Step 6: Assign msg = 'Series are different'

```python
msg = 'Series are different'
```

### Step 7: Call custom_assert_series_equal()

```python
custom_assert_series_equal(a, b)
```

### Step 8: Call custom_assert_frame_equal()

```python
custom_assert_frame_equal(a.to_frame(), b.to_frame())
```


## Complete Example

```python
# Workflow
data = JSONArray([collections.UserDict({'a': 1}), collections.UserDict({'b': 2}), collections.UserDict({'c': 3})])
a = pd.Series(data)
custom_assert_series_equal(a, a)
custom_assert_frame_equal(a.to_frame(), a.to_frame())
b = pd.Series(data.take([0, 0, 1]))
msg = 'Series are different'
with pytest.raises(AssertionError, match=msg):
    custom_assert_series_equal(a, b)
with pytest.raises(AssertionError, match=msg):
    custom_assert_frame_equal(a.to_frame(), b.to_frame())
```

## Next Steps


---

*Source: test_json.py:470 | Complexity: Advanced | Last updated: 2026-06-02*