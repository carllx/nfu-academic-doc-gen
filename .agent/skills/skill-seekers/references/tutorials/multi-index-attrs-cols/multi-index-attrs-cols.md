# How To: Multi Index Attrs Cols

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multi index attrs cols

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

### Step 1: Assign expected = '<?xml version=\'1.0\' encoding=\'utf-8\'?>\n<data>\n  <row location="inner" type="terrestrial" count="4" sum="11.81" mean="2.95"/>\n  <row location="outer" type="gas giant" count="2" sum="2466.5" mean="1233.25"/>\n  <row location="outer" type="ice giant" count="2" sum="189.23" mean="94.61"/>\n</data>'

```python
expected = '<?xml version=\'1.0\' encoding=\'utf-8\'?>\n<data>\n  <row location="inner" type="terrestrial" count="4" sum="11.81" mean="2.95"/>\n  <row location="outer" type="gas giant" count="2" sum="2466.5" mean="1233.25"/>\n  <row location="outer" type="ice giant" count="2" sum="189.23" mean="94.61"/>\n</data>'
```

**Verification:**
```python
assert output == expected
```

### Step 2: Assign agg = unknown.agg.round(...)

```python
agg = planet_df.groupby(['location', 'type'])['mass'].agg(['count', 'sum', 'mean']).round(2)
```

### Step 3: Assign output = agg.to_xml(...)

```python
output = agg.to_xml(attr_cols=list(agg.reset_index().columns.values), parser=parser)
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
expected = '<?xml version=\'1.0\' encoding=\'utf-8\'?>\n<data>\n  <row location="inner" type="terrestrial" count="4" sum="11.81" mean="2.95"/>\n  <row location="outer" type="gas giant" count="2" sum="2466.5" mean="1233.25"/>\n  <row location="outer" type="ice giant" count="2" sum="189.23" mean="94.61"/>\n</data>'
agg = planet_df.groupby(['location', 'type'])['mass'].agg(['count', 'sum', 'mean']).round(2)
output = agg.to_xml(attr_cols=list(agg.reset_index().columns.values), parser=parser)
output = equalize_decl(output)
assert output == expected
```

## Next Steps


---

*Source: test_to_xml.py:651 | Complexity: Intermediate | Last updated: 2026-06-02*