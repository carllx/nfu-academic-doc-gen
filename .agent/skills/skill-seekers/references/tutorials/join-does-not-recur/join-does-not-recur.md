# How To: Join Does Not Recur

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join does not recur

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.ones((3, 2)), index=date_range('2020-01-01', periods=3), columns=period_range('2020-01-01', periods=2))
```

### Step 2: Assign ser = value

```python
ser = df.iloc[:2, 0]
```

### Step 3: Assign res = ser.index.join(...)

```python
res = ser.index.join(df.columns, how='outer')
```

### Step 4: Assign expected = Index(...)

```python
expected = Index([ser.index[0], ser.index[1], df.columns[0], df.columns[1]], object)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.ones((3, 2)), index=date_range('2020-01-01', periods=3), columns=period_range('2020-01-01', periods=2))
ser = df.iloc[:2, 0]
res = ser.index.join(df.columns, how='outer')
expected = Index([ser.index[0], ser.index[1], df.columns[0], df.columns[1]], object)
tm.assert_index_equal(res, expected)
```

## Next Steps


---

*Source: test_join.py:39 | Complexity: Intermediate | Last updated: 2026-06-02*