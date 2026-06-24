# How To: Groupby With Timegrouper Methods

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test groupby with timegrouper methods

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`
- `pandas.core.groupby.ops`

**Setup Required:**
```python
# Fixtures: should_sort
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'Branch': 'A A A A A B'.split(), 'Buyer': 'Carl Mark Carl Joe Joe Carl'.split(), 'Quantity': [1, 3, 5, 8, 9, 3], 'Date': [datetime(2013, 1, 1, 13, 0), datetime(2013, 1, 1, 13, 5), datetime(2013, 10, 1, 20, 0), datetime(2013, 10, 2, 10, 0), datetime(2013, 12, 2, 12, 0), datetime(2013, 12, 2, 14, 0)]})
```

**Verification:**
```python
assert g.group_keys
```

### Step 2: Assign df = df.set_index(...)

```python
df = df.set_index('Date', drop=False)
```

**Verification:**
```python
assert isinstance(g._grouper, BinGrouper)
```

### Step 3: Assign g = df.groupby(...)

```python
g = df.groupby(Grouper(freq='6ME'))
```

**Verification:**
```python
assert isinstance(groups, dict)
```

### Step 4: Assign groups = value

```python
groups = g.groups
```

**Verification:**
```python
assert len(groups) == 3
```

### Step 5: Assign df = df.sort_values(...)

```python
df = df.sort_values(by='Quantity', ascending=False)
```


## Complete Example

```python
# Setup
# Fixtures: should_sort

# Workflow
df = DataFrame({'Branch': 'A A A A A B'.split(), 'Buyer': 'Carl Mark Carl Joe Joe Carl'.split(), 'Quantity': [1, 3, 5, 8, 9, 3], 'Date': [datetime(2013, 1, 1, 13, 0), datetime(2013, 1, 1, 13, 5), datetime(2013, 10, 1, 20, 0), datetime(2013, 10, 2, 10, 0), datetime(2013, 12, 2, 12, 0), datetime(2013, 12, 2, 14, 0)]})
if should_sort:
    df = df.sort_values(by='Quantity', ascending=False)
df = df.set_index('Date', drop=False)
g = df.groupby(Grouper(freq='6ME'))
assert g.group_keys
assert isinstance(g._grouper, BinGrouper)
groups = g.groups
assert isinstance(groups, dict)
assert len(groups) == 3
```

## Next Steps


---

*Source: test_timegrouper.py:133 | Complexity: Intermediate | Last updated: 2026-06-02*