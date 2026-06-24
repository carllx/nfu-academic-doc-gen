# How To: Join With Period Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join with period index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: join_type
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.ones((10, 2)), index=date_range('2020-01-01', periods=10), columns=period_range('2020-01-01', periods=2))
```

### Step 2: Assign s = value

```python
s = df.iloc[:5, 0]
```

### Step 3: Assign expected = df.columns.astype.join(...)

```python
expected = df.columns.astype('O').join(s.index, how=join_type)
```

### Step 4: Assign result = df.columns.join(...)

```python
result = df.columns.join(s.index, how=join_type)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(expected, result)
```


## Complete Example

```python
# Setup
# Fixtures: join_type

# Workflow
df = DataFrame(np.ones((10, 2)), index=date_range('2020-01-01', periods=10), columns=period_range('2020-01-01', periods=2))
s = df.iloc[:5, 0]
expected = df.columns.astype('O').join(s.index, how=join_type)
result = df.columns.join(s.index, how=join_type)
tm.assert_index_equal(expected, result)
```

## Next Steps


---

*Source: test_join.py:40 | Complexity: Intermediate | Last updated: 2026-06-02*