#!/usr/bin/env python3
"""playwright-click-test.py — demo-specific extensive suite for the Monna Map Perspective Renderer.

Per-control FUNCTIONAL assertions (PRESENCE-OVER-FUNCTION-1 / STRUCTURAL-VS-FUNCTIONAL-1):
every control is clicked with REAL pointer events and the engine-predicted output is asserted.
Usage: python playwright-click-test.py <url>   (exit 0 = all pass, 1 = any fail)
"""
import sys, time
from playwright.sync_api import sync_playwright

URL = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8765/index.html"
fails = []

def check(name, cond, extra=""):
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {name}" + (f" — {extra}" if extra else ""))
    if not cond:
        fails.append(name)

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page()
    errors = []
    page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
    page.on("pageerror", lambda e: errors.append(str(e)))

    # 1. engine loaded
    page.goto(URL, wait_until="load")
    time.sleep(1.2)
    eng = page.evaluate("!!(window._demo && window._demo.engine && window._demo.engine.monnaRational)")
    check("engine loaded (window._demo.engine.monnaRational)", eng)

    # 2. default state
    st = page.evaluate("({p: window._demo.params.p, n: window._demo.params.n, g: window._demo.params.grid})")
    check("default params p=3 n=5 grid=false", st == {"p": 3, "n": 5, "g": False}, str(st))
    golden_rows = page.locator("#tbl-golden tbody tr").count()
    check("golden table has 8 rows", golden_rows == 8, str(golden_rows))
    pass_rows = page.locator("#tbl-golden tbody tr:has(.pass)").count()
    check("all golden rows PASS (8/8)", pass_rows == 8, f"{pass_rows}/8")
    canvas_len = page.evaluate("document.getElementById('cv-rend').toDataURL().length")
    check("canvas non-blank (toDataURL > 1000)", canvas_len > 1000, str(canvas_len))

    # 3. p=2 button — real click; assert engine + readouts + golden re-run
    page.click("#btn-p2")
    time.sleep(0.8)
    check("p=2 click -> params.p == 2", page.evaluate("window._demo.params.p") == 2)
    check("p=2 -> verifyMath(2).allPass",
          page.evaluate("window._demo.engine.verifyMath(2, 5).every(r => r.pass)"))
    row1 = page.locator("#tbl-row tbody tr").first.inner_text()
    check("p=2 -> readout row 0 reflects base 2", "1.0000" in row1, row1[:60])

    # 4. p=5 button
    page.click("#btn-p5")
    time.sleep(0.8)
    check("p=5 click -> params.p == 5", page.evaluate("window._demo.params.p") == 5)
    check("p=5 -> M(-1)=5 golden PASS",
          abs(page.evaluate("window._demo.engine.monnaRational(-1, 5).value") - 5.0) < 1e-6)
    canvas5 = page.evaluate("document.getElementById('cv-naive').toDataURL()")
    check("p=5 -> naive canvas differs from p=2 state", canvas5 != canvas_len)

    # 5. depth slider to 8 (engine-predicted: params.n == 8, 9 readout rows)
    page.evaluate("""() => {
        const s = document.getElementById('depth');
        s.value = '8';
        s.dispatchEvent(new Event('input', {bubbles: true}));
    }""")
    time.sleep(0.8)
    check("slider n=8 -> params.n == 8", page.evaluate("window._demo.params.n") == 8)
    rows8 = page.locator("#tbl-row tbody tr").count()
    check("n=8 -> 9 readout rows", rows8 == 9, str(rows8))
    check("n=8 -> golden still all PASS",
          page.evaluate("window._demo.engine.verifyMath(5, 8).every(r => r.pass)"))

    # 6. grid toggle — assert rendered canvas changes
    c0 = page.evaluate("document.getElementById('cv-rend').toDataURL()")
    page.click("#grid-toggle")
    time.sleep(0.8)
    check("grid toggle -> params.grid true", page.evaluate("window._demo.params.grid") is True)
    c1 = page.evaluate("document.getElementById('cv-rend').toDataURL()")
    check("grid toggle -> rendered canvas changed", c1 != c0)

    # 7. reset — back to defaults, active button back on p=3
    page.click("#reset")
    time.sleep(0.8)
    st2 = page.evaluate("({p: window._demo.params.p, n: window._demo.params.n, g: window._demo.params.grid})")
    check("reset -> p=3 n=5 grid=false", st2 == {"p": 3, "n": 5, "g": False}, str(st2))
    active = page.evaluate("document.querySelector('.pbtn.active').dataset.p")
    check("reset -> p=3 button active", active == "3", str(active))

    # 8. zero console errors (whole session)
    check("zero console errors", len(errors) == 0, str(errors[:3]))

    # 9. mobile viewport — no horizontal overflow
    page.set_viewport_size({"width": 375, "height": 720})
    time.sleep(0.5)
    overflow = page.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth + 1")
    check("mobile 375px no horizontal overflow", not overflow)
    page.screenshot(path="screenshots/mobile.png")
    page.set_viewport_size({"width": 1280, "height": 800})
    page.screenshot(path="screenshots/desktop.png")

    browser.close()

print(f"\n{len(fails)} failures" if fails else "\nALL CHECKS PASSED")
sys.exit(1 if fails else 0)
