"""Unit tests for validate-lesson.py check functions."""
import sys, os, importlib.util
spec = importlib.util.spec_from_file_location("vl", os.path.join(os.path.dirname(__file__), "validate-lesson.py"))
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)

PASS = 0
FAIL = 0

def test(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"  [PASS] {name}")
    else:
        FAIL += 1
        print(f"  [FAIL] {name} -- {detail}")

# ==== check_h1_count ====
test("h1: exactly one passes", not v.check_h1_count("<html><h1>Title</h1></html>"))
test("h1: zero fails", len(v.check_h1_count("<html></html>")) > 0)
test("h1: two fails", len(v.check_h1_count("<html><h1>A</h1><h1>B</h1></html>")) > 0)

# ==== check_relative_links ====
test("rel links: relative passes", not v.check_relative_links('<a href="0021-slug.html">link</a>'))
test("rel links: absolute / fails", len(v.check_relative_links('<a href="/lessons/x.html">link</a>')) > 0)
test("rel links: absolute http fails", len(v.check_relative_links('<a href="https://example.com/x.html">link</a>')) > 0)

# ==== check_quiz_correct_count ====
test("quiz: single correct passes", not v.check_quiz_correct_count(
    '<div class="quiz-question"><button data-correct="true">A</button><button data-correct="false">B</button></div>'))
test("quiz: zero correct fails", len(v.check_quiz_correct_count(
    '<div class="quiz-question"><button data-correct="false">A</button></div>')) > 0)
test("quiz: two correct fails", len(v.check_quiz_correct_count(
    '<div class="quiz-question"><button data-correct="true">A</button><button data-correct="true">B</button></div>')) > 0)

# ==== check_quiz_completeness ====
test("quiz comp: 5 questions passes", not v.check_quiz_completeness(
    '<div class="quiz-question"><button class="quiz-option">A</button><button class="quiz-option">B</button><button class="quiz-option">C</button></div>' * 5))
test("quiz comp: 3 questions fails", len(v.check_quiz_completeness(
    '<div class="quiz-question"></div>' * 3)) > 0)
test("quiz comp: wrong options count fails", len(v.check_quiz_completeness(
    '<div class="quiz-question"><button class="quiz-option">A</button><button class="quiz-option">B</button></div>' * 5)) > 0)

# ==== check_data_anim_syntax ====
test("anim: valid values pass", not v.check_data_anim_syntax('<div data-anim="fade-up"></div>'))
test("anim: invalid value fails", len(v.check_data_anim_syntax('<div data-anim="zoom-in"></div>')) > 0)

# ==== check_ppt_js ====
test("ppt: theme+nav present passes", not v.check_ppt_js(
    '<html data-theme="warm"><h2>A</h2><h2>B</h2>'
    'key==="t" key==="ArrowRight" tp-btn-toggle tp-item</html>'))
test("ppt: missing T key fails", len(v.check_ppt_js(
    '<html data-theme="warm">tp-item</html>')) > 0)

# ==== check_inline_svg ====
test("inline svg: with wrapper passes", not v.check_inline_svg(
    '<figure class="svg-fig"><svg xmlns="..."></svg></figure>'))
test("inline svg: no wrapper fails", len(v.check_inline_svg('<svg xmlns="..."></svg>')) > 0)
test("inline svg: icon svg passes", not v.check_inline_svg(
    '<button><svg width="16" height="16" viewBox="0 0 20 20"></svg></button>'))
test("inline svg: pie chart in figure passes", not v.check_inline_svg(
    '<figure class="svg-fig"><svg viewBox="0 0 100 100" width="240"></svg></figure>'))
test("inline svg: pie chart no figure fails", len(v.check_inline_svg(
    '<svg viewBox="0 0 100 100" width="240"></svg>')) > 0)

# ==== check_component_consistency ====
test("lbox: trigger+target passes", not v.check_component_consistency(
    '<span data-lbox="chart-1"></span><div id="lbox-chart-1"></div>'))
test("lbox: trigger no target fails", len(v.check_component_consistency(
    '<span data-lbox="chart-1"></span>')) > 0)
test("panel: trigger+target passes", not v.check_component_consistency(
    '<span data-panel="glossary"></span><div id="panel-glossary"></div>'))
test("panel: trigger no target fails", len(v.check_component_consistency(
    '<span data-panel="glossary"></span>')) > 0)

# ==== Results ====
print(f"\n{PASS} passed, {FAIL} failed")
if FAIL > 0:
    sys.exit(1)
