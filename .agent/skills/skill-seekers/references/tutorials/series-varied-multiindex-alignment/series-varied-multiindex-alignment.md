# How To: Series Varied Multiindex Alignment

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series varied multiindex alignment

## Prerequisites

**Required Modules:**
- `datetime`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.computation`
- `pandas.core.computation.check`


## Step-by-Step Guide

### Step 1: Assign s1 = Series(...)

```python
s1 = Series(range(8), index=pd.MultiIndex.from_product([list('ab'), list('xy'), [1, 2]], names=['ab', 'xy', 'num']))
```

### Step 2: Assign s2 = Series(...)

```python
s2 = Series([1000 * i for i in range(1, 5)], index=pd.MultiIndex.from_product([list('xy'), [1, 2]], names=['xy', 'num']))
```

### Step 3: Assign result = value

```python
result = s1.loc[pd.IndexSlice[['a'], :, :]] + s2
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([1000, 2001, 3002, 4003], index=pd.MultiIndex.from_tuples([('a', 'x', 1), ('a', 'x', 2), ('a', 'y', 1), ('a', 'y', 2)], names=['ab', 'xy', 'num']))
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
s1 = Series(range(8), index=pd.MultiIndex.from_product([list('ab'), list('xy'), [1, 2]], names=['ab', 'xy', 'num']))
s2 = Series([1000 * i for i in range(1, 5)], index=pd.MultiIndex.from_product([list('xy'), [1, 2]], names=['xy', 'num']))
result = s1.loc[pd.IndexSlice[['a'], :, :]] + s2
expected = Series([1000, 2001, 3002, 4003], index=pd.MultiIndex.from_tuples([('a', 'x', 1), ('a', 'x', 2), ('a', 'y', 1), ('a', 'y', 2)], names=['ab', 'xy', 'num']))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_arithmetic.py:943 | Complexity: Intermediate | Last updated: 2026-06-02*