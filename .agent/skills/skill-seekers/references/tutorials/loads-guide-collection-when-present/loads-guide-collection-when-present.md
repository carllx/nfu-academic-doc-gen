# How To: Loads Guide Collection When Present

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loads guide collection when present

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

### Step 1: Assign tutorials = value

```python
tutorials = tmp_path / 'tutorials'
```

**Verification:**
```python
assert result['total_guides'] == 2
```

### Step 2: Call tutorials.mkdir()

```python
tutorials.mkdir()
```

**Verification:**
```python
assert len(result['guides']) == 2
```

### Step 3: Assign payload = value

```python
payload = {'total_guides': 2, 'guides_by_complexity': {}, 'guides_by_use_case': {}, 'guides': [{'id': 'g1', 'title': 'One'}, {'id': 'g2', 'title': 'Two'}]}
```

### Step 4: Call unknown.write_text()

```python
(tutorials / 'guide_collection.json').write_text(json.dumps(payload))
```

### Step 5: Assign scraper = self._scraper(...)

```python
scraper = self._scraper()
```

### Step 6: Assign result = scraper._load_guide_collection(...)

```python
result = scraper._load_guide_collection(tutorials)
```

**Verification:**
```python
assert result['total_guides'] == 2
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
tutorials = tmp_path / 'tutorials'
tutorials.mkdir()
payload = {'total_guides': 2, 'guides_by_complexity': {}, 'guides_by_use_case': {}, 'guides': [{'id': 'g1', 'title': 'One'}, {'id': 'g2', 'title': 'Two'}]}
(tutorials / 'guide_collection.json').write_text(json.dumps(payload))
scraper = self._scraper()
result = scraper._load_guide_collection(tutorials)
assert result['total_guides'] == 2
assert len(result['guides']) == 2
```

## Next Steps


---

*Source: test_unified_scraper_orchestration.py:632 | Complexity: Intermediate | Last updated: 2026-06-02*