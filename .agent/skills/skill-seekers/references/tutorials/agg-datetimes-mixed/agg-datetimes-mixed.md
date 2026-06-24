# How To: Agg Datetimes Mixed

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test agg datetimes mixed

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

### Step 1: Assign data = value

```python
data = [[1, '2012-01-01', 1.0], [2, '2012-01-02', 2.0], [3, None, 3.0]]
```

**Verification:**
```python
assert len(gb1) == len(gb2)
```

### Step 2: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'key': [x[0] for x in data], 'date': [x[1] for x in data], 'value': [x[2] for x in data]})
```

### Step 3: Assign data = value

```python
data = [[row[0], dt.datetime.strptime(row[1], '%Y-%m-%d').date() if row[1] else None, row[2]] for row in data]
```

### Step 4: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'key': [x[0] for x in data], 'date': [x[1] for x in data], 'value': [x[2] for x in data]})
```

### Step 5: Assign unknown = value

```python
df1['weights'] = df1['value'] / df1['value'].sum()
```

### Step 6: Assign gb1 = df1.groupby.aggregate(...)

```python
gb1 = df1.groupby('date').aggregate('sum')
```

### Step 7: Assign unknown = value

```python
df2['weights'] = df1['value'] / df1['value'].sum()
```

### Step 8: Assign gb2 = df2.groupby.aggregate(...)

```python
gb2 = df2.groupby('date').aggregate('sum')
```

**Verification:**
```python
assert len(gb1) == len(gb2)
```


## Complete Example

```python
# Workflow
data = [[1, '2012-01-01', 1.0], [2, '2012-01-02', 2.0], [3, None, 3.0]]
df1 = DataFrame({'key': [x[0] for x in data], 'date': [x[1] for x in data], 'value': [x[2] for x in data]})
data = [[row[0], dt.datetime.strptime(row[1], '%Y-%m-%d').date() if row[1] else None, row[2]] for row in data]
df2 = DataFrame({'key': [x[0] for x in data], 'date': [x[1] for x in data], 'value': [x[2] for x in data]})
df1['weights'] = df1['value'] / df1['value'].sum()
gb1 = df1.groupby('date').aggregate('sum')
df2['weights'] = df1['value'] / df1['value'].sum()
gb2 = df2.groupby('date').aggregate('sum')
assert len(gb1) == len(gb2)
```

## Next Steps


---

*Source: test_other.py:51 | Complexity: Advanced | Last updated: 2026-06-02*