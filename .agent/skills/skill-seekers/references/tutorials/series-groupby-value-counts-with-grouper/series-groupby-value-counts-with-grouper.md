# How To: Series Groupby Value Counts With Grouper

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test series groupby value counts with grouper

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
# Fixtures: utc
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame.drop(...)

```python
df = DataFrame({'Timestamp': [1565083561, 1565083561 + 86400, 1565083561 + 86500, 1565083561 + 86400 * 2, 1565083561 + 86400 * 3, 1565083561 + 86500 * 3, 1565083561 + 86400 * 4], 'Food': ['apple', 'apple', 'banana', 'banana', 'orange', 'orange', 'pear']}).drop([3])
```

### Step 2: Assign unknown = to_datetime(...)

```python
df['Datetime'] = to_datetime(df['Timestamp'], utc=utc, unit='s')
```

### Step 3: Assign dfg = df.groupby(...)

```python
dfg = df.groupby(Grouper(freq='1D', key='Datetime'))
```

### Step 4: Assign result = unknown.value_counts.sort_index(...)

```python
result = dfg['Food'].value_counts().sort_index()
```

### Step 5: Assign expected = unknown.apply.sort_index(...)

```python
expected = dfg['Food'].apply(Series.value_counts).sort_index()
```

### Step 6: Assign expected.index.names = value

```python
expected.index.names = result.index.names
```

### Step 7: Assign expected = expected.rename(...)

```python
expected = expected.rename('count')
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: utc

# Workflow
df = DataFrame({'Timestamp': [1565083561, 1565083561 + 86400, 1565083561 + 86500, 1565083561 + 86400 * 2, 1565083561 + 86400 * 3, 1565083561 + 86500 * 3, 1565083561 + 86400 * 4], 'Food': ['apple', 'apple', 'banana', 'banana', 'orange', 'orange', 'pear']}).drop([3])
df['Datetime'] = to_datetime(df['Timestamp'], utc=utc, unit='s')
dfg = df.groupby(Grouper(freq='1D', key='Datetime'))
result = dfg['Food'].value_counts().sort_index()
expected = dfg['Food'].apply(Series.value_counts).sort_index()
expected.index.names = result.index.names
expected = expected.rename('count')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_value_counts.py:123 | Complexity: Advanced | Last updated: 2026-06-02*