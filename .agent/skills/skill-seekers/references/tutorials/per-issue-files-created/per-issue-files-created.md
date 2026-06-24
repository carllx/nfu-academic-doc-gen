# How To: Per Issue Files Created

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: Per-issue files live in references/issues/ with {owner}-{repo}-{n}.md naming.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `json`
- `os`
- `shutil`
- `tempfile`
- `unittest`
- `datetime`
- `pathlib`
- `unittest.mock`
- `github`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`

**Setup Required:**
```python
if not PYGITHUB_AVAILABLE:
    self.skipTest('PyGithub not installed')
from skill_seekers.cli.github_scraper import GitHubToSkillConverter
self.GitHubToSkillConverter = GitHubToSkillConverter
self.temp_dir = tempfile.mkdtemp()
```

## Step-by-Step Guide

### Step 1: 'Per-issue files live in references/issues/ with {owner}-{repo}-{n}.md naming.'

```python
'Per-issue files live in references/issues/ with {owner}-{repo}-{n}.md naming.'
```

### Step 2: Assign issues = value

```python
issues = [{'number': 42, 'title': 'Bug report', 'state': 'open', 'labels': ['bug'], 'created_at': '2023-01-01T00:00:00', 'updated_at': '2023-01-02T00:00:00', 'closed_at': None, 'url': 'https://github.com/test/test-repo/issues/42', 'body': 'Full bug description here', 'comments': []}]
```

### Step 3: Assign converter = self._setup_converter(...)

```python
converter = self._setup_converter(issues)
```

### Step 4: Call converter._generate_issues_reference()

```python
converter._generate_issues_reference()
```

### Step 5: Assign expected_file = os.path.join(...)

```python
expected_file = os.path.join(converter.skill_dir, 'references', 'issues', 'test-test-repo-42.md')
```

### Step 6: Call self.assertTrue()

```python
self.assertTrue(os.path.exists(expected_file))
```

### Step 7: Assign old_file = os.path.join(...)

```python
old_file = os.path.join(converter.skill_dir, 'references', 'test-repo_42.md')
```

### Step 8: Call self.assertFalse()

```python
self.assertFalse(os.path.exists(old_file))
```


## Complete Example

```python
# Setup
if not PYGITHUB_AVAILABLE:
    self.skipTest('PyGithub not installed')
from skill_seekers.cli.github_scraper import GitHubToSkillConverter
self.GitHubToSkillConverter = GitHubToSkillConverter
self.temp_dir = tempfile.mkdtemp()

# Workflow
'Per-issue files live in references/issues/ with {owner}-{repo}-{n}.md naming.'
issues = [{'number': 42, 'title': 'Bug report', 'state': 'open', 'labels': ['bug'], 'created_at': '2023-01-01T00:00:00', 'updated_at': '2023-01-02T00:00:00', 'closed_at': None, 'url': 'https://github.com/test/test-repo/issues/42', 'body': 'Full bug description here', 'comments': []}]
converter = self._setup_converter(issues)
converter._generate_issues_reference()
expected_file = os.path.join(converter.skill_dir, 'references', 'issues', 'test-test-repo-42.md')
self.assertTrue(os.path.exists(expected_file))
old_file = os.path.join(converter.skill_dir, 'references', 'test-repo_42.md')
self.assertFalse(os.path.exists(old_file))
```

## Next Steps


---

*Source: test_github_scraper.py:1370 | Complexity: Advanced | Last updated: 2026-06-02*