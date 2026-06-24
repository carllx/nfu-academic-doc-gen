# How To: To Dict Timestamp

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to dict timestamp

## Prerequisites

**Required Modules:**
- `collections`
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign tsmp = Timestamp(...)

```python
tsmp = Timestamp('20130101')
```

**Verification:**
```python
assert test_data.to_dict(orient='records') == expected_records
```

### Step 2: Assign test_data = DataFrame(...)

```python
test_data = DataFrame({'A': [tsmp, tsmp], 'B': [tsmp, tsmp]})
```

**Verification:**
```python
assert test_data_mixed.to_dict(orient='records') == expected_records_mixed
```

### Step 3: Assign test_data_mixed = DataFrame(...)

```python
test_data_mixed = DataFrame({'A': [tsmp, tsmp], 'B': [1, 2]})
```

### Step 4: Assign expected_records = value

```python
expected_records = [{'A': tsmp, 'B': tsmp}, {'A': tsmp, 'B': tsmp}]
```

### Step 5: Assign expected_records_mixed = value

```python
expected_records_mixed = [{'A': tsmp, 'B': 1}, {'A': tsmp, 'B': 2}]
```

**Verification:**
```python
assert test_data.to_dict(orient='records') == expected_records
```

### Step 6: Assign expected_series = value

```python
expected_series = {'A': Series([tsmp, tsmp], name='A'), 'B': Series([tsmp, tsmp], name='B')}
```

### Step 7: Assign expected_series_mixed = value

```python
expected_series_mixed = {'A': Series([tsmp, tsmp], name='A'), 'B': Series([1, 2], name='B')}
```

### Step 8: Call tm.assert_dict_equal()

```python
tm.assert_dict_equal(test_data.to_dict(orient='series'), expected_series)
```

### Step 9: Call tm.assert_dict_equal()

```python
tm.assert_dict_equal(test_data_mixed.to_dict(orient='series'), expected_series_mixed)
```

### Step 10: Assign expected_split = value

```python
expected_split = {'index': [0, 1], 'data': [[tsmp, tsmp], [tsmp, tsmp]], 'columns': ['A', 'B']}
```

### Step 11: Assign expected_split_mixed = value

```python
expected_split_mixed = {'index': [0, 1], 'data': [[tsmp, 1], [tsmp, 2]], 'columns': ['A', 'B']}
```

### Step 12: Call tm.assert_dict_equal()

```python
tm.assert_dict_equal(test_data.to_dict(orient='split'), expected_split)
```

### Step 13: Call tm.assert_dict_equal()

```python
tm.assert_dict_equal(test_data_mixed.to_dict(orient='split'), expected_split_mixed)
```


## Complete Example

```python
# Workflow
tsmp = Timestamp('20130101')
test_data = DataFrame({'A': [tsmp, tsmp], 'B': [tsmp, tsmp]})
test_data_mixed = DataFrame({'A': [tsmp, tsmp], 'B': [1, 2]})
expected_records = [{'A': tsmp, 'B': tsmp}, {'A': tsmp, 'B': tsmp}]
expected_records_mixed = [{'A': tsmp, 'B': 1}, {'A': tsmp, 'B': 2}]
assert test_data.to_dict(orient='records') == expected_records
assert test_data_mixed.to_dict(orient='records') == expected_records_mixed
expected_series = {'A': Series([tsmp, tsmp], name='A'), 'B': Series([tsmp, tsmp], name='B')}
expected_series_mixed = {'A': Series([tsmp, tsmp], name='A'), 'B': Series([1, 2], name='B')}
tm.assert_dict_equal(test_data.to_dict(orient='series'), expected_series)
tm.assert_dict_equal(test_data_mixed.to_dict(orient='series'), expected_series_mixed)
expected_split = {'index': [0, 1], 'data': [[tsmp, tsmp], [tsmp, tsmp]], 'columns': ['A', 'B']}
expected_split_mixed = {'index': [0, 1], 'data': [[tsmp, 1], [tsmp, 2]], 'columns': ['A', 'B']}
tm.assert_dict_equal(test_data.to_dict(orient='split'), expected_split)
tm.assert_dict_equal(test_data_mixed.to_dict(orient='split'), expected_split_mixed)
```

## Next Steps


---

*Source: test_to_dict.py:26 | Complexity: Advanced | Last updated: 2026-06-02*