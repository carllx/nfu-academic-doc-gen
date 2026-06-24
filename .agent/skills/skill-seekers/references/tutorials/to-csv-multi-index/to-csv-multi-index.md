# How To: To Csv Multi Index

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to csv multi index

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
df = DataFrame([1], columns=pd.MultiIndex.from_arrays([[1], [2]]))
```

**Verification:**
```python
assert df.to_csv() == exp
```

### Step 2: Assign exp_rows = value

```python
exp_rows = [',1', ',2', '0,1']
```

**Verification:**
```python
assert df.to_csv(index=False) == exp
```

### Step 3: Assign exp = tm.convert_rows_list_to_csv_str(...)

```python
exp = tm.convert_rows_list_to_csv_str(exp_rows)
```

**Verification:**
```python
assert df.to_csv() == exp
```

### Step 4: Assign exp_rows = value

```python
exp_rows = ['1', '2', '1']
```

**Verification:**
```python
assert df.to_csv(index=False) == exp
```

### Step 5: Assign exp = tm.convert_rows_list_to_csv_str(...)

```python
exp = tm.convert_rows_list_to_csv_str(exp_rows)
```

**Verification:**
```python
assert df.to_csv() == exp
```

### Step 6: Assign df = DataFrame(...)

```python
df = DataFrame([1], columns=pd.MultiIndex.from_arrays([[1], [2]]), index=pd.MultiIndex.from_arrays([[1], [2]]))
```

**Verification:**
```python
assert df.to_csv(index=False) == exp
```

### Step 7: Assign exp_rows = value

```python
exp_rows = [',,1', ',,2', '1,2,1']
```

### Step 8: Assign exp = tm.convert_rows_list_to_csv_str(...)

```python
exp = tm.convert_rows_list_to_csv_str(exp_rows)
```

**Verification:**
```python
assert df.to_csv() == exp
```

### Step 9: Assign exp_rows = value

```python
exp_rows = ['1', '2', '1']
```

### Step 10: Assign exp = tm.convert_rows_list_to_csv_str(...)

```python
exp = tm.convert_rows_list_to_csv_str(exp_rows)
```

**Verification:**
```python
assert df.to_csv(index=False) == exp
```

### Step 11: Assign df = DataFrame(...)

```python
df = DataFrame([1], columns=pd.MultiIndex.from_arrays([['foo'], ['bar']]))
```

### Step 12: Assign exp_rows = value

```python
exp_rows = [',foo', ',bar', '0,1']
```

### Step 13: Assign exp = tm.convert_rows_list_to_csv_str(...)

```python
exp = tm.convert_rows_list_to_csv_str(exp_rows)
```

**Verification:**
```python
assert df.to_csv() == exp
```

### Step 14: Assign exp_rows = value

```python
exp_rows = ['foo', 'bar', '1']
```

### Step 15: Assign exp = tm.convert_rows_list_to_csv_str(...)

```python
exp = tm.convert_rows_list_to_csv_str(exp_rows)
```

**Verification:**
```python
assert df.to_csv(index=False) == exp
```


## Complete Example

```python
# Workflow
df = DataFrame([1], columns=pd.MultiIndex.from_arrays([[1], [2]]))
exp_rows = [',1', ',2', '0,1']
exp = tm.convert_rows_list_to_csv_str(exp_rows)
assert df.to_csv() == exp
exp_rows = ['1', '2', '1']
exp = tm.convert_rows_list_to_csv_str(exp_rows)
assert df.to_csv(index=False) == exp
df = DataFrame([1], columns=pd.MultiIndex.from_arrays([[1], [2]]), index=pd.MultiIndex.from_arrays([[1], [2]]))
exp_rows = [',,1', ',,2', '1,2,1']
exp = tm.convert_rows_list_to_csv_str(exp_rows)
assert df.to_csv() == exp
exp_rows = ['1', '2', '1']
exp = tm.convert_rows_list_to_csv_str(exp_rows)
assert df.to_csv(index=False) == exp
df = DataFrame([1], columns=pd.MultiIndex.from_arrays([['foo'], ['bar']]))
exp_rows = [',foo', ',bar', '0,1']
exp = tm.convert_rows_list_to_csv_str(exp_rows)
assert df.to_csv() == exp
exp_rows = ['foo', 'bar', '1']
exp = tm.convert_rows_list_to_csv_str(exp_rows)
assert df.to_csv(index=False) == exp
```

## Next Steps


---

*Source: test_to_csv.py:335 | Complexity: Advanced | Last updated: 2026-06-02*