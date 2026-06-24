# How To: To Csv Decimal

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to csv decimal

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
df = DataFrame({'col1': [1], 'col2': ['a'], 'col3': [10.1]})
```

**Verification:**
```python
assert df.to_csv() == expected_default
```

### Step 2: Assign expected_rows = value

```python
expected_rows = [',col1,col2,col3', '0,1,a,10.1']
```

**Verification:**
```python
assert df.to_csv(decimal=',', sep=';') == expected_european_excel
```

### Step 3: Assign expected_default = tm.convert_rows_list_to_csv_str(...)

```python
expected_default = tm.convert_rows_list_to_csv_str(expected_rows)
```

**Verification:**
```python
assert df.to_csv(float_format='%.2f') == expected_float_format_default
```

### Step 4: Assign expected_rows = value

```python
expected_rows = [';col1;col2;col3', '0;1;a;10,1']
```

**Verification:**
```python
assert df.to_csv(decimal=',', sep=';', float_format='%.2f') == expected_float_format
```

### Step 5: Assign expected_european_excel = tm.convert_rows_list_to_csv_str(...)

```python
expected_european_excel = tm.convert_rows_list_to_csv_str(expected_rows)
```

**Verification:**
```python
assert df.to_csv(index=False, decimal='^') == expected
```

### Step 6: Assign expected_rows = value

```python
expected_rows = [',col1,col2,col3', '0,1,a,10.10']
```

**Verification:**
```python
assert df.set_index('a').to_csv(decimal='^') == expected
```

### Step 7: Assign expected_float_format_default = tm.convert_rows_list_to_csv_str(...)

```python
expected_float_format_default = tm.convert_rows_list_to_csv_str(expected_rows)
```

**Verification:**
```python
assert df.set_index(['a', 'b']).to_csv(decimal='^') == expected
```

### Step 8: Assign expected_rows = value

```python
expected_rows = [';col1;col2;col3', '0;1;a;10,10']
```

### Step 9: Assign expected_float_format = tm.convert_rows_list_to_csv_str(...)

```python
expected_float_format = tm.convert_rows_list_to_csv_str(expected_rows)
```

**Verification:**
```python
assert df.to_csv(decimal=',', sep=';', float_format='%.2f') == expected_float_format
```

### Step 10: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [0, 1.1], 'b': [2.2, 3.3], 'c': 1})
```

### Step 11: Assign expected_rows = value

```python
expected_rows = ['a,b,c', '0^0,2^2,1', '1^1,3^3,1']
```

### Step 12: Assign expected = tm.convert_rows_list_to_csv_str(...)

```python
expected = tm.convert_rows_list_to_csv_str(expected_rows)
```

**Verification:**
```python
assert df.to_csv(index=False, decimal='^') == expected
```


## Complete Example

```python
# Workflow
df = DataFrame({'col1': [1], 'col2': ['a'], 'col3': [10.1]})
expected_rows = [',col1,col2,col3', '0,1,a,10.1']
expected_default = tm.convert_rows_list_to_csv_str(expected_rows)
assert df.to_csv() == expected_default
expected_rows = [';col1;col2;col3', '0;1;a;10,1']
expected_european_excel = tm.convert_rows_list_to_csv_str(expected_rows)
assert df.to_csv(decimal=',', sep=';') == expected_european_excel
expected_rows = [',col1,col2,col3', '0,1,a,10.10']
expected_float_format_default = tm.convert_rows_list_to_csv_str(expected_rows)
assert df.to_csv(float_format='%.2f') == expected_float_format_default
expected_rows = [';col1;col2;col3', '0;1;a;10,10']
expected_float_format = tm.convert_rows_list_to_csv_str(expected_rows)
assert df.to_csv(decimal=',', sep=';', float_format='%.2f') == expected_float_format
df = DataFrame({'a': [0, 1.1], 'b': [2.2, 3.3], 'c': 1})
expected_rows = ['a,b,c', '0^0,2^2,1', '1^1,3^3,1']
expected = tm.convert_rows_list_to_csv_str(expected_rows)
assert df.to_csv(index=False, decimal='^') == expected
assert df.set_index('a').to_csv(decimal='^') == expected
assert df.set_index(['a', 'b']).to_csv(decimal='^') == expected
```

## Next Steps


---

*Source: test_to_csv.py:133 | Complexity: Advanced | Last updated: 2026-06-02*