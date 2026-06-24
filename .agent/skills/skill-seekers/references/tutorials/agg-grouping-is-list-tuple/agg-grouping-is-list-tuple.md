# How To: Agg Grouping Is List Tuple

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test agg grouping is list tuple

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `functools`
- `functools`
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`

**Setup Required:**
```python
# Fixtures: ts
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((30, 4)), columns=Index(list('ABCD'), dtype=object), index=pd.date_range('2000-01-01', periods=30, freq='B'))
```

### Step 2: Assign grouped = df.groupby(...)

```python
grouped = df.groupby(lambda x: x.year)
```

### Step 3: Assign grouper = value

```python
grouper = grouped._grouper.groupings[0].grouping_vector
```

### Step 4: Assign unknown = Grouping(...)

```python
grouped._grouper.groupings[0] = Grouping(ts.index, list(grouper))
```

### Step 5: Assign result = grouped.agg(...)

```python
result = grouped.agg('mean')
```

### Step 6: Assign expected = grouped.mean(...)

```python
expected = grouped.mean()
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign unknown = Grouping(...)

```python
grouped._grouper.groupings[0] = Grouping(ts.index, tuple(grouper))
```

### Step 9: Assign result = grouped.agg(...)

```python
result = grouped.agg('mean')
```

### Step 10: Assign expected = grouped.mean(...)

```python
expected = grouped.mean()
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: ts

# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((30, 4)), columns=Index(list('ABCD'), dtype=object), index=pd.date_range('2000-01-01', periods=30, freq='B'))
grouped = df.groupby(lambda x: x.year)
grouper = grouped._grouper.groupings[0].grouping_vector
grouped._grouper.groupings[0] = Grouping(ts.index, list(grouper))
result = grouped.agg('mean')
expected = grouped.mean()
tm.assert_frame_equal(result, expected)
grouped._grouper.groupings[0] = Grouping(ts.index, tuple(grouper))
result = grouped.agg('mean')
expected = grouped.mean()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_aggregate.py:163 | Complexity: Advanced | Last updated: 2026-06-02*