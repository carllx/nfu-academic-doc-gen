# How To: Observed Nth

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test observed nth

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.typing`
- `pandas.tests.groupby`


## Step-by-Step Guide

### Step 1: Assign cat = Categorical(...)

```python
cat = Categorical(['a', np.nan, np.nan], categories=['a', 'b', 'c'])
```

### Step 2: Assign ser = Series(...)

```python
ser = Series([1, 2, 3])
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'cat': cat, 'ser': ser})
```

### Step 4: Assign result = unknown.nth(...)

```python
result = df.groupby('cat', observed=False)['ser'].nth(0)
```

### Step 5: Assign expected = value

```python
expected = df['ser'].iloc[[0]]
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
cat = Categorical(['a', np.nan, np.nan], categories=['a', 'b', 'c'])
ser = Series([1, 2, 3])
df = DataFrame({'cat': cat, 'ser': ser})
result = df.groupby('cat', observed=False)['ser'].nth(0)
expected = df['ser'].iloc[[0]]
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_categorical.py:605 | Complexity: Intermediate | Last updated: 2026-06-02*