# source/conf.py
import os
import sys
from datetime import datetime

# -- Project Information -----------------------------------------------------
project = 'Batly R1 Manual'
copyright = f'{datetime.now().year}, RTL (ICRT), Burapha University'
author = 'Pisak & RTL Team'
release = '1.0'

# -- Extensions (The Power Tools) --------------------------------------------
extensions = [
    'myst_parser',          # Write in Markdown
    'sphinx_rtd_theme',     # Professional Theme
    'sphinx_copybutton',    # "Copy" button on code blocks
    'sphinx_design',        # Tabs, Badges, and Dropdowns
]

# MyST SETTINGS (Features inside the engine)
# ---------------------------------------------------------
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",   # <--- PUT IT HERE
    "amsmath",      # <--- AND HERE
]

# -- General Settings --------------------------------------------------------
exclude_patterns = []
templates_path = ['_templates']
pygments_style = 'xcode'

# Enable Figure Numbering
numfig = True

# -- HTML Theme Settings (Website) -------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

# หารูปโลโก้
html_logo = '_static/rtl_background.jpg'

# ไอคอนตรง Tab Browser
html_favicon = '_static/favicon_rtl.png'

html_theme_options = {
    'logo_only': True,  # True ถ้าในรูปมีชื่อบริษัทอยู่แล้ว
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'navigation_depth': 3,
    'collapse_navigation': False, # Keep menu open for students
}

# -- PDF / LaTeX Settings (Thai Language Support) ----------------------------
latex_engine = 'xelatex'

latex_elements = {
    # 1. Paper Size
    'papersize': 'a4paper',
    'pointsize': '11pt',

    # 2. Geometry (This fixes the Error)
    # We override the default package load here
    'geometry': r'\usepackage[margin=1in]{geometry}',

    # 3. Thai Fonts
    'fontpkg': r'''
% Scale=1.23 makes Sarabun 23% bigger, matching standard English size
\setmainfont[Scale=1.35]{TH Sarabun New}
\setsansfont[Scale=1.35]{TH Sarabun New}
\setmonofont[Scale=0.9]{Consolas}
''',

    # 4. Preamble (Cleaned up)
    # Notice: No geometry and No xeCJK here anymore
    'preamble': r'''
\usepackage{indentfirst}
\setlength{\parskip}{0.5em}

% Increase line spacing by 30% so Thai vowels don't crash
\linespread{1.4}

% --- FIX LINE NUMBERS ---
% Change line numbers from \tiny to \footnotesize (readable size)
\renewcommand{\theFancyVerbLine}{\footnotesize\arabic{FancyVerbLine}}

% --- THAI LINE BREAKING FIX ---
\XeTeXlinebreaklocale "th"
\XeTeXlinebreakskip = 0pt plus 1pt

% --- CENTER CAPTIONS ---
\usepackage{caption}
\captionsetup{justification=centering}

% --- เพิ่มบรรทัดนี้เพื่อคุมเลขหัวข้อใน PDF ---
\setcounter{secnumdepth}{2}
\setcounter{tocdepth}{2}
''',
}

# --- COPY BUTTON CONFIGURATION ---
# บอกให้ Copy Button รู้ว่าถ้าเจอบรรทัดที่ขึ้นต้นด้วย $ ให้ตัดทิ้งตอน Copy
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True


# (Optional) ถ้าอยากลบคำว่า Built with Sphinx ออกเพื่อให้ดู Clean
html_show_sphinx = False