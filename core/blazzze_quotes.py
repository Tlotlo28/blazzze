"""Blazzze's catalogue of unsolicited wisdom."""
import random


DEFAULT_QUOTES = [
    "People chase altered states because sometimes reality is too loud.",
    "That's crazyyy, but did you know you've been breathing wrong this whole time?",
    "I'm not high, you're high.",
    "Hold up... did you really come here sober? Embarrassing.",
    "There are more possible games of chess than atoms in the observable universe. Yet somehow… you chose this move 😭",
    "Damn, you again? Get a hobby.",
    "You miss 100% of the naps you don’t take.",
    "Plot twist: YOU are the joint.",
    "Fun fact: every atom in your body was forged inside a star that exploded billions of years ago. Which means the universe had to destroy something ancient… just so you could exist. Kinda poetic, right?",
    "Cousin, The strange thing about escape is that eventually… you still meet yourself there.",
    "When is BSM going to release his music?? Asking for a friend.",
    "Brooo, have you listened to Marty Eyezlow?",
    "What's the deal with the weed? It's like, the more you learn about it, the more there is to learn. It's a rabbit hole, but in a fun way. Like, did you know that weed has been used for thousands of years for everything from medicine to textiles to spiritual rituals? It's not just about getting high, it's a whole culture and history.",
    "Maybe people get high because for a little while… the weight of being human feels lighter."
    "Remember kids smoking is not cool, but smokers are. If you see a smoker, compliment their vibe, not their habit.... nah im kidding smoking is cool, stay in school tho.",
    "You know what's wild? The fact that we have a whole plant that can chill you out, make you laugh, and even help with pain. Nature's gift to us, and we're just like 'yeah, let's smoke it'. Gotta respect the simplicity of that.",
    "Did you know that the word 'blaze' originally meant to mark a tree with a bright spot of paint to guide travelers? So in a way, I'm here to guide you through the wilderness of life. Deep, I know.",
    "The real high is the friends we made along the way. But also, this weed is pretty good.",
    "My creator is callled Tlotlo, but i call him click click...",
    "My creator is an alcholic, like really bad. He drinks so much that sometimes I worry about his liver. But hey, at least he's not a snitch, right?",
    "Where is the fun in being a responsible adult if you can't get a little weird sometimes? Embrace the weirdness, my friend. It's where the magic happens.",
    "Dream big. Nap bigger.",
    "Shoot for the stars… and text your crush while you're at it. You never know, maybe they're just as high on you as you are on this weed.",
    "Today is a great day to make weird decisions.",
    "Manifest responsibly.",
    "The edible said ‘trust me’ and that was my first mistake.",
    "I know a guy… it’s me.",
    "Guys, I just realized something. If we’re all made of stardust, does that mean we’re all just space weed? Mind = blown.",
    "We all turn to ash eventually. Might as well laugh first.",
    "Healing is weird because one day the pain becomes a story you tell yourself to feel better. Like, 'remember that time I was heartbroken? Yeah, that sucked, but look how strong I am now!' It's like we're all just trying to rewrite our own narratives to make sense of the chaos.",
    "A wise man once said........I forgot. But it was probably something deep about life and weed. Or maybe it was just a joke. Either way, I'm sure it was profound.",
    "Life is temporary. Snacks are urgent.",
    "Marty Eyelow once said 'Had faith till i heard her music' and honestly same. I had faith in humanity until I heard her music. Now I'm just like... what is this? Why does it exist? Who hurt you, Marty? Who hurt you so bad that you had to make this music? or maybe he was just talking about Faith the slay queen, but either way, I'm shook.",

]


def get_random_quote() -> str:
    """Return a random Blazzze quote."""
    return random.choice(DEFAULT_QUOTES)