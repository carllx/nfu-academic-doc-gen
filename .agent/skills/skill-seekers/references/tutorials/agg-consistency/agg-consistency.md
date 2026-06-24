# How To: Agg Consistency

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test agg consistency

## Prerequisites

**Required Modules:**
- `datetime`
- `functools`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.formats.printing`
- `pandas.tests.extension.decimal.array`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'col1': [1, 2, 3, 4], 'col2': [10, 25, 26, 31], 'date': [dt.date(2013, 2, 10), dt.date(2013, 2, 10), dt.date(2013, 2, 11), dt.date(2013, 2, 11)]})
```

### Step 2: Assign g = df.groupby(...)

```python
g = df.groupby('date')
```

### Step 3: Assign expected = g.agg(...)

```python
expected = g.agg([P1])
```

### Step 4: Assign expected.columns = value

```python
expected.columns = expected.columns.levels[0]
```

### Step 5: Assign result = g.agg(...)

```python
result = g.agg(P1)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
def P1(a):
    return np.percentile(a.dropna(), q=1)
df = DataFrame({'col1': [1, 2, 3, 4], 'col2': [10, 25, 26, 31], 'date': [dt.date(2013, 2, 10), dt.date(2013, 2, 10), dt.date(2013, 2, 11), dt.date(2013, 2, 11)]})
g = df.groupby('date')
expected = g.agg([P1])
expected.columns = expected.columns.levels[0]
result = g.agg(P1)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_other.py:367 | Complexity: Intermediate | Last updated: 2026-06-02*