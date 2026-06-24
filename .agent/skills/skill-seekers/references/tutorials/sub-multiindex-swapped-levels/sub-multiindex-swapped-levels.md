# How To: Sub Multiindex Swapped Levels

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sub multiindex swapped levels

## Prerequisites

**Required Modules:**
- `__future__`
- `collections`
- `datetime`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.computation`
- `pandas.tests.arithmetic.common`


## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'a': np.random.default_rng(2).standard_normal(6)}, index=pd.MultiIndex.from_product([['a', 'b'], [0, 1, 2]], names=['levA', 'levB']))
```

### Step 2: Assign df2 = df.copy(...)

```python
df2 = df.copy()
```

### Step 3: Assign df2.index = df2.index.swaplevel(...)

```python
df2.index = df2.index.swaplevel(0, 1)
```

### Step 4: Assign result = value

```python
result = df - df2
```

### Step 5: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame([0.0] * 6, columns=['a'], index=df.index)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = pd.DataFrame({'a': np.random.default_rng(2).standard_normal(6)}, index=pd.MultiIndex.from_product([['a', 'b'], [0, 1, 2]], names=['levA', 'levB']))
df2 = df.copy()
df2.index = df2.index.swaplevel(0, 1)
result = df - df2
expected = pd.DataFrame([0.0] * 6, columns=['a'], index=df.index)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_numeric.py:1528 | Complexity: Intermediate | Last updated: 2026-06-02*