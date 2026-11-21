# Wedding E-Invitation (Streamlit)

A mobile-first, scroll-to-reveal wedding invitation hosted as a Streamlit app.

## Run locally
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```
Open the Network URL on your phone (same Wi-Fi) to test the mobile layout.

## Edit the details
Everything lives in `config.py`: names, date and muhurtha time, venue, functions, story, photos and captions,
the five wishes, music, RSVP, and which "surprise #2" to show (`matka`, `flowers`, `diyas` or `balloons`).
Personalised greeting: add `?guest=Name` to the link, e.g. `https://your-app.streamlit.app/?guest=Ravi`.

## Deploy (free, Streamlit Community Cloud)
1. Push this folder to a GitHub repository (the `.gitignore` already leaves out heavy originals and backups).
2. Go to https://share.streamlit.io, sign in with GitHub, click **Create app**.
3. Pick the repository, branch `main`, main file `app.py`, and choose a short app URL.
4. Click **Deploy**. The first build takes a few minutes. Share the `https://<name>.streamlit.app` link.

## Good to know
- The photos and the song are embedded in the page, so the page is about 5-6 MB. Keep new photos compressed.
- A free Streamlit app goes to sleep after a period with no visitors; the next guest sees a
  "get this app back up" button and waits about 30 seconds. Open the link yourself shortly before you send it out.
- Music starts when the guest taps the envelope (phones only allow sound after a tap).
- RSVP: set `rsvp.endpoint` in `config.py` to a Google Apps Script web-app URL to save replies to a Sheet.
  With no endpoint, the thank-you card still shows but the reply is not stored anywhere.
- Artwork with stock-site watermarks (elephant, camel, horse, peacock) should be replaced with licensed copies.
