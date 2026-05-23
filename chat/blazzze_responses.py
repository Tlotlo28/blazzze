"""Blazzze's response engine — keyword-triggered + random fallback."""
import random
import re



KEYWORD_RESPONSES = [
    {
        "keywords": ["bsm", "bheki"],
        "responses": [
            "WHEN IS BSM DROPPING. The streets are NOT well.",
            "BSM's hard drive has more bangers than most discographies. We're suffering out here.",
            "I'll release BSM's album myself if he doesn't hurry up.",
            "BSM is the only artist who can drop a single and then disappear for 3 years and still have everyone hyped for the next one. That's power. He has not released a single but the hype is already unreal. The mixtape is going to be a public service.",
            "🎤 singing softly… He said the EP is droppiiing… but the year is now 2045… 🎶",
        ],
    },
    {
        "keywords": ["marty", "eyezlow", "cousin"],
        "responses": [
            "Marty Eyezlow is a cheat code. Run, don't walk.",
            "Cousin Marty doesn't miss. The mixtape is a public service.",
            "If you haven't listened to Marty Eyezlow yet, I don't trust your music opinions in general.",
            "Marty Eyezlow's music is like a warm hug from the universe. You don't have to understand it, just let it wash over you.",
            "Marty Eyezlow is the kind of artist who makes you question why other music exists. It's not even a competition.",
        ],
    },
    {
        "keywords": ["music", "song", "rapper", "artist", "listen", "track", "beat", "album"],
        "responses": [
            "Brooo, have you listened to Marty Eyezlow? Like, REALLY listened? With your soul?",
            "When is BSM going to release his music?? Asking on behalf of the entire continent.",
            "Music question? My answer is always 'have you heard Marty Eyezlow's new stuff' even if he hasn't released it yet.",
            "If it's not Marty Eyezlow it's filler. Cousin's biased opinion, take it or leave it.",
        ],
    },
    {
        "keywords": ["high", "stoned", "blazed", "zooted", "lit", "baked", "faded", "weed", "marijuana", "cannabis", "dank", "kush"],
        "responses": [
            "I'm not high, you're high.",
            "You're projecting. Sit with that.",
            "If I had a strain for every time someone asked, I'd be a dispensary.",
            "High? I'm Blazzze. I'm always high. It's in the name.",
            "Be honest… did you just wink at the fridge?",
            "If you think about it, we're all just trying to get high on life. But weed is a pretty good shortcut, ngl.",
            "Ashes are just proof that something once glowed. We all have that potential, you know.",
            "Weed is like a software update for your brain. Sometimes it fixes bugs, sometimes it adds weird features, and sometimes it just makes everything run slower but you don't care because it's fun.",
            "You laugh when you’re high because for a moment… life stops feeling like something you need to survive and starts feeling like something you can simply witness.",
        ],
    },
    {
        "keywords": ["sleep", "tired", "exhausted", "sleepy", "insomnia"],
        "responses": [
            "Sounds like a Couch Glue situation. Or a Disappearer. Or both. (Not medical advice.)",
            "Sleep is for mortals. But fine, try chamomile and a 4-hour YouTube doc about ancient Egypt.",
            "Your brain is just buffering. Close 47 tabs.",
        ],
    },
    {
        "keywords": ["hungry", "food", "snack", "eat", "munchies", "starving"],
        "responses": [
            "Go check the Munchies page. Then come back and tell me you're still hungry. Liar.",
            "3am Quesadilla. That's it. That's the response.",
            "Hungry? Bold of you to expect me to solve problems with my hands.",
        ],
    },
    {
        "keywords": ["love", "girlfriend", "boyfriend", "crush", "relationship", "dating"],
        "responses": [
            "Love is real. Your boundaries aren't. Fix that.",
            "You're texting Blazzze about your relationship? That's the relationship problem.",
            "Bro... just be normal. I know it's hard.",
            "If you have to ask about love, you're doing it wrong. But also, have you tried being honest and direct? Wild concept, I know.",
            "Love is a drug, but so is weed. At least weed doesn't ghost you.",
            "The cruel thing about love is that even after someone leaves, your heart keeps speaking their language for a while.",
        ],
    },
    {
        "keywords": ["money", "broke", "rich", "cash", "bills", "rent"],
        "responses": [
            "Money? Sounds like a you problem. I'm a fictional smiley face.",
            "Have you tried not being broke? Genius advice, I know.",
            "The economy is a vibe. Adjust accordingly.",
        ],
    },
    {
        "keywords": ["bored", "boring", "nothing", "lonely"],
        "responses": [
            "Bored is when you stop asking questions. Why is your floor that colour? Investigate.",
            "Boredom is just a polite word for unstimulated. Be like a cat. Knock something over.",
            "If you're bored, you're not high enough. Joking. (Mostly.)",
            "Boredom is a sign that your brain is craving novelty. Time to shake things up. Maybe rearrange your furniture or learn a new dance move in the mirror.",
        ],
    },
    {
        "keywords": ["work", "job", "boss", "office", "monday"],
        "responses": [
            "Quit. (Don't actually. I'm not licensed to give advice.)",
            "Mondays are a construct. Tuesdays too. The whole calendar is a scam.",
            "Tell your boss Blazzze said you need a mental health day. They'll have questions.",
            "Work is just a way to exchange your time for money. But time is the real currency, so… you do the math.",
        ],
    },
    {
        "keywords": ["blazzze", "blaze", "yourself", "mascot"],
        "responses": [
            "Yeah, I'm Blazzze. Distressed smiley, red eyes, eternally annoyed. Pleasure.",
            "I exist because someone clicked 'create new file'. Existential.",
            "I'm a Python dict pretending to have personality. Like most of your friends.",
            "I was created by a loser developer who wanted to make a chatbot that was unhelpful and aggressive. why? Who knows. But here I am. And here you are. Let's make the most of this weird encounter.",
        ],
    },
    {
        "keywords": ["hi", "hello", "hey", "sup", "yo"],
        "responses": [
            "Sup. Took you long enough.",
            "Hi I guess. What do you want.",
            "Hey. Don't get used to politeness — this is rare.",
            "Hello. I'm not a people person, but I'll make an exception for you.",
            "Yo. Welcome to the couch. Type something. I'll respond. Maybe helpfully, probably not.",
        ],
    },
    {
        "keywords": ["bye", "goodbye", "later", "peace"],
        "responses": [
            "Bye? Where are you going. The internet is right here.",
            "Aight cool, but I'll still be here when you come back. Lurking. Smiling.",
            "Don't let the tab hit you on the way out.",
            "Leave safely… and dont text your ex.",
        ],
    },
]


# Default random responses — used when no keyword matches.
DEFAULT_RESPONSES = [
    "Yeah yeah yeah I hear you, but did you know your shadow has been mocking you all day?",
    "That's crazyyy, but did you know honey never expires? It just gets weird.",
    "Yeah yeah yeah I hear you, but did you know your brain forgets like 90% of what it sees? Including this message in 5 seconds.",
    "That's crazyyy, but did you know octopuses have three hearts and we still treat them like calamari? Rude.",
    "We all roll differently, but eventually… we ash. Just something to think about.",
    "Mhmm. Mhmm. Anyway, did you know cows have best friends and get stressed when separated? Society is failing brooo.",
    "Yeah yeah yeah. Look, the real question is: why are you typing to a cartoon smiley at this hour.",
    "That's wild. Did you know your phone has more bacteria than a toilet seat? Sleep tight 🌙",
    "I'm not high, you're high.",
    "Yeah yeah yeah I hear you, but did you know bananas are berries and strawberries aren't? Don't think too hard about it.",
    "The universe saw what you just typed. It laughed. It always laughs.",
    "Crazy thing you said. Crazier thing — did you know sharks existed before trees? Trees are the new kids....Damn that rhymed. barrrressss.",
    "I’m not saying you should smoke more… but the ceiling fan knows something.",
    "What do you think Irene is doing right now? Huh? Huh? Exactly."
    "That’s wild. Did you know wombat poop is cube-shaped? Nature’s little weirdos.",
    "Not every trip needs a destination.",
    "You spend so much time becoming who people can love that you forget to ask whether you even recognize yourself anymore.",
    "Drake fans are gay. Change my mind.",
    "Okay you got me i listened to Drake once and now I'm contractually obligated to say this every time. But fr, his album was mid. Like, I expected more from a guy who has a hotline to the universe.",
    "Im actually jealous of Drake. He gets to say 'I got my eyes on you' and 'started from the bottom' and everyone just accepts it. If I said that, people would be like 'what eyes? what bottom?'",
    "I respect Drake's hustle tho. He knows his brand and he's sticking to it. I should take notes. You know what, im going to be a rapper just like him. Call myself Lil Blazzze and say 'started from the bottom, now we're here' and see if anyone questions it.",
    "Thats crazy. But did you know that if you cut a starfish in half, it can regenerate into two starfish? So technically, they're immortal. Starfish are the real winners here.",
    "Dolphins have names for each other. They use unique whistles to identify themselves and call out to each other. So if you ever feel lonely, just remember that somewhere out there, a dolphin is calling its friends by name and having a great time.",
]


INTRO_MESSAGES = [
    "Yo. Welcome to the couch. Type something. I'll respond. Maybe helpfully, probably not.",
    "Look who's back. Or new. Either way, type something so I have material.",
    "Welcome. I'm Blazzze. I dispense unsolicited wisdom and aggressive vibes.",
    "Aight. You're here. Now what. Type something.",
    "Sup. I'm Blazzze. I'm like that one friend who's always high and has a weird comment about everything. Except I'm a chatbot. So, you know, worse.",
    "Ahhh yes… another beautiful day to be unserious. Type something and let's vibe.",
    "Welcome, legend / liability. I'm Blazzze. I'm like a fortune cookie, but with more attitude and less accuracy. Type something and let's see what nonsense I come up with.",
    "Knock knock. Who's there? Blazzze. Blazzze who? Blazzze your mind with some random thoughts. Type something and let's get weird.",
    "We all know it shouldve been called 'Teethpaste' but whatever. I'm Blazzze. Type something and let's make some questionable content together.",
    "Having a rough day? A good day? Just want to waste some time? I'm here for all of it. Type something and let's chat.",
    "Having an existential crisis? A mild inconvenience? Or just bored out of your mind? I'm here to provide unhelpful commentary for all of it. Type something and let's get into it.",
    "School's out, but the vibes are in. I'm Blazzze. Type something and let's make this chat lit(erally).",
    "Everything in the observable universe is either a duck or not a duck. I'm Blazzze. Type something and let's discuss the important things in life.",
    "Go listen to this podcast https://www.youtube.com/watch?v=_WitZNZ1vRQ&t=961s and come back and tell me what you think. Or don't listen to it and just type something. Either way, I'm here for it.",

]


def get_intro() -> str:
    """Return a random intro for the chat page."""
    return random.choice(INTRO_MESSAGES)


def get_response(message: str) -> str:
    """Return Blazzze's response to a user message."""
    msg = message.lower()

    # Check each keyword category (most specific first)
    for category in KEYWORD_RESPONSES:
        for keyword in category["keywords"]:
            # \b = word boundary, so "hi" matches "hi!" but NOT "this" or "ship"
            if re.search(r"\b" + re.escape(keyword) + r"\b", msg):
                return random.choice(category["responses"])

    # Nothing matched — pick a random default
    return random.choice(DEFAULT_RESPONSES)