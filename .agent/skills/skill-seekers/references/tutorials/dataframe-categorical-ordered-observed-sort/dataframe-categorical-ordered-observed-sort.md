# How To: Dataframe Categorical Ordered Observed Sort

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dataframe categorical ordered observed sort

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.typing`
- `pandas.tests.groupby`

**Setup Required:**
```python
# Fixtures: ordered, observed, sort
```

## Step-by-Step Guide

### Step 1: Assign label = Categorical(...)

```python
label = Categorical(['d', 'a', 'b', 'a', 'd', 'b'], categories=['a', 'b', 'missing', 'd'], ordered=ordered)
```

**Verification:**
```python
assert False, msg
```

### Step 2: Assign val = Series(...)

```python
val = Series(['d', 'a', 'b', 'a', 'd', 'b'])
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'label': label, 'val': val})
```

### Step 4: Assign result = unknown.aggregate(...)

```python
result = df.groupby('label', observed=observed, sort=sort)['val'].aggregate('first')
```

### Step 5: Assign label = Series(...)

```python
label = Series(result.index.array, dtype='object')
```

### Step 6: Assign aggr = Series(...)

```python
aggr = Series(result.array)
```

### Step 7: Assign unknown = 'missing'

```python
aggr[aggr.isna()] = 'missing'
```

### Step 8: Assign msg = value

```python
msg = f'Labels and aggregation results not consistently sorted\nfor (ordered={ordered}, observed={observed}, sort={sort})\nResult:\n{result}'
```

**Verification:**
```python
assert False, msg
```


## Complete Example

```python
# Setup
# Fixtures: ordered, observed, sort

# Workflow
label = Categorical(['d', 'a', 'b', 'a', 'd', 'b'], categories=['a', 'b', 'missing', 'd'], ordered=ordered)
val = Series(['d', 'a', 'b', 'a', 'd', 'b'])
df = DataFrame({'label': label, 'val': val})
result = df.groupby('label', observed=observed, sort=sort)['val'].aggregate('first')
label = Series(result.index.array, dtype='object')
aggr = Series(result.array)
if not observed:
    aggr[aggr.isna()] = 'missing'
if not all(label == aggr):
    msg = f'Labels and aggregation results not consistently sorted\nfor (ordered={ordered}, observed={observed}, sort={sort})\nResult:\n{result}'
    assert False, msg
```

## Next Steps


---

*Source: test_categorical.py:639 | Complexity: Advanced | Last updated: 2026-06-02*