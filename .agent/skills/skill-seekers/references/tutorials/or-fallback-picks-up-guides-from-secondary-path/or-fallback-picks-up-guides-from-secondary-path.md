# How To: Or Fallback Picks Up Guides From Secondary Path

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Issue #364: when references/tutorials/ is missing but the original
tutorials/ still has the JSON, the fallback path must win.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `json`
- `pathlib`
- `unittest.mock`
- `skill_seekers.cli.unified_scraper`
- `argparse`
- `argparse`
- `contextlib`
- `skill_seekers.cli.unified_scraper`
- `skill_seekers.cli.workflow_runner`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: 'Issue #364: when references/tutorials/ is missing but the original\n        tutorials/ still has the JSON, the fallback path must win.'

```python
'Issue #364: when references/tutorials/ is missing but the original\n        tutorials/ still has the JSON, the fallback path must win.'
```

**Verification:**
```python
assert not primary
```

### Step 2: Assign temp_output = value

```python
temp_output = tmp_path / 'local_analysis_0_repo'
```

**Verification:**
```python
assert result['total_guides'] == 3
```

### Step 3: Assign refs = value

```python
refs = temp_output / 'references'
```

**Verification:**
```python
assert len(result['guides']) == 3
```

### Step 4: Assign tutorials = value

```python
tutorials = temp_output / 'tutorials'
```

### Step 5: Call tutorials.mkdir()

```python
tutorials.mkdir(parents=True)
```

### Step 6: Assign payload = value

```python
payload = {'total_guides': 3, 'guides_by_complexity': {}, 'guides_by_use_case': {}, 'guides': [{'id': 'g1', 'title': 'One'}, {'id': 'g2', 'title': 'Two'}, {'id': 'g3', 'title': 'Three'}]}
```

### Step 7: Call unknown.write_text()

```python
(tutorials / 'guide_collection.json').write_text(json.dumps(payload))
```

### Step 8: Assign scraper = self._scraper(...)

```python
scraper = self._scraper()
```

### Step 9: Assign primary = scraper._load_guide_collection(...)

```python
primary = scraper._load_guide_collection(refs / 'tutorials')
```

### Step 10: Assign fallback = scraper._load_guide_collection(...)

```python
fallback = scraper._load_guide_collection(temp_output / 'tutorials')
```

### Step 11: Assign result = value

```python
result = primary or fallback
```

**Verification:**
```python
assert not primary
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
'Issue #364: when references/tutorials/ is missing but the original\n        tutorials/ still has the JSON, the fallback path must win.'
temp_output = tmp_path / 'local_analysis_0_repo'
refs = temp_output / 'references'
tutorials = temp_output / 'tutorials'
tutorials.mkdir(parents=True)
payload = {'total_guides': 3, 'guides_by_complexity': {}, 'guides_by_use_case': {}, 'guides': [{'id': 'g1', 'title': 'One'}, {'id': 'g2', 'title': 'Two'}, {'id': 'g3', 'title': 'Three'}]}
(tutorials / 'guide_collection.json').write_text(json.dumps(payload))
scraper = self._scraper()
primary = scraper._load_guide_collection(refs / 'tutorials')
fallback = scraper._load_guide_collection(temp_output / 'tutorials')
result = primary or fallback
assert not primary
assert result['total_guides'] == 3
assert len(result['guides']) == 3
```

## Next Steps


---

*Source: test_unified_scraper_orchestration.py:647 | Complexity: Advanced | Last updated: 2026-06-02*