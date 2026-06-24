# How To: Astype Categorical To Other

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype categorical to other

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign cat = Categorical(...)

```python
cat = Categorical([f'{i} - {i + 499}' for i in range(0, 10000, 500)])
```

### Step 2: Assign ser = Series.sort_values(...)

```python
ser = Series(np.random.default_rng(2).integers(0, 10000, 100)).sort_values()
```

### Step 3: Assign ser = cut(...)

```python
ser = cut(ser, range(0, 10500, 500), right=False, labels=cat)
```

### Step 4: Assign expected = ser

```python
expected = ser
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser.astype('category'), expected)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser.astype(CategoricalDtype()), expected)
```

### Step 7: Assign msg = 'Cannot cast object|str dtype to float64'

```python
msg = 'Cannot cast object|str dtype to float64'
```

### Step 8: Assign cat = Series(...)

```python
cat = Series(Categorical(['a', 'b', 'b', 'a', 'a', 'c', 'c', 'c']))
```

### Step 9: Assign exp = Series(...)

```python
exp = Series(['a', 'b', 'b', 'a', 'a', 'c', 'c', 'c'], dtype='str')
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(cat.astype('str'), exp)
```

### Step 11: Assign s2 = Series(...)

```python
s2 = Series(Categorical(['1', '2', '3', '4']))
```

### Step 12: Assign exp2 = Series.astype(...)

```python
exp2 = Series([1, 2, 3, 4]).astype('int')
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s2.astype('int'), exp2)
```

### Step 14: Assign expected = Series(...)

```python
expected = Series(np.array(ser.values), name='value_group')
```

### Step 15: Call cmp()

```python
cmp(ser.astype('object'), expected)
```

### Step 16: Call cmp()

```python
cmp(ser.astype(np.object_), expected)
```

### Step 17: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(np.array(ser), np.array(ser.values))
```

### Step 18: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser.astype('category'), ser)
```

### Step 19: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser.astype(CategoricalDtype()), ser)
```

### Step 20: Assign roundtrip_expected = ser.cat.set_categories.cat.remove_unused_categories(...)

```python
roundtrip_expected = ser.cat.set_categories(ser.cat.categories.sort_values()).cat.remove_unused_categories()
```

### Step 21: Assign result = ser.astype.astype(...)

```python
result = ser.astype('object').astype('category')
```

### Step 22: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, roundtrip_expected)
```

### Step 23: Assign result = ser.astype.astype(...)

```python
result = ser.astype('object').astype(CategoricalDtype())
```

### Step 24: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, roundtrip_expected)
```

### Step 25: Call ser.astype()

```python
ser.astype('float64')
```

### Step 26: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(np.sort(np.unique(a)), np.sort(np.unique(b)))
```


## Complete Example

```python
# Workflow
cat = Categorical([f'{i} - {i + 499}' for i in range(0, 10000, 500)])
ser = Series(np.random.default_rng(2).integers(0, 10000, 100)).sort_values()
ser = cut(ser, range(0, 10500, 500), right=False, labels=cat)
expected = ser
tm.assert_series_equal(ser.astype('category'), expected)
tm.assert_series_equal(ser.astype(CategoricalDtype()), expected)
msg = 'Cannot cast object|str dtype to float64'
with pytest.raises(ValueError, match=msg):
    ser.astype('float64')
cat = Series(Categorical(['a', 'b', 'b', 'a', 'a', 'c', 'c', 'c']))
exp = Series(['a', 'b', 'b', 'a', 'a', 'c', 'c', 'c'], dtype='str')
tm.assert_series_equal(cat.astype('str'), exp)
s2 = Series(Categorical(['1', '2', '3', '4']))
exp2 = Series([1, 2, 3, 4]).astype('int')
tm.assert_series_equal(s2.astype('int'), exp2)

def cmp(a, b):
    tm.assert_almost_equal(np.sort(np.unique(a)), np.sort(np.unique(b)))
expected = Series(np.array(ser.values), name='value_group')
cmp(ser.astype('object'), expected)
cmp(ser.astype(np.object_), expected)
tm.assert_almost_equal(np.array(ser), np.array(ser.values))
tm.assert_series_equal(ser.astype('category'), ser)
tm.assert_series_equal(ser.astype(CategoricalDtype()), ser)
roundtrip_expected = ser.cat.set_categories(ser.cat.categories.sort_values()).cat.remove_unused_categories()
result = ser.astype('object').astype('category')
tm.assert_series_equal(result, roundtrip_expected)
result = ser.astype('object').astype(CategoricalDtype())
tm.assert_series_equal(result, roundtrip_expected)
```

## Next Steps


---

*Source: test_astype.py:539 | Complexity: Advanced | Last updated: 2026-06-02*