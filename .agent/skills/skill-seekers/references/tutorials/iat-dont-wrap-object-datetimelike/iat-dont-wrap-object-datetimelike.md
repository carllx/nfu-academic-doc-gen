# How To: Iat Dont Wrap Object Datetimelike

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test iat dont wrap object datetimelike

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2016-01-01', periods=3)
```

**Verification:**
```python
assert (df.dtypes == object).all()
```

### Step 2: Assign tdi = value

```python
tdi = dti - dti
```

**Verification:**
```python
assert result is ser[0]
```

### Step 3: Assign ser = Series(...)

```python
ser = Series(dti.to_pydatetime(), dtype=object)
```

**Verification:**
```python
assert isinstance(result, datetime)
```

### Step 4: Assign ser2 = Series(...)

```python
ser2 = Series(tdi.to_pytimedelta(), dtype=object)
```

**Verification:**
```python
assert not isinstance(result, Timestamp)
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame({'A': ser, 'B': ser2})
```

**Verification:**
```python
assert result is ser2[1]
```


## Complete Example

```python
# Workflow
dti = date_range('2016-01-01', periods=3)
tdi = dti - dti
ser = Series(dti.to_pydatetime(), dtype=object)
ser2 = Series(tdi.to_pytimedelta(), dtype=object)
df = DataFrame({'A': ser, 'B': ser2})
assert (df.dtypes == object).all()
for result in [df.at[0, 'A'], df.iat[0, 0], df.loc[0, 'A'], df.iloc[0, 0]]:
    assert result is ser[0]
    assert isinstance(result, datetime)
    assert not isinstance(result, Timestamp)
for result in [df.at[1, 'B'], df.iat[1, 1], df.loc[1, 'B'], df.iloc[1, 1]]:
    assert result is ser2[1]
    assert isinstance(result, timedelta)
    assert not isinstance(result, Timedelta)
```

## Next Steps


---

*Source: test_scalar.py:215 | Complexity: Intermediate | Last updated: 2026-06-02*