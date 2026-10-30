"""NYC Tarot Readers (nyctarotreaders.com): a card-first directory of tarot readers across the five boroughs, with featured
readers who work inside Namaste Bookshop, plus a tarot deck shop. Copy written for this site only."""
import re, types, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dirlib
E = __import__('html').escape
ICON = 'tag'
FAM_LABEL, FAM_ALL, STYLE_LABEL, STYLE_ALL = 'Deck style', 'All styles', 'Format', 'All formats'
NO_FAMILY = ('books',)
NAV_AISLES = False
NAV_EXTRA = '<a href="/tarot-readers/">Find a reader</a><a href="/namaste-readers/">Featured</a><a href="/guide/how-to-choose-a-tarot-reader/">Guides</a><a href="/advertise/">For readers</a><a href="/shop/tarot-decks/">Decks</a>'
BOOK = dirlib.BOOK

# ---------- shop ----------
def category(p):
    t, ty = p['title'], p.get('product_type', '')
    if ty == 'Tarot Deck': return 'decks'
    if ty in ('Tarot Set', 'Tarot Kit'): return 'kits'
    if ty == 'Lenormand Deck': return 'lenormand'
    if ty == 'Tarot Talisman': return 'kits'
    if ty in ('books', 'Book', 'Books', 'Tarot Book', 'Spiritual Book') and re.search(r'\btarot\b', t, re.I): return 'books'
    return None
def assign(x): return x['base']
FAMILIES = [('rider-waite-smith', 'Rider-Waite-Smith', r'rider|waite|smith|\brws\b|radiant'), ('thoth', 'Thoth', r'thoth|crowley'), ('marseille', 'Marseille', r'marseille|marsella'),
            ('witchy', 'Witchy', r'witch|pagan|wicca|spell|magic'), ('dark-gothic', 'Dark & gothic', r'dark|goth|shadow|vampire|skull|horror|death|bone|grim'),
            ('animals-nature', 'Animals & nature', r'\bcats?\b|animal|fox|dog|wolf|bird|forest|botanic|flower|herb|garden|wild|green'), ('goddess', 'Goddess & feminine', r'goddess|feminine|women|queen|divine'),
            ('mini-pocket', 'Mini & pocket', r'\bmini\b|pocket|travel|tiny'), ('beginner', 'For beginners', r'beginner|learn|easy|starter|first'),
            ('art', 'Art & illustrated', r'art|illustrat|paint|golden|gilded|botticelli|klimt|mucha|vintage')]
def style_of(t, b, base):
    if base == 'books': return ''
    return 'Deck with guidebook' if re.search(r'guidebook|book (and|&)|set|kit|with book|\bbook\b', t, re.I) else 'Deck'
_B = [('us-games', 'U.S. Games Systems', r'u\.?s\.? games', ['U.S. Games Systems, Inc.', 'U.S. Games Systems', 'US Games Systems']),
      ('llewellyn', 'Llewellyn', r'llewellyn', ["Llewellyn's Card", 'Llewellyn Publications', 'Llewellyn Worldwide Ltd.']),
      ('lo-scarabeo', 'Lo Scarabeo', r'lo scarabeo', []), ('rockpool', 'Rockpool', r'rockpool', ['Simon Rockpool']), ('hay-house', 'Hay House', r'hay house', ['Hay House']),
      ('weiser', 'Red Wheel/Weiser', r'weiser', ['Red Wheel/Weiser']), ('blue-angel', 'Blue Angel', r'blue angel', ['Blue Angel Publishing'])]
_V = {v: k for k, _, _, vs in _B for v in vs}
def _bo(title, vendor=''):
    for k, _, rx, _ in _B:
        if re.search(rx, title, re.I): return k
    return _V.get(vendor or '', '')
BR = types.SimpleNamespace(NAME={k: n for k, n, _, _ in _B}, brand_of=_bo, FACTS={})
AISLES = {
 'decks': ('Tarot Decks', 'Decks', 'tarot-decks', 'Hundreds of tarot decks, from classic Rider-Waite-Smith to modern indie art.', '#6b3fa0'),
 'kits': ('Tarot Kits, Sets & Talismans', 'Kits', 'tarot-kits-sets', 'Deck-and-book sets, starter kits and tarot talismans.', '#c2185b'),
 'lenormand': ('Lenormand Decks', 'Lenormand', 'lenormand-decks', 'The 36-card Lenormand system for direct, practical answers.', '#00838f'),
 'books': ('Tarot Books', 'Books', 'tarot-books', 'Guides for learning the cards, spreads and reading for others.', '#8d6e63'),
}
VISIT_EYEBROW = 'Want a reading in person?'
def STORE_DESC(S): return 'Directory of tarot readers in New York City with featured readers at Namaste Bookshop near Union Square, plus a shop of tarot decks, kits and books.'
REVIEW_TITLE = 'Had a good reading?'
REVIEW_TEXT = 'A short Google review of Namaste Bookshop helps others find a reader they can trust.'
LOGO_SVG = '<svg viewBox="0 0 40 40"><rect x="9" y="5" width="18" height="28" rx="2.5" fill="none" stroke="currentColor" stroke-width="2.2" transform="rotate(-8 18 19)"/><rect x="15" y="8" width="18" height="28" rx="2.5" fill="#f4c95d" stroke="currentColor" stroke-width="2.2" transform="rotate(6 24 22)"/><circle cx="24.5" cy="22" r="3.2" fill="#6b3fa0"/></svg>'
WORDMARK = 'NYC <b>Tarot Readers</b>'
SEARCH_PLACEHOLDER = 'Search decks: thoth, marseille, cat tarot'
QUIZ = None

# ---------- directory text ----------
def _keep(x): return 'tarot' in x['offers']
def _keepf(r): return bool(set(r['tags']) & {'Tarot', 'Lenormand', 'Oracle Readings'})
T = {
 'keep': _keep, 'keep_featured': _keepf, 'lp': 'tarot-readers', 'fp': 'namaste-readers', 'dp': 'tarot-readers', 'unit': 'tarot readers',
 'email': 'customersupport@namastebookshop.com', 'dir_name': 'Tarot readers',
 'featured_intro': lambda r: f'{E(r["name"])} reads at Namaste Bookshop on West 14th Street, a few minutes from Union Square. Book through the shop\'s reading calendar, or call the readings line to ask who is in today.',
 'ftitle': lambda r: f'{r["name"]}: Tarot Reader at Namaste Bookshop, Union Square',
 'fdesc': lambda r: f'{r["name"]} ({r["specialty"]}) reads tarot inside Namaste Bookshop, 2 W 14th St, Manhattan. Sessions, prices, weekly schedule and booking.',
 'fhub_title': 'Featured Tarot Readers at Namaste Bookshop, Union Square', 'fhub_h1': 'Featured readers at Namaste Bookshop',
 'fhub_desc': 'Tarot readers who read in person at Namaste Bookshop, 2 W 14th St near Union Square: specialties, prices, schedules and booking.',
 'fhub_lead': 'These readers work from the reading room inside Namaste Bookshop at 2 West 14th Street. Each profile lists the reader\'s specialty, session prices and usual days, all taken from namastebookshop.com. They are featured because Namaste Bookshop shares an owner with this directory.',
 'ltitle': lambda x: f'{x["name"]}: Tarot Readings in {x["neighborhood"].split(" (")[0]}, {x["borough"]}',
 'ldesc': lambda x: f'{x["name"]}, {x["neighborhood"]}, {x["borough"]}: {x["note"]} Address, phone and website checked against their own site.',
 'listing_note': 'Free listing.', 'also_in': lambda b: f'More tarot readers in {b}', 'all_in': lambda b: f'All tarot readers in {b}', 'or_featured': 'Or read with a featured reader at Namaste Bookshop',
 'feat_h': 'Featured: read in person near Union Square', 'feat_p': 'Walk-in-friendly tarot, Lenormand and astrology readers who work inside Namaste Bookshop on West 14th Street. Book ahead or ask at the counter.',
 'feat_all': 'All featured readers', 'feat_other': 'Happy to travel to Manhattan? Our featured readers work near Union Square:',
 'btitle': lambda b, n: f'Tarot Readers in {b}, NYC: {n} Verified Listings by Neighborhood',
 'bdesc': lambda b, n, hs: f'{n} tarot readers in {b} sorted by neighborhood ({", ".join(hs[:4])}). Addresses, phone numbers and websites checked against each reader\'s own site.',
 'bh1': lambda b: f'Tarot readers in {b}',
 'bintro': {
  'Manhattan': 'Manhattan has the densest tarot scene in the city. Downtown, between Union Square and SoHo, you can find several readers within a short walk of each other, many of them open to walk-ins. Uptown, readers tend to work by appointment.',
  'Brooklyn': 'Brooklyn readers lean independent: healing centers in north Brooklyn, private studios, and storefront readers along Flatbush and Fifth Avenues. Many book by appointment, so check their site first.',
  'Queens': 'In Queens you will mostly find appointment-based readers working from home studios or small offices, from Astoria to Forest Hills and Bayside.',
  'Bronx': 'Several Bronx readers work inside botanicas, where a reading often sits alongside candles, herbs and spiritual supplies. Expect a mix of tarot and spiritual consultation.',
  'Staten Island': 'Staten Island readers are mostly storefronts with long hours along the main avenues, many taking walk-ins.'},
 'missing': '<b>Know a tarot reader we missed?</b> We only list readers we can check against their own website. <a href="/claim/">Suggest a reader or claim a listing</a>.',
 'dtitle': lambda n: f'Tarot Readers in NYC: {n} Readers Across the Five Boroughs',
 'ddesc': lambda n: f'Find a tarot reader in New York City: {n} readers in Manhattan, Brooklyn, Queens, the Bronx and Staten Island, each checked against their own website. Walk-ins, video readings and classes.',
 'dir_h1': 'Find a tarot reader in New York City',
 'dir_lead': 'Every reader here runs a real, current practice that we checked against their own website. No paid reviews, no star ratings, no invented listings. Pick a borough, or start with the featured readers near Union Square.',
 'browse_by': 'Or browse by how you want to be read:',
 'topics': [
  {'slug': 'walk-in', 'h1': 'Walk-in tarot readings in NYC', 'title': 'Walk-In Tarot Readings in NYC: No Appointment Needed',
   'desc': lambda n: f'{n} places in New York City that take tarot walk-ins, including readers at Namaste Bookshop near Union Square.',
   'intro': 'No appointment? These readers say on their own sites that they take walk-ins. It is still worth calling ahead on weekends. Readers at Namaste Bookshop take walk-ins when someone is free; ask at the counter.',
   'match': lambda x: 'walk-in' in x['modes'], 'fmatch': lambda r: bool(r['schedule'])},
  {'slug': 'online-and-phone', 'h1': 'NYC tarot readers who read by phone or video', 'title': 'NYC Tarot Readers Who Read by Phone or Video',
   'desc': lambda n: f'{n} New York tarot readers who offer readings by phone, FaceTime or Zoom.', 'intro': 'Based in New York but happy to read for you anywhere. These readers list phone or video sessions on their own websites.',
   'match': lambda x: 'phone' in x['modes'] or 'video' in x['modes']},
  {'slug': 'tarot-classes', 'h1': 'Learn tarot in NYC: readers who teach', 'title': 'Tarot Classes in NYC: Readers Who Teach',
   'desc': lambda n: f'{n} New York tarot readers and centers that teach tarot classes or lessons.', 'intro': 'Want to read the cards yourself? These readers and centers list classes or lessons alongside readings.',
   'match': lambda x: 'classes' in x['offers'] or 'classes' in x['modes']},
  {'slug': 'tarot-and-astrology', 'h1': 'Tarot and astrology readers in NYC', 'title': 'Tarot and Astrology Readers in NYC',
   'desc': lambda n: f'{n} New York readers who combine tarot with astrology, including featured astrologers at Namaste Bookshop.', 'intro': 'Some readers pair the cards with your birth chart: the chart shows the season you are in, the cards speak to the question in front of you.',
   'match': lambda x: 'astrology' in x['offers'], 'fmatch': lambda r: 'Astrology' in r['tags']},
  {'slug': 'union-square-village', 'h1': 'Tarot readers near Union Square and the Village', 'title': 'Tarot Readers Near Union Square, Greenwich Village and SoHo',
   'desc': lambda n: f'{n} tarot readers within walking distance of Union Square: Greenwich Village, the East and West Village, SoHo and Chelsea.',
   'intro': 'The blocks between Union Square, the Village and SoHo hold more tarot readers than anywhere else in the city. Here is who is within walking distance, starting with the readers at Namaste Bookshop on West 14th Street.',
   'match': lambda x: x['neighborhood'] in ('Union Square', 'Greenwich Village', 'West Village', 'East Village', 'SoHo', 'Chelsea'), 'fmatch': lambda r: True},
 ],
 'claim_title': 'Claim or Correct a Tarot Reader Listing', 'claim_desc': 'Run a tarot practice listed in this directory? Claim your listing for free to fix details, add hours, or ask to be removed.',
 'claim_h1': 'Claim your listing', 'claim_lead': 'Listings are free. If one of them is your practice, claim it to correct your address or phone, add hours and a photo, or ask us to take it down. Not listed? Use the same form to suggest your practice.',
 'ad_title': 'Advertise to Tarot Clients in NYC', 'ad_desc': 'Get featured in the NYC Tarot Readers directory: labeled featured listings and borough spotlights for tarot readers and spiritual businesses.',
 'ad_h1': 'Get featured on NYC Tarot Readers', 'ad_subject': 'Featured placement on NYC Tarot Readers',
 'ad_lead': 'People come here looking for a tarot reader in a specific borough or neighborhood. If you read tarot in New York, a featured spot puts you at the top of the pages they browse.',
 'ad_feat': 'your photo, specialty, schedule and booking link shown above the free listings, marked Featured.',
 'guide_cta': 'Find a tarot reader',
 'guides': [
  {'path': '/guide/how-to-choose-a-tarot-reader/', 'h1': 'How to choose a tarot reader in NYC', 'title': 'How to Choose a Tarot Reader in NYC (Without Getting Scammed)',
   'desc': 'What to look for in a New York tarot reader: deck and style, clear pricing, how they handle hard questions, and the red flags to walk away from.',
   'html': '''<p class="lead">A good reader makes you feel clearer, not more anxious. Here is how to find one.</p>
<h2>Start with the kind of reading you want</h2><p>Some readers stay close to the cards and their traditional meanings. Others read more intuitively, using the images as a starting point. Some combine tarot with astrology or Lenormand. Read a reader's own description and pick the style that sounds like a conversation you want to have.</p>
<h2>Look for clear, upfront pricing</h2><p>A professional tells you the price and length of a session before it starts. Most list it on their website or booking page.</p>
<h2>Red flags</h2><ul><li>Being told you are cursed and need to pay to have it removed.</li><li>Pressure to book more sessions or buy candles, charms or "work" on the spot.</li><li>Refusing to say the price before the reading.</li><li>Promising guaranteed outcomes, especially about health, money or getting someone back.</li></ul>
<h2>Good signs</h2><ul><li>They ask what you want to focus on.</li><li>They explain the cards as they go.</li><li>They leave decisions with you.</li><li>They are comfortable saying when a question is better for a doctor, lawyer or therapist.</li></ul>
<h2>Try a short reading first</h2><p>Many readers offer short sessions. It is an easy way to see whether their style fits before booking a longer one.</p>'''},
  {'path': '/guide/how-much-does-a-tarot-reading-cost/', 'h1': 'What does a tarot reading cost in New York?', 'title': 'How Much Does a Tarot Reading Cost in NYC?',
   'desc': 'What shapes the price of a tarot reading in New York: session length, the reader\'s experience, in person versus video, and events. Plus how to avoid surprise charges.',
   'html': '''<p class="lead">There is no single price. What you pay depends mostly on how long you book and who you book.</p>
<h2>What changes the price</h2><ul><li><b>Length.</b> Readers usually price by the session, and a longer session costs more. Short readings suit one question; longer ones suit a full spread or several topics.</li><li><b>Experience and demand.</b> Readers with decades of practice or a waiting list tend to charge more.</li><li><b>Format.</b> In-person, phone and video readings are often priced the same, but not always.</li><li><b>Extras.</b> Combined astrology and tarot sessions, recordings, and party or event bookings are usually priced separately.</li></ul>
<h2>How to avoid surprises</h2><p>Confirm the price and the length before the reading starts. Be wary of a low teaser price followed by a pitch for expensive add-ons.</p>
<h2>Where to see real prices</h2><p>Many readers publish their rates. The featured readers at Namaste Bookshop each list their session lengths and prices on their profile pages here, copied from the shop's own site.</p>'''},
  {'path': '/guide/tarot-vs-psychic-reading/', 'h1': 'Tarot reading or psychic reading: which one do you want?', 'title': 'Tarot vs Psychic Reading: What Is the Difference?',
   'desc': 'A tarot reading works from the cards on the table; a psychic reading works from the reader\'s intuition. How they differ, and how to choose.',
   'html': '''<p class="lead">Both can be insightful. The difference is where the information comes from.</p>
<h2>Tarot</h2><p>A tarot reader lays out cards from a 78-card deck in a spread and interprets them for your question. You can see the cards, ask what each means, and even photograph the spread.</p>
<h2>Psychic</h2><p>A psychic reading relies on the reader's intuition. Some psychics use cards, palms or crystals as a focus, others nothing at all. Mediums say they connect with people who have passed.</p>
<h2>Which to pick</h2><ul><li>Choose <b>tarot</b> if you like structure and want to understand the reasoning.</li><li>Choose a <b>psychic</b> or <b>medium</b> if you are drawn to an intuitive conversation or want to connect with someone you lost.</li><li>Many readers do both; ask how they work.</li></ul>
<p>Whatever you choose, readings are for reflection and entertainment, not a substitute for medical, legal or financial advice.</p>'''},
  {'path': '/guide/first-tarot-reading-tips/', 'h1': 'Your first tarot reading: what to expect', 'title': 'First Tarot Reading? What to Expect and How to Prepare',
   'desc': 'Tips for a first tarot reading in NYC: how to phrase questions, what happens during the session, whether to record it, and what to do after.',
   'html': '''<p class="lead">You do not need to believe anything in particular to get something out of a reading. Come curious.</p>
<h2>Before</h2><ul><li>Pick one or two areas to focus on: work, love, a decision.</li><li>Phrase questions openly. "What should I understand about this job offer?" works better than "Will I get rich?"</li><li>Check the price and length.</li></ul>
<h2>During</h2><ul><li>The reader shuffles (sometimes you do), lays out a spread and walks you through it.</li><li>Ask questions. A good reading is a conversation.</li><li>Ask whether you can take a photo of the spread or take notes.</li></ul>
<h2>After</h2><p>Give it a few days. Readings often make more sense in hindsight. If you want to keep exploring, pick up a beginner deck and pull a card each morning.</p>
<p><a href="/shop/tarot-decks/">Browse beginner-friendly decks</a></p>'''},
 ],
}

# ---------- home ----------
def HERO_HTML(S):
    L, F = dirlib.load(T)
    return f'''<section class="dhero"><div class="wrap"><p class="eyebrow">Five boroughs &middot; Checked listings &middot; Free to list</p><h1>Find a tarot reader in New York City</h1>
<p>{len(L) + len(F)} tarot readers from Union Square to Staten Island, each checked against their own website. Start near you, or book a featured reader at Namaste Bookshop on West 14th Street.</p>
<div class="btns"><a class="btn" href="/tarot-readers/">Browse readers</a><a class="btn ghost" href="/namaste-readers/">Featured readers</a></div>
<p class="heroloc">Featured readers work inside <b>Namaste Bookshop</b>, 2 W 14th St, a few doors west of Fifth Ave near Union Square.</p><div class="dstats"><div><b>{len(L) + len(F)}</b>tarot readers</div><div><b>{len({x["borough"] for x in L})}</b>boroughs</div><div><b>{len(F)}</b>featured at Namaste</div></div></div></section>'''
def _home_dir(S):
    L, F = dirlib.load(T)
    return (f'<section class="wrap"><div class="sechead"><h2>Browse by borough</h2><a href="/tarot-readers/">All readers &rarr;</a></div>{dirlib.boro_tiles(T, L)}</section>'
            f'<section class="wrap"><div class="sechead"><h2>Featured readers near Union Square</h2><a href="/namaste-readers/">All {len(F)} &rarr;</a></div><p class="intro">{T["feat_p"]}</p>{dirlib.featured_grid(T, F, 8)}'
            f'<div class="btns"><a class="btn" href="{BOOK}" rel="noopener">Book a reading at Namaste Bookshop</a></div></section>'
            f'<section class="wrap"><div class="sechead"><h2>Recently checked listings</h2><a href="/tarot-readers/">See all &rarr;</a></div>{dirlib.lgrid(T, L[:6])}</section>')
def _home_guides(S):
    return '<section class="wrap"><div class="sechead"><h2>Before you book</h2></div><ul class="whys">' + ''.join(f'<li><b><a href="{g["path"]}">{E(g["h1"])}</a></b><span>{E(g["desc"])}</span></li>' for g in T['guides']) + '</ul></section>'
def _home_list(S):
    return '<section class="wrap"><div class="claim"><b>Read tarot professionally in NYC?</b> Listings are free. <a href="/claim/">Claim or suggest a listing</a> &middot; <a href="/advertise/">Get featured</a></div></section>'
def _decks(S): return [x for x in S.by_rank(S.leaders) if x['aisle'] == 'decks' and not x['noimg']][:8]
def _beg(S): return [x for x in S.by_rank(S.leaders) if x['family'] in ('rider-waite-smith', 'beginner') and not x['noimg']][:8]
HERO = lambda S: {'eyebrow': '', 'h1': '', 'lede': '', 'shop_cta': ''}
HERO_BASES = ('decks',)
HOME_SECTIONS = [
 {'type': 'html', 'html': _home_dir},
 {'type': 'html', 'html': _home_guides},
 {'type': 'grid', 'title': 'Learning the cards? Start with these decks', 'select': _beg, 'href': '/shop/tarot-decks/', 'link': 'All decks'},
 {'type': 'grid', 'title': 'Tarot decks people are buying', 'select': _decks, 'href': '/shop/tarot-decks/', 'link': 'Shop decks'},
 {'type': 'html', 'html': _home_list},
 {'type': 'visit'},
]
def HOME_TITLE(S): return 'Tarot Readers in NYC | Find a Tarot Reader in Manhattan, Brooklyn & Queens'
def HOME_DESC(S):
    L, F = dirlib.load(T)
    return f'Directory of {len(L) + len(F)} tarot readers in New York City, by borough and neighborhood, each checked against their own website. Featured readers near Union Square, guides, and tarot decks.'
def HOME_LD(S):
    L, F = dirlib.load(T)
    return [S.store_ld(), {'@context': 'https://schema.org', '@type': 'Organization', 'name': 'Wealth Edge Ventures Inc.', 'brand': S.BRAND, 'url': S.SITE + '/'},
            dirlib.itemlist(S, 'Tarot readers in New York City', [(r['name'], f'/namaste-readers/{r["slug"]}/') for r in F] + [(x['name'], f'/tarot-readers/{x["slug"]}/') for x in L])]
def LLMS_EXTRA(S):
    L, F = dirlib.load(T)
    return (['## Tarot reader directory', f'- [All tarot readers in NYC]({S.SITE}/tarot-readers/): {len(L) + len(F)} readers, each checked against their own website; data at {S.SITE}/data/listings.json']
            + [f'- [Tarot readers in {b}]({S.SITE}/tarot-readers/{dirlib.slug(b)}/)' for b in dirlib.BORO if any(x["borough"] == b for x in L)]
            + [f'- [{g["h1"]}]({S.SITE}/tarot-readers/{g["slug"]}/)' for g in T['topics']] + ['', '## Featured readers at Namaste Bookshop (2 W 14th St; book at https://namastebookshop.com/pages/book-a-reading)']
            + [f'- [{r["name"]}]({S.SITE}/namaste-readers/{r["slug"]}/): {r["specialty"]}' for r in F] + ['', '## Guides'] + [f'- [{g["h1"]}]({S.SITE}{g["path"]})' for g in T['guides']] + [''])
def GUIDES(S): return dirlib.pages(T, S)

def SHOP_TITLE(S): return 'Tarot Decks, Kits & Books | NYC Tarot Readers'
def SHOP_DESC(S): return f'{S.N:,} tarot decks, Lenormand decks, kits and tarot books. Ships from NYC or pick up at Namaste Bookshop, 2 W 14th St.'
SHOP_H1 = 'Tarot decks and books'
def SHOP_SUB(S): return f'{S.N:,} items. Filter by deck style, publisher or price.'
def AISLE_TITLE(S, k): return f'{AISLES[k][0]} | NYC Tarot Readers'
def AISLE_DESC(S, k): return f'{AISLES[k][3]} {S.cat_count[k]} in stock. Ships from NYC or pick up near Union Square.'
def FOOTER_EXPLORE(S):
    return [('Find a tarot reader', '/tarot-readers/'), ('Featured readers', '/namaste-readers/'), ('Walk-in readings', '/tarot-readers/walk-in/'), ('Choosing a reader', '/guide/how-to-choose-a-tarot-reader/'),
            ('Claim a listing', '/claim/'), ('Advertise', '/advertise/'), ('Tarot decks', '/shop/tarot-decks/')]
FOOT_BLURB = 'A free, checked directory of tarot readers in the five boroughs, published by the owners of Namaste Bookshop.'
def LANDINGS(S):
    return [{'path': f'/decks/{k}/', 'title': f'{n} Tarot Decks | NYC Tarot Readers', 'desc': f'{S.fam_count[k]} {n.lower()} tarot decks in stock, from {S.money(min(x["price"] for x in S.products if x["family"] == k))}.',
             'h1': f'{n} tarot decks', 'sub': f'{S.fam_count[k]} in stock.', 'filter': {'fam': [k]}} for k, n, _ in FAMILIES if S.fam_count[k] >= 4]
def brand_intro(S, k, st): return f'<p>{st["n"]} tarot titles from {E(S.BRAND_NAME[k])}, from {S.money(st["min"])}.</p>'
def brand_faq(S, k, st): return [(f'Do you stock {S.BRAND_NAME[k]} decks?', f'Yes, {st["n"]} are listed today.')]
def BRAND_H1(S, k): return f'{S.BRAND_NAME[k]} tarot decks'
def BRAND_TITLE(S, k, st): return f'{S.BRAND_NAME[k]} Tarot Decks | NYC Tarot Readers'
def BRAND_DESC(S, k, st): return f'{st["n"]} {S.BRAND_NAME[k]} tarot decks and books from {S.money(st["min"])}.'
def BRANDS_TITLE(S): return 'Tarot Publishers | NYC Tarot Readers'
def BRANDS_DESC(S): return 'Tarot decks by publisher.'
BRANDS_H1 = 'Tarot publishers'
def BRANDS_LEAD(S, n): return f'{n} publishers.'
PAIR = {'decks': ['books', 'kits'], 'kits': ['books', 'decks'], 'lenormand': ['decks', 'books'], 'books': ['decks']}
CART_PAIR_TITLE = 'Goes with your deck'
REL_BRAND = 'More from {brand}'
REL_SCENT = 'More {scent} decks'
REL_PAIR = 'Pairs well with'
REL_MORE = 'More {aisle}'
def describe(S, x):
    fam = S.FAM_NAME.get(x['family'], '')
    s = [f"{E(x['title'])}, from the tarot shelf at NYC Tarot Readers."]
    if fam: s.append(f'Style: {E(fam)}. <a href="/decks/{x["family"]}/">More {E(fam.lower())} decks</a>.')
    s.append({'decks': 'Want to see how a reader uses the cards before you learn? <a href="/namaste-readers/">Book a featured reader</a> and ask about their deck.',
              'lenormand': 'Lenormand uses 36 cards read in combinations; several featured readers pair it with tarot.',
              'books': 'A good companion for learning the cards on your own.', 'kits': 'A complete starting point: cards plus guidance.'}[x['aisle']])
    s.append('Ships from New York City, or pick up inside Namaste Bookshop, 2 West 14th Street. Checkout on Shopify.')
    return s
def PRODUCT_DESC(S, x, v0): return f"{x['title']}, {S.money(v0['price'])}. Tarot from NYC: ships or pick up at 2 W 14th St."
def ABOUT_DESC(S): return 'About NYC Tarot Readers: who publishes the directory, how listings are checked, and why some readers are featured.'
ABOUT_H1 = 'About NYC Tarot Readers'
def ABOUT(S):
    return f'''<p class="lead">NYC Tarot Readers is a free directory of tarot readers in New York City.</p>
<h2>How listings are checked</h2><p>We only list readers with a working website that describes a current tarot practice in New York. Names, neighborhoods, addresses and phone numbers come from that website, and every listing links to it with the date we checked. We do not copy reviews, publish star ratings or invent listings. Readers can <a href="/claim/">claim, correct or remove</a> their listing at any time.</p>
<h2>Who publishes it</h2><p>{S.LEGAL} Wealth Edge Ventures also owns Namaste Bookshop at {S.STORE_ADDR}. The readers marked <b>Featured</b> work at Namaste Bookshop, and their profiles come from <a href="https://namastebookshop.com/pages/book-a-reading" rel="noopener">namastebookshop.com</a>. Featured spots may also be offered to other readers as clearly labeled paid placements; see <a href="/advertise/">advertise</a>.</p>
<h2>The shop</h2><p>We also sell tarot decks, kits and books. Checkout runs on Shopify through <a href="{S.SHOP}" rel="noopener">namastebookshop.com</a>; orders ship from New York or can be picked up at Namaste Bookshop.</p>{S.hours_html()}'''
def FAQ_DESC(S): return 'Questions about NYC Tarot Readers: how readers are listed, featured placements, booking and buying a deck.'
FAQ_H1 = 'NYC Tarot Readers FAQ'
def FAQ(S):
    return [('How do you choose which readers to list?', 'Any New York tarot reader with a current website describing their practice can be listed. We check details against that site.'),
            ('What does Featured mean?', 'Featured readers work at Namaste Bookshop, which shares an owner with this site, or have paid for a labeled placement.'),
            ('Do you rate or review readers?', 'No. We do not publish ratings or reviews. Read about each reader on their own site and use our guide to choosing a reader.'),
            ('How do I book?', 'Use the reader\'s website or phone number. For featured readers, book through the Namaste Bookshop reading calendar.'),
            ('I am a reader. How do I get listed or removed?', 'Use the <a href="/claim/">claim form</a>. It is free.'),
            ('Do you sell tarot decks?', 'Yes, hundreds. See <a href="/shop/tarot-decks/">tarot decks</a>.')]
NOT_FOUND = 'That card is not in this deck'
