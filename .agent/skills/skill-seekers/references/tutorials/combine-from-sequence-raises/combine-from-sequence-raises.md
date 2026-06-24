# How To: Combine From Sequence Raises

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test combine from sequence raises

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`
- `pandas.tests.extension`
- `pandas.tests.extension.decimal.array`

**Setup Required:**
```python
# Fixtures: monkeypatch
```

## Step-by-Step Guide

### Step 1: Assign cls = DecimalArrayWithoutFromSequence

```python
cls = DecimalArrayWithoutFromSequence
```

### Step 2: Call monkeypatch.setattr()

```python
monkeypatch.setattr(DecimalDtype, 'construct_array_type', construct_array_type)
```

### Step 3: Assign arr = cls(...)

```python
arr = cls([decimal.Decimal('1.0'), decimal.Decimal('2.0')])
```

### Step 4: Assign ser = pd.Series(...)

```python
ser = pd.Series(arr)
```

### Step 5: Assign result = ser.combine(...)

```python
result = ser.combine(ser, operator.add)
```

### Step 6: Assign expected = pd.Series(...)

```python
expected = pd.Series([decimal.Decimal('2.0'), decimal.Decimal('4.0')], dtype='object')
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: monkeypatch

# Workflow
cls = DecimalArrayWithoutFromSequence

@classmethod
def construct_array_type(cls):
    return DecimalArrayWithoutFromSequence
monkeypatch.setattr(DecimalDtype, 'construct_array_type', construct_array_type)
arr = cls([decimal.Decimal('1.0'), decimal.Decimal('2.0')])
ser = pd.Series(arr)
result = ser.combine(ser, operator.add)
expected = pd.Series([decimal.Decimal('2.0'), decimal.Decimal('4.0')], dtype='object')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_decimal.py:394 | Complexity: Intermediate | Last updated: 2026-06-02*