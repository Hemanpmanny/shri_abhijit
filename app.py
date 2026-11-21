"""Streamlit host for the wedding e-invitation.

Streamlit only provides the hosting shell. The whole invitation is one self-contained
page (templates/index.html) rendered with components.html, so all animations run in the
browser without Streamlit reruns.

Run locally:   streamlit run app.py
"""

from __future__ import annotations

import base64
import json
import mimetypes
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

from config import INVITE

BASE = Path(__file__).resolve().parent
TEMPLATE = BASE / "templates" / "index.html"

st.set_page_config(
    page_title=f"{INVITE['couple']['bride']} & {INVITE['couple']['groom']} | Wedding Invitation",
    page_icon="💐",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit chrome and make the invitation iframe fill the screen.
st.markdown(
    """
    <style>
      #MainMenu, header, footer,
      [data-testid="stToolbar"], [data-testid="stDecoration"],
      [data-testid="stStatusWidget"], [data-testid="stSidebar"] { display: none !important; }
      .block-container, [data-testid="stMainBlockContainer"] { padding: 0 !important; max-width: 100% !important; }
      /* Streamlit puts a 16px gap between page elements; that gap pushed the invitation down and made the page scroll. */
      [data-testid="stVerticalBlock"] { gap: 0 !important; }
      [data-testid="stElementContainer"]:has(style) { display: none !important; }
      .stApp { background: #2a0612; }
      html, body { overscroll-behavior: none; }
      /* 100dvh = the visible height on phones (the address bar is not counted); 100vh is the fallback. */
      iframe { border: 0 !important; width: 100% !important; display: block !important;
               height: 100vh !important; min-height: 100vh !important; }
      @supports (height: 100dvh) { iframe { height: 100dvh !important; min-height: 100dvh !important; } }
    </style>
    """,
    unsafe_allow_html=True,
)


def _data_uri(rel: str) -> str:
    """Embed a project file as a data URI. Returns '' if the file is missing."""
    if not rel:
        return ""
    path = BASE / rel
    if not path.is_file():
        return ""
    mime = mimetypes.guess_type(path.name)[0] or {".webp": "image/webp", ".jpg": "image/jpeg", ".jpeg": "image/jpeg"}.get(path.suffix.lower(), "application/octet-stream")
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def _guest_name() -> str:
    """Read ?guest=Name from the URL for a personalised greeting."""
    try:
        value = st.query_params.get("guest", "")
        return value if isinstance(value, str) else (value[0] if value else "")
    except Exception:
        return st.experimental_get_query_params().get("guest", [""])[0]


def _stamp() -> int:
    """Newest modification time of everything the page is built from, so edits are never served from a stale cache."""
    files = [TEMPLATE, BASE / "config.py", *(BASE / "assets").rglob("*")]
    return max((f.stat().st_mtime_ns for f in files if f.is_file()), default=0)


@st.cache_data(show_spinner=False)
def build_page(guest: str, stamp: int) -> str:
    cfg = json.loads(json.dumps(INVITE))  # deep copy
    cfg["photos"] = [uri for uri in (_data_uri(p) for p in INVITE["photos"]) if uri]
    cfg["story"] = [{**s, "photo": _data_uri(s.get("photo", ""))} for s in INVITE["story"]]
    cfg["music"] = _data_uri(INVITE["music"])
    cfg["frame"] = {
        "corner_l": _data_uri("assets/frame/corner_l.png"),
        "corner_r": _data_uri("assets/frame/corner_r.png"),
        "ganesha": _data_uri("assets/frame/ganesha.png"),
        "pet_camel": _data_uri("assets/frame/pet_camel.png"),
        "pet_elephant": _data_uri("assets/frame/pet_elephant.png"),
        "pet_horse": _data_uri("assets/frame/pet_horse.png"),
        "pet_peacock": _data_uri("assets/frame/pet_peacock.png"),
        "art_couple": _data_uri("assets/frame/art_couple.png"),
        "art_lotus1": _data_uri("assets/frame/art_lotus1.png"),
        "art_lotus2": _data_uri("assets/frame/art_lotus2.png"),
    }
    cfg["guest"] = guest.strip()[:60]
    # Safe for embedding inside <script>
    payload = json.dumps(cfg, ensure_ascii=False).replace("</", "<\\/")
    html = TEMPLATE.read_text(encoding="utf-8")
    return html.replace("/*__CONFIG__*/{}", payload)


page_html = build_page(_guest_name(), _stamp())
if hasattr(st, "iframe"):
    # Newer Streamlit: components.v1.html is deprecated in favour of st.iframe.
    # Fixed pixel height (CSS above stretches it to the viewport) so the page scrolls inside the frame.
    st.iframe(page_html, height=900)
else:
    components.html(page_html, height=900, scrolling=True)
