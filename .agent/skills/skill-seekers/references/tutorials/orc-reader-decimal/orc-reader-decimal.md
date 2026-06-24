# How To: Orc Reader Decimal

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test orc reader decimal

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `io`
- `os`
- `pathlib`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pyarrow`

**Setup Required:**
```python
# Fixtures: dirpath
```

## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = {'_col0': np.array([Decimal('-1000.50000'), Decimal('-999.60000'), Decimal('-998.70000'), Decimal('-997.80000'), Decimal('-996.90000'), Decimal('-995.10000'), Decimal('-994.11000'), Decimal('-993.12000'), Decimal('-992.13000'), Decimal('-991.14000')], dtype='object')}
```

### Step 2: Assign expected = pd.DataFrame.from_dict(...)

```python
expected = pd.DataFrame.from_dict(data)
```

### Step 3: Assign inputfile = os.path.join(...)

```python
inputfile = os.path.join(dirpath, 'TestOrcFile.decimal.orc')
```

### Step 4: Assign got = value

```python
got = read_orc(inputfile).iloc[:10]
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(expected, got)
```


## Complete Example

```python
# Setup
# Fixtures: dirpath

# Workflow
data = {'_col0': np.array([Decimal('-1000.50000'), Decimal('-999.60000'), Decimal('-998.70000'), Decimal('-997.80000'), Decimal('-996.90000'), Decimal('-995.10000'), Decimal('-994.11000'), Decimal('-993.12000'), Decimal('-992.13000'), Decimal('-991.14000')], dtype='object')}
expected = pd.DataFrame.from_dict(data)
inputfile = os.path.join(dirpath, 'TestOrcFile.decimal.orc')
got = read_orc(inputfile).iloc[:10]
tm.assert_equal(expected, got)
```

## Next Steps


---

*Source: test_orc.py:99 | Complexity: Intermediate | Last updated: 2026-06-02*