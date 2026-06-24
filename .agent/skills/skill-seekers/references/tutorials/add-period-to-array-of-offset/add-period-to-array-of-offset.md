# How To: Add Period To Array Of Offset

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test add period to array of offset

## Prerequisites

**Required Modules:**
- `datetime`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`


## Step-by-Step Guide

### Step 1: Assign per = pd.Period(...)

```python
per = pd.Period('2012-1-1', freq='D')
```

### Step 2: Assign pi = pd.period_range(...)

```python
pi = pd.period_range('2012-1-1', periods=10, freq='D')
```

### Step 3: Assign idx = value

```python
idx = per - pi
```

### Step 4: Assign expected = pd.Index(...)

```python
expected = pd.Index([x + per for x in idx], dtype=object)
```

### Step 5: Assign result = value

```python
result = idx + per
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 7: Assign result = value

```python
result = per + idx
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
per = pd.Period('2012-1-1', freq='D')
pi = pd.period_range('2012-1-1', periods=10, freq='D')
idx = per - pi
expected = pd.Index([x + per for x in idx], dtype=object)
result = idx + per
tm.assert_index_equal(result, expected)
result = per + idx
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_object.py:83 | Complexity: Advanced | Last updated: 2026-06-02*