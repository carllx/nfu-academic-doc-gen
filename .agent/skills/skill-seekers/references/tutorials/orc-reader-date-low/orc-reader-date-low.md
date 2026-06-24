# How To: Orc Reader Date Low

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test orc reader date low

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
data = {'time': np.array(['1900-05-05 12:34:56.100000', '1900-05-05 12:34:56.100100', '1900-05-05 12:34:56.100200', '1900-05-05 12:34:56.100300', '1900-05-05 12:34:56.100400', '1900-05-05 12:34:56.100500', '1900-05-05 12:34:56.100600', '1900-05-05 12:34:56.100700', '1900-05-05 12:34:56.100800', '1900-05-05 12:34:56.100900'], dtype='datetime64[ns]'), 'date': np.array([datetime.date(1900, 12, 25), datetime.date(1900, 12, 25), datetime.date(1900, 12, 25), datetime.date(1900, 12, 25), datetime.date(1900, 12, 25), datetime.date(1900, 12, 25), datetime.date(1900, 12, 25), datetime.date(1900, 12, 25), datetime.date(1900, 12, 25), datetime.date(1900, 12, 25)], dtype='object')}
```

### Step 2: Assign expected = pd.DataFrame.from_dict(...)

```python
expected = pd.DataFrame.from_dict(data)
```

### Step 3: Assign inputfile = os.path.join(...)

```python
inputfile = os.path.join(dirpath, 'TestOrcFile.testDate1900.orc')
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
data = {'time': np.array(['1900-05-05 12:34:56.100000', '1900-05-05 12:34:56.100100', '1900-05-05 12:34:56.100200', '1900-05-05 12:34:56.100300', '1900-05-05 12:34:56.100400', '1900-05-05 12:34:56.100500', '1900-05-05 12:34:56.100600', '1900-05-05 12:34:56.100700', '1900-05-05 12:34:56.100800', '1900-05-05 12:34:56.100900'], dtype='datetime64[ns]'), 'date': np.array([datetime.date(1900, 12, 25), datetime.date(1900, 12, 25), datetime.date(1900, 12, 25), datetime.date(1900, 12, 25), datetime.date(1900, 12, 25), datetime.date(1900, 12, 25), datetime.date(1900, 12, 25), datetime.date(1900, 12, 25), datetime.date(1900, 12, 25), datetime.date(1900, 12, 25)], dtype='object')}
expected = pd.DataFrame.from_dict(data)
inputfile = os.path.join(dirpath, 'TestOrcFile.testDate1900.orc')
got = read_orc(inputfile).iloc[:10]
tm.assert_equal(expected, got)
```

## Next Steps


---

*Source: test_orc.py:126 | Complexity: Intermediate | Last updated: 2026-06-02*