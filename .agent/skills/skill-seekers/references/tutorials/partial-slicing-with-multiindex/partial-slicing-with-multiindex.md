# How To: Partial Slicing With Multiindex

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test partial slicing with multiindex

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'ACCOUNT': ['ACCT1', 'ACCT1', 'ACCT1', 'ACCT2'], 'TICKER': ['ABC', 'MNP', 'XYZ', 'XYZ'], 'val': [1, 2, 3, 4]}, index=date_range('2013-06-19 09:30:00', periods=4, freq='5min'))
```

### Step 2: Assign df_multi = df.set_index(...)

```python
df_multi = df.set_index(['ACCOUNT', 'TICKER'], append=True)
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1]], index=Index(['ABC'], name='TICKER'), columns=['val'])
```

### Step 4: Assign result = value

```python
result = df_multi.loc['2013-06-19 09:30:00', 'ACCT1']
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign expected = value

```python
expected = df_multi.loc[Timestamp('2013-06-19 09:30:00', tz=None), 'ACCT1', 'ABC']
```

### Step 7: Assign result = value

```python
result = df_multi.loc['2013-06-19 09:30:00', 'ACCT1', 'ABC']
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 9: Assign result = value

```python
result = df_multi.loc['2013-06-19', 'ACCT1', 'ABC']
```

### Step 10: Assign expected = unknown.droplevel(...)

```python
expected = df_multi.iloc[:1].droplevel([1, 2])
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'ACCOUNT': ['ACCT1', 'ACCT1', 'ACCT1', 'ACCT2'], 'TICKER': ['ABC', 'MNP', 'XYZ', 'XYZ'], 'val': [1, 2, 3, 4]}, index=date_range('2013-06-19 09:30:00', periods=4, freq='5min'))
df_multi = df.set_index(['ACCOUNT', 'TICKER'], append=True)
expected = DataFrame([[1]], index=Index(['ABC'], name='TICKER'), columns=['val'])
result = df_multi.loc['2013-06-19 09:30:00', 'ACCT1']
tm.assert_frame_equal(result, expected)
expected = df_multi.loc[Timestamp('2013-06-19 09:30:00', tz=None), 'ACCT1', 'ABC']
result = df_multi.loc['2013-06-19 09:30:00', 'ACCT1', 'ABC']
tm.assert_series_equal(result, expected)
result = df_multi.loc['2013-06-19', 'ACCT1', 'ABC']
expected = df_multi.iloc[:1].droplevel([1, 2])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_partial_slicing.py:331 | Complexity: Advanced | Last updated: 2026-06-02*