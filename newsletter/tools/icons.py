#!/usr/bin/env python3
"""
icons.py — on-brand inline SVG glyphs for the newsletter, replacing stock emoji.

Each icon is a minimal line glyph drawn with currentColor so the badge's own
color (set per-section in CSS) fills it. 24x24 viewBox, 2px strokes. Keyed by
the section CSS class (s-news, s-mt, …). ICON(cls) returns an <svg> string.
"""

# All glyphs use stroke:currentColor; fill:none unless noted. The badge sets
# color via CSS (badge text color), so icons inherit the per-section accent.
_P = ('<svg viewBox="0 0 24 24" width="15" height="15" fill="none" '
      'stroke="currentColor" stroke-width="2" stroke-linecap="round" '
      'stroke-linejoin="round">{}</svg>')

_PATHS = {
    # radio tower (masthead + general): mast with signal arcs
    "tower":  '<path d="M12 8v13"/><path d="M8 21h8"/><path d="M12 8l-4 8"/>'
              '<path d="M12 8l4 8"/><path d="M5 6a7 7 0 0 1 14 0"/>'
              '<path d="M8 7a4 4 0 0 1 8 0"/>',
    # news: document with lines
    "news":   '<rect x="4" y="4" width="16" height="16" rx="2"/>'
              '<path d="M8 9h8M8 13h8M8 17h5"/>',
    # calendar (events)
    "cal":    '<rect x="4" y="5" width="16" height="15" rx="2"/>'
              '<path d="M4 9h16M8 3v4M16 3v4"/>',
    # camera (photo/video)
    "cam":    '<rect x="3" y="7" width="18" height="12" rx="2"/>'
              '<circle cx="12" cy="13" r="3.2"/><path d="M8 7l1.5-2h5L16 7"/>',
    # meshtastic: node with radiating dots (mesh)
    "mt":     '<circle cx="12" cy="12" r="2.5"/><circle cx="5" cy="6" r="1.5"/>'
              '<circle cx="19" cy="6" r="1.5"/><circle cx="5" cy="18" r="1.5"/>'
              '<circle cx="19" cy="18" r="1.5"/><path d="M10 11L6.3 7M14 11l3.7-4'
              'M10 13l-3.7 4M14 13l3.7 4"/>',
    # meshcore: linked chain
    "mc":     '<path d="M9 12a3 3 0 0 1 3-3h2a3 3 0 0 1 0 6h-1"/>'
              '<path d="M15 12a3 3 0 0 1-3 3h-2a3 3 0 0 1 0-6h1"/>',
    # reticulum: satellite/relay dish
    "rns":    '<path d="M5 14a7 7 0 0 1 7-7"/><path d="M8 14a4 4 0 0 1 4-4"/>'
              '<circle cx="12" cy="14" r="1.5"/><path d="M12 15.5L8 21h8z"/>',
    # market/tag (for sale & wanted)
    "tag":    '<path d="M4 4h7l9 9-7 7-9-9z"/><circle cx="8" cy="8" r="1.3"/>',
    # megaphone (call to action)
    "cta":    '<path d="M4 10v4a1 1 0 0 0 1 1h2l7 4V5L7 9H5a1 1 0 0 0-1 1z"/>'
              '<path d="M17 8a5 5 0 0 1 0 8"/>',
    # star (spotlight)
    "star":   '<path d="M12 3l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9 6.8 19.1l1-5.8'
              'L3.5 9.2l5.9-.9z"/>',
    # book (wiki)
    "book":   '<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z"/>'
              '<path d="M4 19a2 2 0 0 1 2-2h13"/>',
    # globe (around the web)
    "globe":  '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/>'
              '<path d="M12 3a14 14 0 0 1 0 18a14 14 0 0 1 0-18z"/>',
    # feather/quill (story)
    "story":  '<path d="M20 4C11 5 6 10 4 20l3-3c6 0 11-4 13-13z"/><path d="M7 17l5-5"/>',
    # bookmark (sources)
    "cite":   '<path d="M6 3h12v18l-6-4-6 4z"/>',
    # app window (mesh-client)
    "app":    '<rect x="3" y="4" width="18" height="16" rx="2"/>'
              '<path d="M3 8h18"/><circle cx="6" cy="6" r=".6"/><circle cx="8.5" cy="6" r=".6"/>',
    # wrench (gear & firmware)
    "wrench": '<path d="M15 4a4 4 0 0 0-5.2 5.2L4 15v5h5l5.8-5.8A4 4 0 0 0 20 9l-3 3-2-2 3-3a4 4 0 0 0-3-3z"/>',
    # wave/hand (signoff)
    "wave":   '<path d="M6 12V7a1.5 1.5 0 0 1 3 0v4M9 11V5a1.5 1.5 0 0 1 3 0v6'
              'M12 11V6a1.5 1.5 0 0 1 3 0v6M15 12V8a1.5 1.5 0 0 1 3 0v6a6 6 0 0 1'
              '-6 6h-1a6 6 0 0 1-5-3l-2-3a1.5 1.5 0 0 1 2.6-1.5L9 15"/>',
}

# section CSS class -> glyph key
_SECTION_ICON = {
    "s-news":   "news",
    "s-events": "cal",
    "s-photo":  "cam",
    "s-client": "app",
    "s-mt":     "mt",
    "s-mc":     "mc",
    "s-rns":    "rns",
    "s-gear":   "wrench",
    "s-market": "tag",
    "s-cta":    "cta",
    "s-spot":   "star",
    "s-wiki":   "book",
    "s-web":    "globe",
    "s-story":  "story",
    "s-cite":   "cite",
    "s-bye":    "wave",
}


def icon_for(section_cls):
    key = _SECTION_ICON.get(section_cls, "tower")
    return _P.format(_PATHS[key])


def masthead_icon():
    return _P.format(_PATHS["tower"])
