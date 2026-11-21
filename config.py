"""All wedding details live here. Edit this file only — the page reads everything from INVITE.

Placeholders are marked TODO. Photos/music are optional: if a file is missing the page
shows a styled placeholder instead of breaking.
"""

INVITE = {
    "couple": {"bride": "Shri Lakshmi Kulkarni", "groom": "Abhijit Kulkarni"},
    # TODO: replace with the real family names
    "families": "With the blessings of both our families",
    # Wedding date & muhurtha time, ISO format WITH timezone (IST). The countdown and calendar use this.
    "wedding": "2026-12-30T07:30:00+05:30",
    "date_text": "Wednesday, 30 December 2026",
    "blessing": "With the blessings of our elders and the love of our families, "
                "we joyfully invite you to share in the celebration of our wedding.",

    "venue": {
        "name": "Sathya Bodha Sabha Bhavana",    # TODO: confirm spelling
        "address": "Bagalkot, Karnataka",        # TODO: add street / landmark
        "maps_url": "https://www.google.com/maps/search/?api=1&query=Sathya+Bodha+Sabha+Bhavana+Bagalkot",  # TODO: paste exact Maps link
        "phone": "+910000000000",                # TODO (used for the Call button)
        "muhurat": "Muhurtha at 7:30 AM",
        "travel": "Parking available at the venue. Stay options nearby.",  # TODO
    },

    # Wedding functions / schedule ("muhurat" is optional and shown as an extra line on the card)
    "functions": [
        {"name": "Mehendi", "emoji": "🌿", "date": "28 Dec 2026", "time": "10:30 AM", "color": "#2ec4b6"},
        {"name": "Sangeet", "emoji": "🎶", "date": "28 Dec 2026", "time": "12:00 PM", "color": "#ff3d7f"},
        {"name": "Wedding", "emoji": "💍", "date": "30 Dec 2026", "time": "Morning",
         "muhurat": "Muhurtha 7:30 AM", "color": "#9b0f2e"},
        {"name": "Reception", "emoji": "🥂", "date": "30 Dec 2026", "time": "12:30 PM", "color": "#ff9f1c"},
    ],

    # Our story: told chapter by chapter (photo is optional). The last chapter ("quote": True) is styled as a quote.
    "story_title": "A little story of us… ❤️",
    "story": [
        {"label": "Chapter One", "emoji": "☕", "title": "Two strangers, one coffee",
         "text": "Two strangers, one matrimony match, and a first coffee date! ☕", "photo": ""},
        {"label": "Chapter Two", "emoji": "🌸", "title": "A sniffle and a smile",
         "text": "He showed up sick, and I showed up curious about what this meeting would turn into.", "photo": ""},
        {"label": "Chapter Three", "emoji": "💬", "title": "Endless stories",
         "text": "Turns out, I found someone who listens to my endless stories and he found someone with endless stories "
                 "(I think I got the better deal 🙈)", "photo": ""},
        {"label": "Chapter Four", "emoji": "🌙", "title": "A whisper in my heart",
         "text": "Somewhere between all my talking and his listening, I found an unexpected sense of peace and a whisper "
                 "that said ‘Maybe he is the one’ ♥️", "photo": ""},
        {"label": "Chapter Five", "emoji": "💍", "title": "The words I will never forget", "quote": True,
         "text": "I didn't want to come because I was sick, but I'm glad I came.",
         "after": "Little did we know, this was just the beginning! 🥺💍", "photo": ""},
    ],

    # Scrapbook photos (files under assets/photos). Empty list = placeholder polaroids.
    # Light copies (~100 KB) of the originals; the big .png files stay in the folder but are not embedded.
    "photos": [
        "assets/photos/ride.jpg",
        "assets/photos/giving_flower.jpg",
        "assets/photos/reading_book.jpg",
        "assets/photos/singing_song.jpg",
    ],
    # One caption per photo, in the same order ("Our first trip" is the existing caption kept for the bike ride).
    "photo_captions": ["Our first trip", "A rose for my heart", "Lost in our story", "Songs just for you"],

    # Surprise #2 (the interactive blessings section):
    #   "matka"    -> break the decorated matka (flowers, gold coins and a note fall out)
    #   "flowers"  -> shower the couple with marigold and rose petals (one wish per tap)
    #   "diyas"    -> light the diyas (one blessing per diya)
    #   "balloons" -> the original pop-a-balloon version.
    # Change this one word to switch; nothing else needs to change.
    "surprise2": "matka",

    # One message per balloon / diya (the number of balloons or diyas = number of messages)
    "balloons": [
        "Wishing you a lifetime of love 💕",
        "Your presence is our biggest gift 🎁",
        "Dance like nobody's watching 💃",
        "Good food, good music, great company 🍛",
        "Come early, stay late 🌙",
    ],

    # Background music (file under assets/music). Empty = no music button.
    # Starts when the guest taps the envelope open (browsers only allow sound after a tap).
    "music": "assets/music/shree_radhe.mp3",

    # RSVP: set endpoint to a Google Apps Script web-app URL that appends rows to a Sheet.
    # If empty, the RSVP opens WhatsApp to `whatsapp` with the message pre-filled.
    "rsvp": {
        "endpoint": "",
        "whatsapp": "910000000000",  # TODO: country code + number, digits only
    },

    # Public link to share on WhatsApp from the finale. Leave empty to share the page's own link.
    "share_url": "",

    # Hosts' sign-off used on the finale
    "signoff": "See you at the wedding! 🪔",
}
