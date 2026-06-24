# How To: Astype Unicode

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype unicode

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `importlib`
- `string`
- `sys`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign digits = value

```python
digits = string.digits
```

### Step 2: Assign test_series = value

```python
test_series = [Series([digits * 10, rand_str(63), rand_str(64), rand_str(1000)]), Series(['データーサイエンス、お前はもう死んでいる'])]
```

### Step 3: Assign former_encoding = None

```python
former_encoding = None
```

### Step 4: Assign item = '野菜食べないとやばい'

```python
item = '野菜食べないとやばい'
```

### Step 5: Assign ser = Series(...)

```python
ser = Series([item.encode()])
```

### Step 6: Assign result = ser.astype(...)

```python
result = ser.astype(np.str_)
```

### Step 7: Assign expected = Series(...)

```python
expected = Series([item], dtype=object)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 9: Assign res = ser.astype(...)

```python
res = ser.astype(np.str_)
```

### Step 10: Assign expec = ser.map(...)

```python
expec = ser.map(str)
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expec)
```

### Step 12: Call reload()

```python
reload(sys)
```

### Step 13: Call sys.setdefaultencoding()

```python
sys.setdefaultencoding(former_encoding)
```

### Step 14: Assign expec = expec.astype(...)

```python
expec = expec.astype(object)
```


## Complete Example

```python
# Setup
# Fixtures: using_infer_string

# Workflow
digits = string.digits
test_series = [Series([digits * 10, rand_str(63), rand_str(64), rand_str(1000)]), Series(['データーサイエンス、お前はもう死んでいる'])]
former_encoding = None
if sys.getdefaultencoding() == 'utf-8':
    item = '野菜食べないとやばい'
    ser = Series([item.encode()])
    result = ser.astype(np.str_)
    expected = Series([item], dtype=object)
    tm.assert_series_equal(result, expected)
for ser in test_series:
    res = ser.astype(np.str_)
    expec = ser.map(str)
    if using_infer_string:
        expec = expec.astype(object)
    tm.assert_series_equal(res, expec)
if former_encoding is not None and former_encoding != 'utf-8':
    reload(sys)
    sys.setdefaultencoding(former_encoding)
```

## Next Steps


---

*Source: test_astype.py:427 | Complexity: Advanced | Last updated: 2026-06-02*