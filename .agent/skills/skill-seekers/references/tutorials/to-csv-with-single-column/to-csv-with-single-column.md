# How To: To Csv With Single Column

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to csv with single column

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

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame([None, 1])
```

**Verification:**
```python
assert f.read() == expected1
```

### Step 2: Assign expected1 = '""\n1.0\n'

```python
expected1 = '""\n1.0\n'
```

**Verification:**
```python
assert f.read() == expected2
```

### Step 3: Assign df2 = DataFrame(...)

```python
df2 = DataFrame([1, None])
```

### Step 4: Assign expected2 = '1.0\n""\n'

```python
expected2 = '1.0\n""\n'
```

### Step 5: Call df1.to_csv()

```python
df1.to_csv(path, header=None, index=None)
```

### Step 6: Call df2.to_csv()

```python
df2.to_csv(path, header=None, index=None)
```

**Verification:**
```python
assert f.read() == expected1
```


## Complete Example

```python
# Workflow
df1 = DataFrame([None, 1])
expected1 = '""\n1.0\n'
with tm.ensure_clean('test.csv') as path:
    df1.to_csv(path, header=None, index=None)
    with open(path, encoding='utf-8') as f:
        assert f.read() == expected1
df2 = DataFrame([1, None])
expected2 = '1.0\n""\n'
with tm.ensure_clean('test.csv') as path:
    df2.to_csv(path, header=None, index=None)
    with open(path, encoding='utf-8') as f:
        assert f.read() == expected2
```

## Next Steps


---

*Source: test_to_csv.py:20 | Complexity: Intermediate | Last updated: 2026-06-02*