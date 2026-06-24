# How To: Series Groupby Value Counts One Row

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test series groupby value counts one row

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.util.version`

**Setup Required:**
```python
# Fixtures: columns
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(data=[range(len(columns))], columns=columns)
```

### Step 2: Assign dfg = df.groupby(...)

```python
dfg = df.groupby(columns[:-1])
```

### Step 3: Assign result = unknown.value_counts(...)

```python
result = dfg[columns[-1]].value_counts()
```

### Step 4: Assign expected = df.value_counts(...)

```python
expected = df.value_counts()
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: columns

# Workflow
df = DataFrame(data=[range(len(columns))], columns=columns)
dfg = df.groupby(columns[:-1])
result = dfg[columns[-1]].value_counts()
expected = df.value_counts()
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_value_counts.py:167 | Complexity: Intermediate | Last updated: 2026-06-02*