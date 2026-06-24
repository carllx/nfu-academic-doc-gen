# How To: Spss Metadata

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test spss metadata

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `pathlib`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.util.version`
- `pandas.arrays`

**Setup Required:**
```python
# Fixtures: datapath
```

## Step-by-Step Guide

### Step 1: Assign fname = datapath(...)

```python
fname = datapath('io', 'data', 'spss', 'labelled-num.sav')
```

### Step 2: Assign df = pd.read_spss(...)

```python
df = pd.read_spss(fname)
```

### Step 3: Assign metadata = value

```python
metadata = {'column_names': ['VAR00002'], 'column_labels': [None], 'column_names_to_labels': {'VAR00002': None}, 'file_encoding': 'UTF-8', 'number_columns': 1, 'number_rows': 1, 'variable_value_labels': {'VAR00002': {1.0: 'This is one'}}, 'value_labels': {'labels0': {1.0: 'This is one'}}, 'variable_to_label': {'VAR00002': 'labels0'}, 'notes': [], 'original_variable_types': {'VAR00002': 'F8.0'}, 'readstat_variable_types': {'VAR00002': 'double'}, 'table_name': None, 'missing_ranges': {}, 'missing_user_values': {}, 'variable_storage_width': {'VAR00002': 8}, 'variable_display_width': {'VAR00002': 8}, 'variable_alignment': {'VAR00002': 'unknown'}, 'variable_measure': {'VAR00002': 'unknown'}, 'file_label': None, 'file_format': 'sav/zsav'}
```

### Step 4: Call tm.assert_dict_equal()

```python
tm.assert_dict_equal(df.attrs, metadata)
```

### Step 5: Call metadata.update()

```python
metadata.update({'creation_time': datetime.datetime(2015, 2, 6, 14, 33, 36), 'modification_time': datetime.datetime(2015, 2, 6, 14, 33, 36)})
```

### Step 6: Assign unknown = value

```python
metadata['mr_sets'] = {}
```


## Complete Example

```python
# Setup
# Fixtures: datapath

# Workflow
fname = datapath('io', 'data', 'spss', 'labelled-num.sav')
df = pd.read_spss(fname)
metadata = {'column_names': ['VAR00002'], 'column_labels': [None], 'column_names_to_labels': {'VAR00002': None}, 'file_encoding': 'UTF-8', 'number_columns': 1, 'number_rows': 1, 'variable_value_labels': {'VAR00002': {1.0: 'This is one'}}, 'value_labels': {'labels0': {1.0: 'This is one'}}, 'variable_to_label': {'VAR00002': 'labels0'}, 'notes': [], 'original_variable_types': {'VAR00002': 'F8.0'}, 'readstat_variable_types': {'VAR00002': 'double'}, 'table_name': None, 'missing_ranges': {}, 'missing_user_values': {}, 'variable_storage_width': {'VAR00002': 8}, 'variable_display_width': {'VAR00002': 8}, 'variable_alignment': {'VAR00002': 'unknown'}, 'variable_measure': {'VAR00002': 'unknown'}, 'file_label': None, 'file_format': 'sav/zsav'}
if Version(pyreadstat.__version__) >= Version('1.2.4'):
    metadata.update({'creation_time': datetime.datetime(2015, 2, 6, 14, 33, 36), 'modification_time': datetime.datetime(2015, 2, 6, 14, 33, 36)})
if Version(pyreadstat.__version__) >= Version('1.2.8'):
    metadata['mr_sets'] = {}
tm.assert_dict_equal(df.attrs, metadata)
```

## Next Steps


---

*Source: test_spss.py:129 | Complexity: Intermediate | Last updated: 2026-06-02*