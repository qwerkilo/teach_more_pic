"""pytest unit tests for validate-lesson.py check functions."""
import sys, os, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import importlib.util
spec = importlib.util.spec_from_file_location("vl", os.path.join(os.path.dirname(__file__), "..", "scripts", "validate-lesson.py"))
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)

def check_passes(fn, *args):
    result = fn(*args)
    return len(result) == 0

def check_fails(fn, *args):
    result = fn(*args)
    return len(result) > 0

# ==== check_h1_count ====
def test_h1_exactly_one_passes(): assert check_passes(v.check_h1_count, "<html><h1>Title</h1></html>")
def test_h1_zero_fails(): assert check_fails(v.check_h1_count, "<html></html>")
def test_h1_two_fails(): assert check_fails(v.check_h1_count, "<html><h1>A</h1><h1>B</h1></html>")

# ==== check_relative_links ====
def test_rel_relative_passes(): assert check_passes(v.check_relative_links, '<a href="0021-slug.html">link</a>')
def test_rel_absolute_slash_fails(): assert check_fails(v.check_relative_links, '<a href="/lessons/x.html">link</a>')
def test_rel_absolute_http_fails(): assert check_fails(v.check_relative_links, '<a href="https://example.com/x.html">link</a>')

# ==== check_quiz_correct_count ====
def test_quiz_single_correct_passes(): assert check_passes(v.check_quiz_correct_count, '<div class="quiz-question"><button data-correct="true">A</button><button data-correct="false">B</button></div>')
def test_quiz_zero_correct_fails(): assert check_fails(v.check_quiz_correct_count, '<div class="quiz-question"><button data-correct="false">A</button></div>')
def test_quiz_two_correct_fails(): assert check_fails(v.check_quiz_correct_count, '<div class="quiz-question"><button data-correct="true">A</button><button data-correct="true">B</button></div>')

# ==== check_quiz_completeness ====
def test_quiz_5_questions_passes(): assert check_passes(v.check_quiz_completeness, '<div class="quiz-question"><button class="quiz-option">A</button><button class="quiz-option">B</button><button class="quiz-option">C</button></div>' * 5)
def test_quiz_3_questions_fails(): assert check_fails(v.check_quiz_completeness, '<div class="quiz-question"></div>' * 3)
def test_quiz_wrong_options_fails(): assert check_fails(v.check_quiz_completeness, '<div class="quiz-question"><button class="quiz-option">A</button><button class="quiz-option">B</button></div>' * 5)

# ==== check_data_anim_syntax ====
def test_anim_valid_pass(): assert check_passes(v.check_data_anim_syntax, '<div data-anim="fade-up"></div>')
def test_anim_invalid_fail(): assert check_fails(v.check_data_anim_syntax, '<div data-anim="zoom-in"></div>')

# ==== check_ppt_js ====
def test_ppt_theme_nav_passes(): assert check_passes(v.check_ppt_js, '<html data-theme="warm"><h2>A</h2><h2>B</h2>key==="t" key==="ArrowRight" tp-btn-toggle tp-item</html>')
def test_ppt_missing_T_fails(): assert check_fails(v.check_ppt_js, '<html data-theme="warm">tp-item</html>')

# ==== check_inline_svg ====
def test_inline_svg_with_wrapper_pass(): assert check_passes(v.check_inline_svg, '<figure class="svg-fig"><svg xmlns="..."></svg></figure>')
def test_inline_svg_no_wrapper_fail(): assert check_fails(v.check_inline_svg, '<svg xmlns="..."></svg>')
def test_inline_svg_icon_pass(): assert check_passes(v.check_inline_svg, '<button><svg width="16" height="16" viewBox="0 0 20 20"></svg></button>')
def test_inline_svg_24px_icon_pass(): assert check_passes(v.check_inline_svg, '<span><svg width="24" height="24" viewBox="0 0 24 24"></svg></span>')
def test_inline_svg_28px_icon_pass(): assert check_passes(v.check_inline_svg, '<span><svg width="28" height="28" viewBox="0 0 24 24"></svg></span>')
def test_inline_svg_pie_in_figure_pass(): assert check_passes(v.check_inline_svg, '<figure class="svg-fig"><svg viewBox="0 0 100 100" width="240"></svg></figure>')
def test_inline_svg_pie_no_figure_fail(): assert check_fails(v.check_inline_svg, '<svg viewBox="0 0 100 100" width="240"></svg>')
def test_inline_svg_mixed_figure_and_bare_fail():
    """B4: mixed case — one wrapped, one bare SVG — should flag the bare one."""
    html = '<figure class="svg-fig"><svg width="200"></svg></figure><p><svg width="300" viewBox="0 0 100 100"></svg></p>'
    assert check_fails(v.check_inline_svg, html)
def test_inline_svg_figure_no_svgfig_fail():
    """B4: <figure> without .svg-fig class should be flagged."""
    assert check_fails(v.check_inline_svg, '<figure><svg width="300"></svg></figure>')

# ==== check_component_consistency ====
def test_lbox_trigger_target_pass(): assert check_passes(v.check_component_consistency, '<span data-lbox="chart-1"></span><div id="lbox-chart-1"></div>')
def test_lbox_trigger_no_target_fail(): assert check_fails(v.check_component_consistency, '<span data-lbox="chart-1"></span>')
def test_panel_trigger_target_pass(): assert check_passes(v.check_component_consistency, '<span data-panel="glossary"></span><div id="panel-glossary"></div>')
def test_panel_trigger_no_target_fail(): assert check_fails(v.check_component_consistency, '<span data-panel="glossary"></span>')
def test_popover_trigger_target_pass(): assert check_passes(v.check_component_consistency, '<button popovertarget="pop-1"></button><div id="pop-1" popover></div>')
def test_popover_trigger_no_target_fail(): assert check_fails(v.check_component_consistency, '<button popovertarget="pop-1"></button>')
def test_popover_target_missing_popover_attr_fail():
    """B6: target exists but missing popover attribute — should flag."""
    assert check_fails(v.check_component_consistency, '<button popovertarget="pop-1"></button><div id="pop-1">not a popover</div>')
def test_dialog_with_close_pass(): assert check_passes(v.check_component_consistency, '<dialog><button onclick="this.closest(\'dialog\').close()">x</button></dialog>')
def test_dialog_no_close_fail(): assert check_fails(v.check_component_consistency, '<dialog></dialog>')

# ==== check_focus_visible ====
def test_focus_visible_present_pass(): assert check_passes(v.check_focus_visible, '<style>:focus-visible { outline: 2px solid red; }</style>')
def test_focus_visible_missing_fail(): assert check_fails(v.check_focus_visible, '<style>body { color: red; }</style>')

# ==== check_tabular_nums ====
def test_tabular_nums_present_pass(): assert check_passes(v.check_tabular_nums, '<style>body { font-variant-numeric: tabular-nums; }</style>')
def test_tabular_nums_missing_fail(): assert check_fails(v.check_tabular_nums, '<style>body { color: red; }</style>')

# ==== check_semantic_html ====
def test_semantic_article_pass(): assert check_passes(v.check_semantic_html, '<html><article></article></html>')
def test_semantic_section_pass(): assert check_passes(v.check_semantic_html, '<html><section></section></html>')
def test_semantic_nav_pass(): assert check_passes(v.check_semantic_html, '<html><nav></nav></html>')
def test_semantic_none_fail(): assert check_fails(v.check_semantic_html, '<html><div></div></html>')

# ==== check_spa_integration ====
def test_spa_with_section_pass():
    fd, tmp = tempfile.mkstemp(suffix=".html")
    os.close(fd)
    with open(tmp, "w") as f: f.write('<section class="lesson-view" id="lesson-42"><h1>Title</h1></section>')
    try: assert check_passes(v.check_spa_integration, '<section class="lesson-view" id="lesson-42"></section>', tmp)
    finally: os.unlink(tmp)

def test_spa_missing_id_fail():
    fd, tmp = tempfile.mkstemp(suffix=".html")
    os.close(fd)
    with open(tmp, "w") as f: f.write('<p>No lesson section here</p>')
    try: assert check_fails(v.check_spa_integration, '<p>No section</p>', tmp)
    finally: os.unlink(tmp)

def test_spa_index_with_sections_pass():
    assert check_passes(v.check_spa_integration, '<section class="lesson-view" id="lesson-1"></section><section class="lesson-view" id="lesson-2"></section>', "C:/fake/index.html")

def test_spa_index_missing_sections_fail():
    assert check_fails(v.check_spa_integration, '<p>hello</p>', "C:/fake/index.html")

def test_spa_index_duplicate_id_fail():
    assert check_fails(v.check_spa_integration, '<section class="lesson-view" id="lesson-1"></section><section class="lesson-view" id="lesson-1"></section>', "C:/fake/index.html")

def test_spa_kg_skips():
    assert check_passes(v.check_spa_integration, 'const graphData = {nodes:[]};', "C:/fake/kg-mine.html")

# ==== check_kg_structure ====
def test_kg_non_kg_skips(): assert check_passes(v.check_kg_structure, "<html><p>hello</p></html>", "")
def test_kg_minimal_valid_pass(): assert check_passes(v.check_kg_structure, 'const graphData = {"categories": ["课程"],"nodes": [{"id":"L1","name":"第一课","category":"课程","weight":80}],"links": [{"source":"L1","target":"L1","relation":"自指"}]};', "")
def test_kg_missing_categories_fail(): assert check_fails(v.check_kg_structure, 'const graphData = {"nodes": [{"id":"L1","name":"第一课","category":"课程","weight":80}],"links": [{"source":"L1","target":"L1","relation":"自指"}]};', "")
def test_kg_empty_nodes_fail(): assert check_fails(v.check_kg_structure, 'const graphData = {"categories": ["课程"],"nodes": [],"links": [{"source":"L1","target":"L1","relation":"自指"}]};', "")
def test_kg_missing_links_fail(): assert check_fails(v.check_kg_structure, 'const graphData = {"categories": ["课程"],"nodes": [{"id":"L1","name":"第一课","category":"课程","weight":80}]};', "")
def test_kg_node_missing_id_fail(): assert check_fails(v.check_kg_structure, 'const graphData = {"categories": ["课程"],"nodes": [{"name":"第一课","category":"课程","weight":80}],"links": [{"source":"","target":"","relation":"x"}]};', "")
def test_kg_node_missing_name_fail(): assert check_fails(v.check_kg_structure, 'const graphData = {"categories": ["课程"],"nodes": [{"id":"L1","category":"课程","weight":80}],"links": [{"source":"L1","target":"L1","relation":"x"}]};', "")
def test_kg_duplicate_node_id_fail(): assert check_fails(v.check_kg_structure, 'const graphData = {"categories": ["课程"],"nodes": [{"id":"L1","name":"A","category":"课程","weight":50},{"id":"L1","name":"B","category":"课程","weight":60}],"links": [{"source":"L1","target":"L1","relation":"x"}]};', "")
def test_kg_link_to_unknown_fail(): assert check_fails(v.check_kg_structure, 'const graphData = {"categories": ["课程"],"nodes": [{"id":"L1","name":"A","category":"课程","weight":50}],"links": [{"source":"L1","target":"NOEXIST","relation":"x"}]};', "")
def test_kg_invalid_category_fail(): assert check_fails(v.check_kg_structure, 'const graphData = {"categories": ["课程"],"nodes": [{"id":"L1","name":"A","category":"系统","weight":50}],"links": [{"source":"L1","target":"L1","relation":"x"}]};', "")
def test_kg_weight_over_100_fail(): assert check_fails(v.check_kg_structure, 'const graphData = {"categories": ["课程"],"nodes": [{"id":"L1","name":"A","category":"课程","weight":150}],"links": [{"source":"L1","target":"L1","relation":"x"}]};', "")
def test_kg_bilingual_format_pass(): assert check_passes(v.check_kg_structure, 'var rawNodes=[{"id":"L1","nameZh":"课","nameEn":"Lesson","category":"课程","weight":50}];var rawLinks=[{"source":"L1","target":"L1","relation":"x"}];var catNames={"zh":["课程"],"en":["Course"]};var graphData={};', "")
def test_kg_bilingual_missing_en_fail(): assert check_fails(v.check_kg_structure, 'var rawNodes=[{"id":"L1","nameZh":"课","category":"课程","weight":50}];var rawLinks=[{"source":"L1","target":"L1","relation":"x"}];var catNames={"zh":["课程"],"en":["Course"]};var graphData={};', "")
def test_kg_bilingual_missing_zh_fail(): assert check_fails(v.check_kg_structure, 'var rawNodes=[{"id":"L1","nameEn":"Lesson","category":"课程","weight":50}];var rawLinks=[{"source":"L1","target":"L1","relation":"x"}];var catNames={"zh":["课程"],"en":["Course"]};var graphData={};', "")

# ==== check_bilingual ====
def test_bilingual_no_lang_skip(): assert check_passes(v.check_bilingual, "<html><p>no lang attributes</p></html>")
def test_bilingual_full_pass(): assert check_passes(v.check_bilingual, '<html data-lang="zh"><span data-lang="zh">中</span><span data-lang="en">EN</span><button data-lang-btn></button>key==="l"</html>')
def test_bilingual_missing_en_fail(): assert check_fails(v.check_bilingual, '<html><span data-lang="zh">中</span><button data-lang-btn></button>key==="l"</html>')
def test_bilingual_missing_toggle_fail(): assert check_fails(v.check_bilingual, '<html><span data-lang="zh">中</span><span data-lang="en">EN</span>key==="l"</html>')
def test_bilingual_missing_l_key_fail(): assert check_fails(v.check_bilingual, '<html><span data-lang="zh">中</span><span data-lang="en">EN</span><button data-lang-btn></button></html>')
def test_bilingual_td_with_lang_pass(): assert check_passes(v.check_bilingual, '<html><td data-lang="zh">中</td><td data-lang="en">EN</td><button data-lang-btn></button>key==="l"</html>')
def test_bilingual_th_with_lang_pass(): assert check_passes(v.check_bilingual, '<html><th data-lang="zh">中</th><th data-lang="en">EN</th><button data-lang-btn></button>key==="l"</html>')

# ==== check_lib_deps ====
def test_lib_no_deps_pass(): assert check_passes(v.check_lib_deps, '<html><p>hello</p></html>', '.')
def test_lib_echarts_cdn_pass(): assert check_passes(v.check_lib_deps, '<html><script src="https://cdn.jsdelivr.net/npm/echarts@5/dist/echarts.min.js"></script>echarts.init()</html>', '.')
def test_lib_three_cdn_pass(): assert check_passes(v.check_lib_deps, '<html><script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>new THREE.Scene()</html>', '.')
def test_lib_echarts_local_pass(): assert check_passes(v.check_lib_deps, '<html>echarts.init()</html>', '.')
def test_lib_three_local_pass(): assert check_passes(v.check_lib_deps, '<html>new THREE.Scene()</html>', '.')
def test_lib_echarts_no_lib_fail(): assert check_fails(v.check_lib_deps, '<html>echarts.init()</html>', 'C:\\nonexistent')
def test_lib_three_no_lib_fail(): assert check_fails(v.check_lib_deps, '<html>new THREE.Scene()</html>', 'C:\\nonexistent')
def test_lib_d3_cdn_pass(): assert check_passes(v.check_lib_deps, '<html><script src="https://d3js.org/d3.v7.min.js"></script>d3.forceSimulation()</html>', '.')
def test_lib_d3_local_pass(): assert check_passes(v.check_lib_deps, '<html>d3.select("body")</html>', '.')
def test_lib_d3_no_lib_fail(): assert check_fails(v.check_lib_deps, '<html>d3.forceSimulation()</html>', 'C:\\nonexistent')
def test_lib_three_r185_importmap_pass(): assert check_passes(v.check_lib_deps, '<html>cdn.jsdelivr.net/npm/three@0.185.0/ new THREE.Scene()</html>', '.')
def test_lib_three_r185_importmap_as_cdn_pass(): assert check_passes(v.check_lib_deps, '<html>cdn.jsdelivr.net/npm/three@0.185.0/ new THREE.Scene()</html>', 'C:\\nonexistent')
def test_lib_echarts_gl_pass(): assert check_passes(v.check_lib_deps, '<html>type: "bar3D" scatter3D map3D globe</html>', '.')
def test_lib_echarts_gl_no_lib_fail(): assert check_fails(v.check_lib_deps, '<html>type: "bar3D"</html>', 'C:\\nonexistent')

# ==== magicui CSS effects ====
def test_anim_blur_valid(): assert check_passes(v.check_data_anim_syntax, '<html><div data-anim="blur"></div></html>')
def test_anim_fade_up_valid(): assert check_passes(v.check_data_anim_syntax, '<html><div data-anim="fade-up"></div></html>')
def test_anim_unknown_fails(): assert check_fails(v.check_data_anim_syntax, '<html><div data-anim="foobar"></div></html>')
def test_magicui_shiny_text_detected(): assert check_passes(v.check_data_anim_syntax, '<html><span class="shiny-text">hi</span></html>')
def test_anim_blur_in_list(): assert check_passes(v.check_data_anim_syntax, '<html><div data-anim="blur"></div><div data-anim="fade-up"></div></html>')

# ==== check_svg_links ====
def test_svg_links_no_svg_pass(): assert check_passes(v.check_svg_links, '<html><p>no svg</p></html>', '.')
def test_svg_links_missing_fail():
    issues = v.check_svg_links('<html><img src="nonexistent.svg"></html>', '.')
    assert len(issues) > 0 and 'nonexistent' in issues[0]

# ==== check_container_width ====
def test_container_width_ok(): assert check_passes(v.check_container_width, '<style>.container { max-width: 760px; }</style>')
def test_container_width_too_small(): assert check_fails(v.check_container_width, '<style>.container { max-width: 600px; }</style>')
def test_container_width_too_large(): assert check_fails(v.check_container_width, '<style>.container { max-width: 900px; }</style>')
def test_container_width_no_rule_pass(): assert check_passes(v.check_container_width, '<html><p>hello</p></html>')
def test_container_width_body_width_in_range_pass():
    """B5: body max-width within range should pass."""
    assert check_passes(v.check_container_width, '<style>body { max-width: 720px; }</style>')
def test_container_width_body_width_outside_flags():
    """B5: body max-width outside 700-800 should be flagged."""
    assert check_fails(v.check_container_width, '<style>body { max-width: 600px; }</style>')
def test_container_width_body_width_too_large_flags():
    """B5: body max-width >900 should be flagged."""
    assert check_fails(v.check_container_width, '<style>body { max-width: 960px; }</style>')

# ==== check_svg_contrast ====
def test_svg_contrast_no_svg_pass(): assert check_passes(v.check_svg_contrast, '<html><p>no svg</p></html>', '.')
def test_svg_contrast_dark_fill_pass():
    # Create a temp SVG with dark fill
    fd, tmpsvg = tempfile.mkstemp(suffix='.svg')
    os.close(fd)
    with open(tmpsvg, 'w', encoding='utf-8') as f: f.write('<svg><rect fill="#1a1a1a"/></svg>')
    svgname = os.path.basename(tmpsvg)
    try: assert check_passes(v.check_svg_contrast, f'<html><img src="{svgname}"></html>', os.path.dirname(tmpsvg))
    finally: os.unlink(tmpsvg)
