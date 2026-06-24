# How To: Hierarchical Columns

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test hierarchical columns

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

### Step 1: Assign expected = "<?xml version='1.0' encoding='utf-8'?>\n<data>\n  <row>\n    <location>inner</location>\n    <type>terrestrial</type>\n    <count_mass>4</count_mass>\n    <sum_mass>11.81</sum_mass>\n    <mean_mass>2.95</mean_mass>\n  </row>\n  <row>\n    <location>outer</location>\n    <type>gas giant</type>\n    <count_mass>2</count_mass>\n    <sum_mass>2466.5</sum_mass>\n    <mean_mass>1233.25</mean_mass>\n  </row>\n  <row>\n    <location>outer</location>\n    <type>ice giant</type>\n    <count_mass>2</count_mass>\n    <sum_mass>189.23</sum_mass>\n    <mean_mass>94.61</mean_mass>\n  </row>\n  <row>\n    <location>All</location>\n    <type/>\n    <count_mass>8</count_mass>\n    <sum_mass>2667.54</sum_mass>\n    <mean_mass>333.44</mean_mass>\n  </row>\n</data>"

```python
expected = "<?xml version='1.0' encoding='utf-8'?>\n<data>\n  <row>\n    <location>inner</location>\n    <type>terrestrial</type>\n    <count_mass>4</count_mass>\n    <sum_mass>11.81</sum_mass>\n    <mean_mass>2.95</mean_mass>\n  </row>\n  <row>\n    <location>outer</location>\n    <type>gas giant</type>\n    <count_mass>2</count_mass>\n    <sum_mass>2466.5</sum_mass>\n    <mean_mass>1233.25</mean_mass>\n  </row>\n  <row>\n    <location>outer</location>\n    <type>ice giant</type>\n    <count_mass>2</count_mass>\n    <sum_mass>189.23</sum_mass>\n    <mean_mass>94.61</mean_mass>\n  </row>\n  <row>\n    <location>All</location>\n    <type/>\n    <count_mass>8</count_mass>\n    <sum_mass>2667.54</sum_mass>\n    <mean_mass>333.44</mean_mass>\n  </row>\n</data>"
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
output = pvt.to_xml(parser=parser)
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
expected = "<?xml version='1.0' encoding='utf-8'?>\n<data>\n  <row>\n    <location>inner</location>\n    <type>terrestrial</type>\n    <count_mass>4</count_mass>\n    <sum_mass>11.81</sum_mass>\n    <mean_mass>2.95</mean_mass>\n  </row>\n  <row>\n    <location>outer</location>\n    <type>gas giant</type>\n    <count_mass>2</count_mass>\n    <sum_mass>2466.5</sum_mass>\n    <mean_mass>1233.25</mean_mass>\n  </row>\n  <row>\n    <location>outer</location>\n    <type>ice giant</type>\n    <count_mass>2</count_mass>\n    <sum_mass>189.23</sum_mass>\n    <mean_mass>94.61</mean_mass>\n  </row>\n  <row>\n    <location>All</location>\n    <type/>\n    <count_mass>8</count_mass>\n    <sum_mass>2667.54</sum_mass>\n    <mean_mass>333.44</mean_mass>\n  </row>\n</data>"
pvt = planet_df.pivot_table(index=['location', 'type'], values='mass', aggfunc=['count', 'sum', 'mean'], margins=True).round(2)
output = pvt.to_xml(parser=parser)
output = equalize_decl(output)
assert output == expected
```

## Next Steps


---

*Source: test_to_xml.py:535 | Complexity: Intermediate | Last updated: 2026-06-02*