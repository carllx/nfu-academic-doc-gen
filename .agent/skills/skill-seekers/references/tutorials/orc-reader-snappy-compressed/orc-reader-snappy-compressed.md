# How To: Orc Reader Snappy Compressed

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test orc reader snappy compressed

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
data = {'int1': np.array([-1160101563, 1181413113, 2065821249, -267157795, 172111193, 1752363137, 1406072123, 1911809390, -1308542224, -467100286], dtype='int32'), 'string1': np.array(['f50dcb8', '382fdaaa', '90758c6', '9e8caf3f', 'ee97332b', 'd634da1', '2bea4396', 'd67d89e8', 'ad71007e', 'e8c82066'], dtype='object')}
```

### Step 2: Assign expected = pd.DataFrame.from_dict(...)

```python
expected = pd.DataFrame.from_dict(data)
```

### Step 3: Assign inputfile = os.path.join(...)

```python
inputfile = os.path.join(dirpath, 'TestOrcFile.testSnappy.orc')
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
data = {'int1': np.array([-1160101563, 1181413113, 2065821249, -267157795, 172111193, 1752363137, 1406072123, 1911809390, -1308542224, -467100286], dtype='int32'), 'string1': np.array(['f50dcb8', '382fdaaa', '90758c6', '9e8caf3f', 'ee97332b', 'd634da1', '2bea4396', 'd67d89e8', 'ad71007e', 'e8c82066'], dtype='object')}
expected = pd.DataFrame.from_dict(data)
inputfile = os.path.join(dirpath, 'TestOrcFile.testSnappy.orc')
got = read_orc(inputfile).iloc[:10]
tm.assert_equal(expected, got)
```

## Next Steps


---

*Source: test_orc.py:208 | Complexity: Intermediate | Last updated: 2026-06-02*