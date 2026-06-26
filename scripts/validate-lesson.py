"""Validate a lesson HTML file against teach_more_pic's error checklist.
Usage: python validate-lesson.py <path-to-lesson.html>
"""

import re
import sys
import os
import xml.etree.ElementTree as ET

PASS = "[PASS]"
FAIL = "[FAIL]"


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
                ET.parse(path)
            except Exception as e:
                issues.append(f"SVG invalid XML: {src} -- {e}")
    return issues


def check_quiz_correct_count(html):
    """Each quiz question should have exactly one data-correct=true."""
    issues = []
    questions = re.findall(
        r'<div[^>]*class="[^"]*quiz-question[^"]*"[^>]*>.*?</div>', html, re.DOTALL
    )
    for i, q in enumerate(questions, 1):
        corrects = re.findall(r'data-correct="true"', q)
        if len(corrects) != 1:
            issues.append(f"Quiz Q{i}: {len(corrects)} correct answers (expected 1)")
    return issues


def check_h1_count(html):
    """Each lesson must have exactly one h1."""
    h1s = re.findall(r"<h1[^>]*>", html)
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
    m = re.search(r"\.container\s*\{[^}]*max-width:\s*(\d+)", html)
    if m:
        w = int(m.group(1))
        if w < 700 or w > 800:
            return [f"Container max-width is {w}px (recommended 720-780)"]
    return []


def check_relative_links(html):
    """Cross-lesson links must use relative paths, not / or http."""
    issues = []
    links = re.findall(r'<a[^>]*href="([^"]+\.html)"', html)
    for href in links:
        if href.startswith("/") or href.startswith("http"):
            issues.append(f"Absolute link found: {href} (use relative path)")
    return issues


def check_quiz_completeness(html):
    """Should have exactly 5 questions, each with 3 options."""
    issues = []
    questions = re.findall(
        r'<div[^>]*class="[^"]*quiz-question[^"]*"[^>]*>.*?</div>', html, re.DOTALL
    )
    if len(questions) != 5:
        issues.append(f"Found {len(questions)} quiz questions (expected 5)")
    for i, q in enumerate(questions, 1):
        options = re.findall(r'<button[^>]*class="[^"]*quiz-option[^"]*"', q)
        if len(options) != 3:
            issues.append(f"Quiz Q{i}: {len(options)} options (expected 3)")
    return issues


_LIGHT_FILLS = re.compile(
    r'fill="(?:#)?(?:fef2f2|f0fdf4|eff6ff|fff7ed|ffffff|f8fafc)"', re.IGNORECASE
)
_WHITE_TEXT = re.compile(r'fill="(?:#)?(?:fff{1,3})"', re.IGNORECASE)


def check_svg_contrast(html, base_dir):
    """Flag SVGs that may have white text on light backgrounds."""
    issues = []
    svgs = re.findall(r'<img[^>]*src="([^"]+\.svg)"', html)
    for src in svgs:
        path = os.path.join(base_dir, src)
        if not os.path.exists(path):
            continue
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            has_light_fill = bool(_LIGHT_FILLS.search(content))
            has_white_text = bool(_WHITE_TEXT.search(content))
            if has_light_fill and has_white_text:
                issues.append(
                    f"{src}: possible white text on light background -- verify manually"
                )
        except Exception:
            pass
    return issues


def check_ppt_js(html):
    """Check for theme switching (T key) and keyboard nav (arrow keys) JS."""
    issues = []
    # Only flag missing if the class patterns suggest the feature is expected
    has_themes = bool(re.search(r"data-theme", html))
    if has_themes and not re.search(
        r"key\s*===?\s*['\"]t['\"]", html, re.IGNORECASE
    ):
        issues.append("Missing theme switching JS (T key handler)")

    has_sections = len(re.findall(r"<h2[^>]*>", html)) > 1
    if has_sections and not re.search(
        r"key\s*===?\s*['\"]Arrow(?:Right|Left)['\"]", html, re.IGNORECASE
    ):
        issues.append("Missing keyboard navigation JS (arrow key handler)")
    return issues


def run_all(path):
    if not os.path.exists(path):
        print(f"{FAIL} File not found: {path}")
        sys.exit(1)

    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    base_dir = os.path.dirname(path)

    results = [
        ("SVG files exist & valid", check_svg_links(html, base_dir)),
        ("Quiz: exactly 1 correct per question", check_quiz_correct_count(html)),
        ("Quiz: 5 questions x 3 options", check_quiz_completeness(html)),
        ("Exactly one <h1>", check_h1_count(html)),
        ("data-anim syntax valid", check_data_anim_syntax(html)),
        ("Container width in range", check_container_width(html)),
        ("Relative links only", check_relative_links(html)),
        ("SVG text/background contrast", check_svg_contrast(html, base_dir)),
        ("PPT JS (theme + nav) present", check_ppt_js(html)),
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
