import streamlit as st
import time

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="For Chidka Boka ♡",
    page_icon="🌷",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600;700&family=Montserrat:wght@400;500&display=swap');

.stApp {
    background:
        radial-gradient(circle at 20% 20%, rgba(255,255,255,0.45), transparent 25%),
        radial-gradient(circle at 80% 70%, rgba(170,125,90,0.08), transparent 30%),
        #eadbc5;
    color: #5b4438;
}

.block-container {
    max-width: 850px;
    padding: 2rem 1rem 4rem 1rem;
}


/* ---------------- HEADINGS ---------------- */

h1, h2, h3 {
    font-family: 'Cormorant Garamond', serif !important;
    color: #68483d !important;
    letter-spacing: 1px;
}


/* ---------------- NORMAL TEXT ---------------- */

p, li {
    font-family: 'Montserrat', sans-serif;
    color: #654d42;
    line-height: 1.7;
}


/* ---------------- HERO ---------------- */

.hero {
    text-align: center;
    padding: 50px 15px 35px 15px;
}

.flower {
    font-size: 45px;
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-8px);
    }

    100% {
        transform: translateY(0px);
    }
}

.hero h1 {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 58px !important;
    line-height: 1.05;
    margin-bottom: 10px;
    color: #68483d !important;
}

.subtitle {
    font-family: 'Montserrat', sans-serif;
    font-size: 15px;
    color: #85675a;
    letter-spacing: 1.5px;
}

.date {
    font-family: 'Cormorant Garamond', serif;
    font-size: 20px;
    color: #98705d;
    letter-spacing: 3px;
}


/* ---------------- VINTAGE CARDS ---------------- */

.card {
    background:
        linear-gradient(
            rgba(255,250,239,0.90),
            rgba(247,236,216,0.94)
        );

    border: 1px solid rgba(120,85,62,0.25);
    border-radius: 5px;
    padding: 28px;
    margin: 20px 0;

    box-shadow:
        0 5px 15px rgba(78,52,35,0.10),
        inset 0 0 25px rgba(139,102,70,0.05);
}


/* ---------------- LETTER ---------------- */

.letter {
    background: #fff9ec;
    border: 1px solid #cdb79d;
    border-radius: 3px;
    padding: 30px 25px;
    line-height: 1.9;

    font-family: 'Cormorant Garamond', serif;
    font-size: 19px;
    color: #5f493d;

    box-shadow:
        0 5px 15px rgba(80,55,40,0.10);
}


/* ---------------- BUTTONS ---------------- */

.stButton > button,
.stLinkButton > a {
    width: 100%;
    border-radius: 3px !important;

    border: 1px solid #654438 !important;

    background-color: #7b5548 !important;
    color: #fff8ed !important;

    font-family: 'Montserrat', sans-serif !important;
    font-weight: 500;

    letter-spacing: 0.5px;

    padding: 12px !important;

    transition: all 0.3s ease;
}

.stButton > button:hover,
.stLinkButton > a:hover {
    background-color: #624238 !important;
    transform: translateY(-2px);
}


/* ---------------- DIVIDER ---------------- */

.divider {
    text-align: center;

    color: #9b705e;

    font-family: 'Cormorant Garamond', serif;

    font-size: 25px;

    margin: 30px 0;
}

.divider::before,
.divider::after {
    content: " ─── ";
    color: #b18a72;
}


/* ---------------- IMAGES ---------------- */

img {
    border: 7px solid #f8efdf;

    box-shadow:
        0 5px 15px rgba(70,45,30,0.18);
}


/* ---------------- FOOTER ---------------- */

.footer {
    text-align: center;

    color: #806254;

    font-family: 'Montserrat', sans-serif;

    font-size: 13px;

    margin-top: 50px;
}


/* ---------------- MOBILE ---------------- */

@media (max-width: 600px) {

    .block-container {
        padding: 1rem 0.8rem 3rem 0.8rem;
    }

    .hero {
        padding-top: 30px;
    }

    .hero h1 {
        font-size: 42px !important;
    }

    .card {
        padding: 20px;
    }

    .letter {
        padding: 23px 18px;
        font-size: 17px;
    }

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<div class="flower">🌷</div>

<h1>
Happy Birthday,<br>
Chidka Boka ♡
</h1>

<p class="subtitle">
A little something made just for you
</p>

<p class="date">
30 • 09 • 2006
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# OPEN BUTTON
# ============================================================

if st.button("🎁 Open Your Surprise"):

    st.balloons()

    st.markdown("""
    <div class="card" style="text-align:center;">

    <h2>Hi Chidka Boka ♡</h2>

    <p>
    You probably weren't expecting a whole website,
    but here we are...
    </p>

    <p>
    Made with a little bit of code,
    a lot of memories,
    and way too much love.
    </p>

    <p style="font-size:25px;">
    — Shrads 🌷
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# OUR STORY
# ============================================================

st.markdown(
    '<div class="divider">♡ · ♡ · ♡</div>',
    unsafe_allow_html=True
)

st.header("Our Little Story 🌷")

st.markdown("""
<div class="card">

<p>
Some people enter your life unexpectedly
and somehow become a really important part of it.
</p>

<p>
And then there's you.
</p>

<p>
From being friends to becoming something more,
there are so many little moments that
I wouldn't trade for anything.
</p>

<p>
This website is just a tiny collection
of some of those feelings.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# MEMORIES
# ============================================================

st.header("Little Memories 📸")

st.markdown("""
<div class="card">

<p style="text-align:center; font-size:18px;">
Before we even knew what was coming... ♡
</p>

<p style="text-align:center; color:#987c78;">
Somehow, we've been making memories for a very long time.
</p>

</div>
""", unsafe_allow_html=True)


# ---------------- FIRST CHILDHOOD PHOTO ----------------

st.image(
    "childhood1.jpeg",
    caption="Little us ♡",
    width="stretch"
)

st.markdown("""
<p style="text-align:center; color:#806254; font-style:italic;">
And look at those tiny faces...
</p>
""", unsafe_allow_html=True)


# ---------------- SECOND CHILDHOOD PHOTO ----------------

st.image(
    "childhood2.jpeg",
    caption="And then there was this ♡",
    width="stretch"
)

st.markdown("""
<div class="card" style="text-align:center;">

<p>
We really had no idea that these little moments
would become memories we'd look back on someday.
</p>

<p style="font-size:20px;">
♡
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# LETTER
# ============================================================

st.header("A Letter For You 💌")

st.markdown("""
<div class="letter">

<p>Dear Chidka Boka,</p>

<p>
Happy Birthday to you. ♡
</p>

<p>
This is where your actual birthday letter will go.
I wanted to make something a little different
for you this time.
</p>

<p>
There are probably a hundred things I could say,
but some things are easier to write than say out loud.
</p>

<p>
So this little corner of the internet is yours.
Just for today.
</p>

<p>
I hope you have the happiest birthday
and I hope you know how special you are to me.
</p>

<p>
With love,<br>
<strong>Shrads ♡</strong>
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# THINGS ABOUT HIM
# ============================================================

st.header("A Few Things About You ♡")

things = [
    "You make ordinary days feel a little less ordinary.",
    "You somehow manage to make me smile even when I'm annoyed.",
    "You're someone I can talk to about random things.",
    "You have a very special place in my life.",
    "And yes... you're stuck with Shrads now. 😌"
]

for i, thing in enumerate(things, 1):

    st.markdown(f"""
    <div class="card">

    <h3 style="margin-bottom:5px;">
    {i:02d}
    </h3>

    <p>
    {thing}
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# PLAYLIST
# ============================================================

st.header("A Song For You 🎧")

st.markdown("""
<div class="card">

<p style="text-align:center; font-size:20px;">
🎵 Hum Tere Pyaar Mein
</p>

<p style="text-align:center; color:#806254;">
Lata Mangeshkar
</p>

<p style="text-align:center; font-style:italic;">
A song that says a little of what I can't always put into words ♡
</p>

</div>
""", unsafe_allow_html=True)

st.link_button(
    "🎧 Listen to the song ♡",
    "https://www.youtube.com/results?search_query=Hum+Tere+Pyaar+Mein+Lata+Mangeshkar"
)


# ============================================================
# FINAL SURPRISE
# ============================================================

st.markdown(
    '<div class="divider">♡ · ♡ · ♡</div>',
    unsafe_allow_html=True
)

st.header("One Last Thing 🎁")

if st.button("💗 Click Me"):

    st.markdown("""
    <div class="card" style="text-align:center;">

    <div style="font-size:50px;">
    🌷
    </div>

    <h2>
    Happy Birthday, Chidka Boka ♡
    </h2>

    <p>
    I hope this year brings you lots of happiness,
    good memories and everything you've been wishing for.
    </p>

    <p>
    Thank you for being you.
    </p>

    <p style="font-size:20px;">
    I love you. ♡
    </p>

    <p>
    — Shrads
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

Made with ♡ by Shrads

</div>
""", unsafe_allow_html=True)
