# How To: Groupby Dropna Datetime Like Data

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test groupby dropna datetime like data

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.pyarrow`
- `pandas.core.dtypes.missing`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`

**Setup Required:**
```python
# Fixtures: dropna, values, datetime1, datetime2, unique_nulls_fixture, unique_nulls_fixture2
```

## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'values': [1, 2, 3, 4, 5, 6], 'dt': [datetime1, unique_nulls_fixture, datetime2, unique_nulls_fixture2, datetime1, datetime1]})
```

### Step 2: Assign grouped = df.groupby.agg(...)

```python
grouped = df.groupby('dt', dropna=dropna).agg({'values': 'sum'})
```

### Step 3: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'values': values}, index=pd.Index(indexes, name='dt'))
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(grouped, expected)
```

### Step 5: Assign indexes = value

```python
indexes = [datetime1, datetime2]
```

### Step 6: Assign indexes = value

```python
indexes = [datetime1, datetime2, np.nan]
```


## Complete Example

```python
# Setup
# Fixtures: dropna, values, datetime1, datetime2, unique_nulls_fixture, unique_nulls_fixture2

# Workflow
df = pd.DataFrame({'values': [1, 2, 3, 4, 5, 6], 'dt': [datetime1, unique_nulls_fixture, datetime2, unique_nulls_fixture2, datetime1, datetime1]})
if dropna:
    indexes = [datetime1, datetime2]
else:
    indexes = [datetime1, datetime2, np.nan]
grouped = df.groupby('dt', dropna=dropna).agg({'values': 'sum'})
expected = pd.DataFrame({'values': values}, index=pd.Index(indexes, name='dt'))
tm.assert_frame_equal(grouped, expected)
```

## Next Steps


---

*Source: test_groupby_dropna.py:258 | Complexity: Intermediate | Last updated: 2026-06-02*