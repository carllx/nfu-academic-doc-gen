# How To: To Csv Na Rep

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to csv na rep

## Prerequisites

**Required Modules:**
- `io`
- `os`
- `sys`
- `zipfile`
- `_csv`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [0, np.nan], 'b': [0, 1], 'c': [2, 3]})
```

**Verification:**
```python
assert df.set_index('a').to_csv(na_rep='_') == expected
```

### Step 2: Assign expected_rows = value

```python
expected_rows = ['a,b,c', '0.0,0,2', '_,1,3']
```

**Verification:**
```python
assert df.set_index(['a', 'b']).to_csv(na_rep='_') == expected
```

### Step 3: Assign expected = tm.convert_rows_list_to_csv_str(...)

```python
expected = tm.convert_rows_list_to_csv_str(expected_rows)
```

**Verification:**
```python
assert df.set_index('a').to_csv(na_rep='_') == expected
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame({'a': np.nan, 'b': [0, 1], 'c': [2, 3]})
```

**Verification:**
```python
assert df.set_index(['a', 'b']).to_csv(na_rep='_') == expected
```

### Step 5: Assign expected_rows = value

```python
expected_rows = ['a,b,c', '_,0,2', '_,1,3']
```

**Verification:**
```python
assert df.set_index('a').to_csv(na_rep='_') == expected
```

### Step 6: Assign expected = tm.convert_rows_list_to_csv_str(...)

```python
expected = tm.convert_rows_list_to_csv_str(expected_rows)
```

**Verification:**
```python
assert df.set_index(['a', 'b']).to_csv(na_rep='_') == expected
```

### Step 7: Assign df = DataFrame(...)

```python
df = DataFrame({'a': 0, 'b': [0, 1], 'c': [2, 3]})
```

**Verification:**
```python
assert expected == csv
```

### Step 8: Assign expected_rows = value

```python
expected_rows = ['a,b,c', '0,0,2', '0,1,3']
```

### Step 9: Assign expected = tm.convert_rows_list_to_csv_str(...)

```python
expected = tm.convert_rows_list_to_csv_str(expected_rows)
```

**Verification:**
```python
assert df.set_index('a').to_csv(na_rep='_') == expected
```

### Step 10: Assign csv = pd.Series.to_csv(...)

```python
csv = pd.Series(['a', pd.NA, 'c']).to_csv(na_rep='ZZZZZ')
```

### Step 11: Assign expected = tm.convert_rows_list_to_csv_str(...)

```python
expected = tm.convert_rows_list_to_csv_str([',0', '0,a', '1,ZZZZZ', '2,c'])
```

**Verification:**
```python
assert expected == csv
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [0, np.nan], 'b': [0, 1], 'c': [2, 3]})
expected_rows = ['a,b,c', '0.0,0,2', '_,1,3']
expected = tm.convert_rows_list_to_csv_str(expected_rows)
assert df.set_index('a').to_csv(na_rep='_') == expected
assert df.set_index(['a', 'b']).to_csv(na_rep='_') == expected
df = DataFrame({'a': np.nan, 'b': [0, 1], 'c': [2, 3]})
expected_rows = ['a,b,c', '_,0,2', '_,1,3']
expected = tm.convert_rows_list_to_csv_str(expected_rows)
assert df.set_index('a').to_csv(na_rep='_') == expected
assert df.set_index(['a', 'b']).to_csv(na_rep='_') == expected
df = DataFrame({'a': 0, 'b': [0, 1], 'c': [2, 3]})
expected_rows = ['a,b,c', '0,0,2', '0,1,3']
expected = tm.convert_rows_list_to_csv_str(expected_rows)
assert df.set_index('a').to_csv(na_rep='_') == expected
assert df.set_index(['a', 'b']).to_csv(na_rep='_') == expected
csv = pd.Series(['a', pd.NA, 'c']).to_csv(na_rep='ZZZZZ')
expected = tm.convert_rows_list_to_csv_str([',0', '0,a', '1,ZZZZZ', '2,c'])
assert expected == csv
```

## Next Steps


---

*Source: test_to_csv.py:181 | Complexity: Advanced | Last updated: 2026-06-02*