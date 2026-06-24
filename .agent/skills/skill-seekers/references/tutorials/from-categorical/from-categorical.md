# How To: From Categorical

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from categorical

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.timedeltas`


## Step-by-Step Guide

### Step 1: Assign tdi = timedelta_range(...)

```python
tdi = timedelta_range(1, periods=5)
```

### Step 2: Assign cat = pd.Categorical(...)

```python
cat = pd.Categorical(tdi)
```

### Step 3: Assign result = TimedeltaIndex(...)

```python
result = TimedeltaIndex(cat)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, tdi)
```

### Step 5: Assign ci = pd.CategoricalIndex(...)

```python
ci = pd.CategoricalIndex(tdi)
```

### Step 6: Assign result = TimedeltaIndex(...)

```python
result = TimedeltaIndex(ci)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, tdi)
```


## Complete Example

```python
# Workflow
tdi = timedelta_range(1, periods=5)
cat = pd.Categorical(tdi)
result = TimedeltaIndex(cat)
tm.assert_index_equal(result, tdi)
ci = pd.CategoricalIndex(tdi)
result = TimedeltaIndex(ci)
tm.assert_index_equal(result, tdi)
```

## Next Steps


---

*Source: test_constructors.py:281 | Complexity: Intermediate | Last updated: 2026-06-02*