# How To: Total Seconds Nanoseconds

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test total seconds nanoseconds

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign start_time = pd.Series.astype(...)

```python
start_time = pd.Series(['2145-11-02 06:00:00']).astype('datetime64[ns]')
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign end_time = pd.Series.astype(...)

```python
end_time = pd.Series(['2145-11-02 07:06:00']).astype('datetime64[ns]')
```

### Step 3: Assign expected = value

```python
expected = (end_time - start_time).values / np.timedelta64(1, 's')
```

### Step 4: Assign result = value

```python
result = (end_time - start_time).dt.total_seconds().values
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
start_time = pd.Series(['2145-11-02 06:00:00']).astype('datetime64[ns]')
end_time = pd.Series(['2145-11-02 07:06:00']).astype('datetime64[ns]')
expected = (end_time - start_time).values / np.timedelta64(1, 's')
result = (end_time - start_time).dt.total_seconds().values
assert result == expected
```

## Next Steps


---

*Source: test_timedeltas.py:73 | Complexity: Intermediate | Last updated: 2026-06-02*