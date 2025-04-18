import discord
import feedparser
import asyncio
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')

TOKEN = os.getenv("DISCORD_TOKEN")
CYBER_CHANNEL_ID = int(os.getenv("CYBER_CHANNEL_ID"))
TECH_CHANNEL_ID = int(os.getenv("TECH_CHANNEL_ID"))
GEO_CHANNEL_ID = int(os.getenv("GEO_CHANNEL_ID"))
CRYPTO_CHANNEL_ID = int(os.getenv("CRYPTO_CHANNEL_ID"))
FOREX_CHANNEL_ID = int(os.getenv("FOREX_CHANNEL_ID"))
STOCK_CHANNEL_ID = int(os.getenv("STOCK_CHANNEL_ID"))
DOC_CYBER_CHANNEL_ID = int(os.getenv("DOC_CYBER_CHANNEL_ID"))
WRITE_UP_HTB = int(os.getenv("WRITE_UP_HTB"))


RSS_FEEDS = {
    "CyberSécurité": {
        "feeds": [
            "https://www.cert.ssi.gouv.fr/feed/",
            "https://feeds.feedburner.com/TheHackersNews",
            "https://www.bleepingcomputer.com/feed/",
            "https://www.zataz.com/feed/",
            "https://www.zataz.com/category/fuite-de-donnees/"
        ],
        "channel_id": int(os.getenv("CYBER_CHANNEL_ID"))
    },
    "Technologie / Informatique": {
        "feeds": [
            "https://www.lemondeinformatique.fr/flux-rss/thematique/securite/",
            "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"
        ],
        "channel_id": int(os.getenv("TECH_CHANNEL_ID"))
    },
    "Géopolitique": {
        "feeds": [
            "https://www.france24.com/fr/rss",
            "https://www.lemonde.fr/international/rss_full.xml"
        ],
        "channel_id": int(os.getenv("GEO_CHANNEL_ID"))
    },
    "Cryptomonnaies": {
        "feeds": [
            "https://www.coindesk.com/arc/outboundfeeds/rss/",
            "https://cryptopotato.com/feed/",
            "https://bitcoinmagazine.com/.rss/full"
        ],
        "channel_id": int(os.getenv("CRYPTO_CHANNEL_ID"))
    },
    "Forex": {
        "feeds": [
            "https://www.dailyfx.com/feeds/market-news",
            "https://www.fxstreet.com/rss/news"
        ],
        "channel_id": int(os.getenv("FOREX_CHANNEL_ID"))
    },
    "Actions": {
        "feeds": [
            "https://www.boursorama.com/rss/actualites/",
            "https://www.lesechos.fr/rss/finance-marches.xml",
            "https://www.marketwatch.com/rss/topstories"
        ],
        "channel_id": int(os.getenv("STOCK_CHANNEL_ID"))
    },
    "Documentation Cyber": {  
        "feeds": [
            "https://www.linkedin.com/company/hackingarticles/posts/?feedView=documents",
            "https://ticodevv.github.io/",
            "https://beta.hackndo.com/",
            "https://thecybersecguru.com/all-posts/",
            "https://vuln.dev/"
        ],
        "channel_id": int(os.getenv("DOC_CYBER_CHANNEL_ID"))  
    },
    "Writes-ups htb": {  
        "feeds": [
            "https://medium.com/write-ups-hackthebox"
        ],
        "channel_id": int(os.getenv("WRITE_UP_HTB"))  
    }
}


intents = discord.Intents.default()
client = discord.Client(intents=intents)

posted_links = set()

async def fetch_and_post_news():
    await client.wait_until_ready()

    while not client.is_closed():
        for category, data in RSS_FEEDS.items():
            channel = client.get_channel(data["channel_id"])

            if channel is None:
                print(f"Aucun salons trouvé pour {category}")
                continue

            for feed_url in data["feeds"]:
                    feed = feedparser.parse(feed_url)
                    
                    for entry in feed.entries[:3]: 
                        if entry.link not in posted_links:
                            posted_links.add(entry.link)
                            message = f"**{entry.title}**\n{entry.link}"
                            print(f"[{category}] Articles ajouté: {entry.title}")
                            
                            await channel.send(message)

        await asyncio.sleep(360)  
@client.event
async def on_ready():
    print(f"Bot connecté  {client.user}")
    client.loop.create_task(fetch_and_post_news())

client.run(TOKEN)
