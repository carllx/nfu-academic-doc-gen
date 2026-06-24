# How To: Date Time

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test date time

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `datetime`
- `io`
- `os`
- `pathlib`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.io.sas.sas7bdat`
- `py.path`

**Setup Required:**
```python
# Fixtures: datapath
```

## Step-by-Step Guide

### Step 1: Assign fname = datapath(...)

```python
fname = datapath('io', 'sas', 'data', 'datetime.sas7bdat')
```

### Step 2: Assign df = pd.read_sas(...)

```python
df = pd.read_sas(fname)
```

### Step 3: Assign fname = datapath(...)

```python
fname = datapath('io', 'sas', 'data', 'datetime.csv')
```

### Step 4: Assign df0 = pd.read_csv(...)

```python
df0 = pd.read_csv(fname, parse_dates=['Date1', 'Date2', 'DateTime', 'DateTimeHi', 'Taiw'])
```

### Step 5: Assign unknown = unknown.dt.round(...)

```python
df[df.columns[3]] = df.iloc[:, 3].dt.round('us')
```

### Step 6: Assign unknown = unknown.astype(...)

```python
df0['Date1'] = df0['Date1'].astype('M8[s]')
```

### Step 7: Assign unknown = unknown.astype(...)

```python
df0['Date2'] = df0['Date2'].astype('M8[s]')
```

### Step 8: Assign unknown = unknown.astype(...)

```python
df0['DateTime'] = df0['DateTime'].astype('M8[ms]')
```

### Step 9: Assign unknown = unknown.astype(...)

```python
df0['Taiw'] = df0['Taiw'].astype('M8[s]')
```

### Step 10: Assign res = unknown.astype.dt.round(...)

```python
res = df0['DateTimeHi'].astype('M8[us]').dt.round('ms')
```

### Step 11: Assign unknown = res.astype(...)

```python
df0['DateTimeHi'] = res.astype('M8[ms]')
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df0)
```


## Complete Example

```python
# Setup
# Fixtures: datapath

# Workflow
fname = datapath('io', 'sas', 'data', 'datetime.sas7bdat')
df = pd.read_sas(fname)
fname = datapath('io', 'sas', 'data', 'datetime.csv')
df0 = pd.read_csv(fname, parse_dates=['Date1', 'Date2', 'DateTime', 'DateTimeHi', 'Taiw'])
df[df.columns[3]] = df.iloc[:, 3].dt.round('us')
df0['Date1'] = df0['Date1'].astype('M8[s]')
df0['Date2'] = df0['Date2'].astype('M8[s]')
df0['DateTime'] = df0['DateTime'].astype('M8[ms]')
df0['Taiw'] = df0['Taiw'].astype('M8[s]')
res = df0['DateTimeHi'].astype('M8[us]').dt.round('ms')
df0['DateTimeHi'] = res.astype('M8[ms]')
if not IS64:
    df0.loc[0, 'DateTimeHi'] += np.timedelta64(1, 'ms')
    df0.loc[[2, 3], 'DateTimeHi'] -= np.timedelta64(1, 'ms')
tm.assert_frame_equal(df, df0)
```

## Next Steps


---

*Source: test_sas7bdat.py:183 | Complexity: Advanced | Last updated: 2026-06-02*