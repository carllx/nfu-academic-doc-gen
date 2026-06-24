# How To: Get Values For Csv

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get values for csv

## Prerequisites

**Required Modules:**
- `contextlib`
- `datetime`
- `locale`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index = PeriodIndex(...)

```python
index = PeriodIndex(['2017-01-01', '2017-01-02', '2017-01-03'], freq='D')
```

### Step 2: Assign expected = np.array(...)

```python
expected = np.array(['2017-01-01', '2017-01-02', '2017-01-03'], dtype=object)
```

### Step 3: Assign result = index._get_values_for_csv(...)

```python
result = index._get_values_for_csv()
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 5: Assign result = index._get_values_for_csv(...)

```python
result = index._get_values_for_csv(na_rep='pandas')
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 7: Assign expected = np.array(...)

```python
expected = np.array(['01-2017-01', '01-2017-02', '01-2017-03'], dtype=object)
```

### Step 8: Assign result = index._get_values_for_csv(...)

```python
result = index._get_values_for_csv(date_format='%m-%Y-%d')
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 10: Assign index = PeriodIndex(...)

```python
index = PeriodIndex(['2017-01-01', pd.NaT, '2017-01-03'], freq='D')
```

### Step 11: Assign expected = np.array(...)

```python
expected = np.array(['2017-01-01', 'NaT', '2017-01-03'], dtype=object)
```

### Step 12: Assign result = index._get_values_for_csv(...)

```python
result = index._get_values_for_csv(na_rep='NaT')
```

### Step 13: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 14: Assign expected = np.array(...)

```python
expected = np.array(['2017-01-01', 'pandas', '2017-01-03'], dtype=object)
```

### Step 15: Assign result = index._get_values_for_csv(...)

```python
result = index._get_values_for_csv(na_rep='pandas')
```

### Step 16: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
index = PeriodIndex(['2017-01-01', '2017-01-02', '2017-01-03'], freq='D')
expected = np.array(['2017-01-01', '2017-01-02', '2017-01-03'], dtype=object)
result = index._get_values_for_csv()
tm.assert_numpy_array_equal(result, expected)
result = index._get_values_for_csv(na_rep='pandas')
tm.assert_numpy_array_equal(result, expected)
expected = np.array(['01-2017-01', '01-2017-02', '01-2017-03'], dtype=object)
result = index._get_values_for_csv(date_format='%m-%Y-%d')
tm.assert_numpy_array_equal(result, expected)
index = PeriodIndex(['2017-01-01', pd.NaT, '2017-01-03'], freq='D')
expected = np.array(['2017-01-01', 'NaT', '2017-01-03'], dtype=object)
result = index._get_values_for_csv(na_rep='NaT')
tm.assert_numpy_array_equal(result, expected)
expected = np.array(['2017-01-01', 'pandas', '2017-01-03'], dtype=object)
result = index._get_values_for_csv(na_rep='pandas')
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_formats.py:26 | Complexity: Advanced | Last updated: 2026-06-02*