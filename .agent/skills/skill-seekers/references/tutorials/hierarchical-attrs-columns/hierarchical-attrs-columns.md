# How To: Hierarchical Attrs Columns

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test hierarchical attrs columns

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `io`
- `os`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.io.common`
- `pandas.io.xml`

**Setup Required:**
```python
# Fixtures: parser, planet_df
```

## Step-by-Step Guide

### Step 1: Assign expected = '<?xml version=\'1.0\' encoding=\'utf-8\'?>\n<data>\n  <row location="inner" type="terrestrial" count_mass="4" sum_mass="11.81" mean_mass="2.95"/>\n  <row location="outer" type="gas giant" count_mass="2" sum_mass="2466.5" mean_mass="1233.25"/>\n  <row location="outer" type="ice giant" count_mass="2" sum_mass="189.23" mean_mass="94.61"/>\n  <row location="All" type="" count_mass="8" sum_mass="2667.54" mean_mass="333.44"/>\n</data>'

```python
expected = '<?xml version=\'1.0\' encoding=\'utf-8\'?>\n<data>\n  <row location="inner" type="terrestrial" count_mass="4" sum_mass="11.81" mean_mass="2.95"/>\n  <row location="outer" type="gas giant" count_mass="2" sum_mass="2466.5" mean_mass="1233.25"/>\n  <row location="outer" type="ice giant" count_mass="2" sum_mass="189.23" mean_mass="94.61"/>\n  <row location="All" type="" count_mass="8" sum_mass="2667.54" mean_mass="333.44"/>\n</data>'
```

**Verification:**
```python
assert output == expected
```

### Step 2: Assign pvt = planet_df.pivot_table.round(...)

```python
pvt = planet_df.pivot_table(index=['location', 'type'], values='mass', aggfunc=['count', 'sum', 'mean'], margins=True).round(2)
```

### Step 3: Assign output = pvt.to_xml(...)

```python
output = pvt.to_xml(attr_cols=list(pvt.reset_index().columns.values), parser=parser)
```

### Step 4: Assign output = equalize_decl(...)

```python
output = equalize_decl(output)
```

**Verification:**
```python
assert output == expected
```


## Complete Example

```python
# Setup
# Fixtures: parser, planet_df

# Workflow
expected = '<?xml version=\'1.0\' encoding=\'utf-8\'?>\n<data>\n  <row location="inner" type="terrestrial" count_mass="4" sum_mass="11.81" mean_mass="2.95"/>\n  <row location="outer" type="gas giant" count_mass="2" sum_mass="2466.5" mean_mass="1233.25"/>\n  <row location="outer" type="ice giant" count_mass="2" sum_mass="189.23" mean_mass="94.61"/>\n  <row location="All" type="" count_mass="8" sum_mass="2667.54" mean_mass="333.44"/>\n</data>'
pvt = planet_df.pivot_table(index=['location', 'type'], values='mass', aggfunc=['count', 'sum', 'mean'], margins=True).round(2)
output = pvt.to_xml(attr_cols=list(pvt.reset_index().columns.values), parser=parser)
output = equalize_decl(output)
assert output == expected
```

## Next Steps


---

*Source: test_to_xml.py:582 | Complexity: Intermediate | Last updated: 2026-06-02*