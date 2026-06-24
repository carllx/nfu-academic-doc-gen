# How To: Groupby Resample Preserves Subclass

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test groupby resample preserves subclass

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`

**Setup Required:**
```python
# Fixtures: obj
```

## Step-by-Step Guide

### Step 1: Assign df = obj(...)

```python
df = obj({'Buyer': Series('Carl Carl Carl Carl Joe Carl'.split(), dtype=object), 'Quantity': [18, 3, 5, 1, 9, 3], 'Date': [datetime(2013, 9, 1, 13, 0), datetime(2013, 9, 1, 13, 5), datetime(2013, 10, 1, 20, 0), datetime(2013, 10, 3, 10, 0), datetime(2013, 12, 2, 12, 0), datetime(2013, 9, 2, 14, 0)]})
```

**Verification:**
```python
assert isinstance(result, obj)
```

### Step 2: Assign df = df.set_index(...)

```python
df = df.set_index('Date')
```

### Step 3: Assign msg = 'DataFrameGroupBy.resample operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.resample operated on the grouping columns'
```

**Verification:**
```python
assert isinstance(result, obj)
```

### Step 4: Assign result = df.groupby.resample.sum(...)

```python
result = df.groupby('Buyer').resample('5D').sum()
```


## Complete Example

```python
# Setup
# Fixtures: obj

# Workflow
df = obj({'Buyer': Series('Carl Carl Carl Carl Joe Carl'.split(), dtype=object), 'Quantity': [18, 3, 5, 1, 9, 3], 'Date': [datetime(2013, 9, 1, 13, 0), datetime(2013, 9, 1, 13, 5), datetime(2013, 10, 1, 20, 0), datetime(2013, 10, 3, 10, 0), datetime(2013, 12, 2, 12, 0), datetime(2013, 9, 2, 14, 0)]})
df = df.set_index('Date')
msg = 'DataFrameGroupBy.resample operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg, raise_on_extra_warnings=False, check_stacklevel=False):
    result = df.groupby('Buyer').resample('5D').sum()
assert isinstance(result, obj)
```

## Next Steps


---

*Source: test_groupby_subclass.py:107 | Complexity: Intermediate | Last updated: 2026-06-02*