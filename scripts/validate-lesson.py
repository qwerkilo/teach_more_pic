"""Validate a lesson HTML file against teach_more_pic's error checklist.
Usage: python validate-lesson.py <path-to-lesson.html>
"""

import re
import sys
import os

PASS = "✓"
FAIL = "✗"

def check_svg_links(html, base_dir):
    """Check that all SVG src files exist and are valid XML."""
    issues = []
    svgs = re.findall(r'<img[^>]*src="([^"]+\.svg)"', html)
    for src in svgs:
        path = os.path.join(base_dir, src)
        if not os.path.exists(path):
            issues.append(f"SVG not found: {src}")
        else:
            try:
                import xml.etree.ElementTree as ET
                ET.parse(path)
            except Exception as e:
                issues.append(f"SVG invalid XML: {src} — {e}")
    return issues

def check_quiz_correct_count(html):
    """Each quiz question should have exactly one data-correct=true."""
    issues = []
    questions = re.findall(r'<div[^>]*class="[^"]*quiz-question[^"]*"[^>]*>.*?</div>', html, re.DOTALL)
    for i, q in enumerate(questions, 1):
        corrects = re.findall(r'data-correct="true"', q)
        if len(corrects) != 1:
            issues.append(f"Quiz Q{i}: {len(corrects)} correct answers (expected 1)")
    return issues

def check_h1_count(html):
    """Each lesson must have exactly one h1."""
    h1s = re.findall(r'<h1[^>]*>', html)
    if len(h1s) != 1:
        return [f"Found {len(h1s)} h1 tags (expected 1)"]
    return []

def check_data_anim_syntax(html):
    """data-anim values should be valid."""
    valid = {"fade-up", "fade", "slide-left"}
    anims = re.findall(r'data-anim="([^"]+)"', html)
    bad = [a for a in anims if a not in valid]
    if bad:
        return [f"Invalid data-anim values: {set(bad)}"]
    return []

def check_container_width(html):
    """Container max-width should be between 700-800px."""
    m = re.search(r'\.container\s*\{[^}]*max-width:\s*(\d+)', html)
    if m:
        w = int(m.group(1))
        if w < 700 or w > 800:
            return [f"Container max-width is {w}px (recommended 720-780)"]
    return []

def run_all(path):
    if not os.path.exists(path):
        print(f"{FAIL} File not found: {path}")
        sys.exit(1)

    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    base_dir = os.path.dirname(path)
    all_issues = []
    all_issues.extend((PASS, "check") for check in [True])  # dummy

    results = [
        ("SVG files exist & valid", check_svg_links(html, base_dir)),
        ("Quiz: exactly 1 correct per question", check_quiz_correct_count(html)),
        ("Exactly one <h1>", check_h1_count(html)),
        ("data-anim syntax valid", check_data_anim_syntax(html)),
        ("Container width in range", check_container_width(html)),
    ]

    all_pass = True
    for label, issues in results:
        if issues:
            all_pass = False
            print(f"  {FAIL} {label}")
            for i in issues:
                print(f"      {i}")
        else:
            print(f"  {PASS} {label}")

    print()
    if all_pass:
        print(f" {PASS} All checks passed for {os.path.basename(path)}")
    else:
        print(f" {FAIL} Some checks failed")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <lesson.html>")
        sys.exit(1)
    run_all(sys.argv[1])
