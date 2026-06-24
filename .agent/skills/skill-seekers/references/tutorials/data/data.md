# How To: Data

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: data

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `decimal`
- `io`
- `operator`
- `pickle`
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas.compat`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.api.extensions`
- `pandas.api.types`
- `pandas.tests.extension`
- `pandas.core.arrays.arrow.array`
- `pandas.core.arrays.arrow.extension_types`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign pa_dtype = value

```python
pa_dtype = dtype.pyarrow_dtype
```

### Step 2: Assign data = value

```python
data = [True, False] * 4 + [None] + [True, False] * 44 + [None] + [True, False]
```

### Step 3: Assign data = value

```python
data = [1.0, 0.0] * 4 + [None] + [-2.0, -1.0] * 44 + [None] + [0.5, 99.5]
```

### Step 4: Assign data = value

```python
data = [1, 0] * 4 + [None] + [-2, -1] * 44 + [None] + [1, 99]
```

### Step 5: Assign data = value

```python
data = [1, 0] * 4 + [None] + [2, 1] * 44 + [None] + [1, 99]
```

### Step 6: Assign data = value

```python
data = [Decimal('1'), Decimal('0.0')] * 4 + [None] + [Decimal('-2.0'), Decimal('-1.0')] * 44 + [None] + [Decimal('0.5'), Decimal('33.123')]
```

### Step 7: Assign data = value

```python
data = [date(2022, 1, 1), date(1999, 12, 31)] * 4 + [None] + [date(2022, 1, 1), date(2022, 1, 1)] * 44 + [None] + [date(1999, 12, 31), date(1999, 12, 31)]
```

### Step 8: Assign data = value

```python
data = [datetime(2020, 1, 1, 1, 1, 1, 1), datetime(1999, 1, 1, 1, 1, 1, 1)] * 4 + [None] + [datetime(2020, 1, 1, 1), datetime(1999, 1, 1, 1)] * 44 + [None] + [datetime(2020, 1, 1), datetime(1999, 1, 1)]
```

### Step 9: Assign data = value

```python
data = [timedelta(1), timedelta(1, 1)] * 4 + [None] + [timedelta(-1), timedelta(0)] * 44 + [None] + [timedelta(-10), timedelta(10)]
```

### Step 10: Assign data = value

```python
data = [time(12, 0), time(0, 12)] * 4 + [None] + [time(0, 0), time(1, 1)] * 44 + [None] + [time(0, 5), time(5, 0)]
```

### Step 11: Assign data = value

```python
data = ['a', 'b'] * 4 + [None] + ['1', '2'] * 44 + [None] + ['!', '>']
```

### Step 12: Assign data = value

```python
data = [b'a', b'b'] * 4 + [None] + [b'1', b'2'] * 44 + [None] + [b'!', b'>']
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
pa_dtype = dtype.pyarrow_dtype
if pa.types.is_boolean(pa_dtype):
    data = [True, False] * 4 + [None] + [True, False] * 44 + [None] + [True, False]
elif pa.types.is_floating(pa_dtype):
    data = [1.0, 0.0] * 4 + [None] + [-2.0, -1.0] * 44 + [None] + [0.5, 99.5]
elif pa.types.is_signed_integer(pa_dtype):
    data = [1, 0] * 4 + [None] + [-2, -1] * 44 + [None] + [1, 99]
elif pa.types.is_unsigned_integer(pa_dtype):
    data = [1, 0] * 4 + [None] + [2, 1] * 44 + [None] + [1, 99]
elif pa.types.is_decimal(pa_dtype):
    data = [Decimal('1'), Decimal('0.0')] * 4 + [None] + [Decimal('-2.0'), Decimal('-1.0')] * 44 + [None] + [Decimal('0.5'), Decimal('33.123')]
elif pa.types.is_date(pa_dtype):
    data = [date(2022, 1, 1), date(1999, 12, 31)] * 4 + [None] + [date(2022, 1, 1), date(2022, 1, 1)] * 44 + [None] + [date(1999, 12, 31), date(1999, 12, 31)]
elif pa.types.is_timestamp(pa_dtype):
    data = [datetime(2020, 1, 1, 1, 1, 1, 1), datetime(1999, 1, 1, 1, 1, 1, 1)] * 4 + [None] + [datetime(2020, 1, 1, 1), datetime(1999, 1, 1, 1)] * 44 + [None] + [datetime(2020, 1, 1), datetime(1999, 1, 1)]
elif pa.types.is_duration(pa_dtype):
    data = [timedelta(1), timedelta(1, 1)] * 4 + [None] + [timedelta(-1), timedelta(0)] * 44 + [None] + [timedelta(-10), timedelta(10)]
elif pa.types.is_time(pa_dtype):
    data = [time(12, 0), time(0, 12)] * 4 + [None] + [time(0, 0), time(1, 1)] * 44 + [None] + [time(0, 5), time(5, 0)]
elif pa.types.is_string(pa_dtype):
    data = ['a', 'b'] * 4 + [None] + ['1', '2'] * 44 + [None] + ['!', '>']
elif pa.types.is_binary(pa_dtype):
    data = [b'a', b'b'] * 4 + [None] + [b'1', b'2'] * 44 + [None] + [b'!', b'>']
else:
    raise NotImplementedError
return pd.array(data, dtype=dtype)
```

## Next Steps


---

*Source: test_arrow.py:90 | Complexity: Advanced | Last updated: 2026-06-02*