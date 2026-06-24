# How To: Boxable Categorical Values

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test boxable categorical values

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign cat = pd.Categorical(...)

```python
cat = pd.Categorical(pd.date_range('2012-01-01', periods=3, freq='h'))
```

### Step 2: Assign result = value

```python
result = MultiIndex.from_product([['a', 'b', 'c'], cat]).values
```

### Step 3: Assign expected = value

```python
expected = pd.Series([('a', pd.Timestamp('2012-01-01 00:00:00')), ('a', pd.Timestamp('2012-01-01 01:00:00')), ('a', pd.Timestamp('2012-01-01 02:00:00')), ('b', pd.Timestamp('2012-01-01 00:00:00')), ('b', pd.Timestamp('2012-01-01 01:00:00')), ('b', pd.Timestamp('2012-01-01 02:00:00')), ('c', pd.Timestamp('2012-01-01 00:00:00')), ('c', pd.Timestamp('2012-01-01 01:00:00')), ('c', pd.Timestamp('2012-01-01 02:00:00'))]).values
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 5: Assign result = value

```python
result = pd.DataFrame({'a': ['a', 'b', 'c'], 'b': cat, 'c': np.array(cat)}).values
```

### Step 6: Assign expected = value

```python
expected = pd.DataFrame({'a': ['a', 'b', 'c'], 'b': [pd.Timestamp('2012-01-01 00:00:00'), pd.Timestamp('2012-01-01 01:00:00'), pd.Timestamp('2012-01-01 02:00:00')], 'c': [pd.Timestamp('2012-01-01 00:00:00'), pd.Timestamp('2012-01-01 01:00:00'), pd.Timestamp('2012-01-01 02:00:00')]}).values
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
cat = pd.Categorical(pd.date_range('2012-01-01', periods=3, freq='h'))
result = MultiIndex.from_product([['a', 'b', 'c'], cat]).values
expected = pd.Series([('a', pd.Timestamp('2012-01-01 00:00:00')), ('a', pd.Timestamp('2012-01-01 01:00:00')), ('a', pd.Timestamp('2012-01-01 02:00:00')), ('b', pd.Timestamp('2012-01-01 00:00:00')), ('b', pd.Timestamp('2012-01-01 01:00:00')), ('b', pd.Timestamp('2012-01-01 02:00:00')), ('c', pd.Timestamp('2012-01-01 00:00:00')), ('c', pd.Timestamp('2012-01-01 01:00:00')), ('c', pd.Timestamp('2012-01-01 02:00:00'))]).values
tm.assert_numpy_array_equal(result, expected)
result = pd.DataFrame({'a': ['a', 'b', 'c'], 'b': cat, 'c': np.array(cat)}).values
expected = pd.DataFrame({'a': ['a', 'b', 'c'], 'b': [pd.Timestamp('2012-01-01 00:00:00'), pd.Timestamp('2012-01-01 01:00:00'), pd.Timestamp('2012-01-01 02:00:00')], 'c': [pd.Timestamp('2012-01-01 00:00:00'), pd.Timestamp('2012-01-01 01:00:00'), pd.Timestamp('2012-01-01 02:00:00')]}).values
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_compat.py:89 | Complexity: Intermediate | Last updated: 2026-06-02*