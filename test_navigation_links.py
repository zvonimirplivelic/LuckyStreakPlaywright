from playwright.sync_api import Page, expect

"""
    This script goes through each link in the navigation bar on the Lucky Streak Live website
    It's made to check if Contact Us button works on each page. When user is on career page 
"""   
    
def test_successful_qa_job_application(page: Page) -> None:
    
    page.goto("https://luckystreaklive.com/")
    page.wait_for_url("https://luckystreaklive.com/")

    ## Allow cookies
    page.get_by_role("button", name="Allow all").click()
    
    ## Navigating to contact us form in the footer from each link in the navigation
    ## Home Page
    page.get_by_role("button", name="Contact Us").click()
    
    ## Live Blackjack Software
    page.get_by_role("link", name="Live Blackjack Software").click()
    page.wait_for_url("https://luckystreaklive.com/live-blackjack-software/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Live Baccarat Software
    page.get_by_role("link", name="Live Baccarat Software").click()
    page.wait_for_url("https://luckystreaklive.com/live-baccarat-software/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Live Roulette Software
    page.get_by_role("link", name="Live Roulette Software").click()
    page.wait_for_url("https://luckystreaklive.com/live-roulette-software/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Live Auto Roulette Software
    page.get_by_role("link", name="Live Auto Roulette Software").click()
    page.wait_for_url("https://luckystreaklive.com/live-auto-roulette-software/")
    page.get_by_role("button", name="Contact Us").click()

    ## Dual Play Roulette Software
    page.get_by_role("link", name="Dual Play Roulette Software").click()
    page.wait_for_url("https://luckystreaklive.com/dual-play-roulette-software/")    
    page.get_by_role("button", name="Contact Us").click()

    ## Online Live Casino API
    page.get_by_role("link", name="Online Live Casino API").click()
    page.wait_for_url("https://luckystreaklive.com/online-live-casino-api-integration/")
    page.get_by_role("button", name="Contact Us").click()

    ## Live Blackjack API
    page.get_by_role("link", name="Live Blackjack API", exact=True).click()
    page.wait_for_url("https://luckystreaklive.com/live-blackjack-api/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Live Baccarat API
    page.get_by_role("link", name="Live Baccarat API", exact=True).click()
    page.wait_for_url("https://luckystreaklive.com/live-baccarat-api/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Live Roulette API
    page.get_by_role("link", name="Live Roulette API", exact=True).click()
    page.wait_for_url("https://luckystreaklive.com/live-roulette-api/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Slots Software API
    page.get_by_role("link", name="Slots Software API", exact=True).click()
    page.wait_for_url("https://luckystreaklive.com/slots-software-api/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Jackpot Games Software API
    page.get_by_role("link", name="Jackpot Games Software API", exact=True).click()
    page.wait_for_url("https://luckystreaklive.com/jackpot-games-software-api/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Table Games Software API
    page.get_by_role("link", name="Table Games Software API", exact=True).click()
    page.wait_for_url("https://luckystreaklive.com/table-games-software-api/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Crash Games Software API
    page.get_by_role("link", name="Crash Games Software API", exact=True).click()
    page.wait_for_url("https://luckystreaklive.com/crash-games-software-api/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Live Casino Games Software
    page.get_by_role("link", name="Live Casino Games Software").click()
    page.wait_for_url("https://luckystreaklive.com/online-live-casino-software/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## LuckyConnect Content
    page.get_by_role("link", name="LuckyConnect Content").click()
    page.wait_for_url("https://luckystreaklive.com/luckyconnect/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Casino Content Aggregation
    page.get_by_role("link", name="Casino Content Aggregation", exact=True).click()
    page.wait_for_url("https://luckystreaklive.com/casino-content-aggregation/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Sweepstakes Casino Software Provider
    page.get_by_role("link", name="Sweepstakes Casino Software Provider").click()
    page.wait_for_url("https://luckystreaklive.com/sweepstakes-casinos-software/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Social Casino Software
    page.get_by_role("link", name="Social Casino Software").click()
    page.wait_for_url("https://luckystreaklive.com/social-casino-games-api-solutions/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Casino Marketing Software Tools
    page.get_by_role("link", name="Casino Marketing Software Tools").click()
    page.wait_for_url("https://luckystreaklive.com/casino-marketing-software-tools/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## LuckyDedicated Branded
    page.get_by_role("link", name="LuckyDedicated Branded").click()
    page.wait_for_url("https://luckystreaklive.com/luckydedicated/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Lucky Land-Based Streaming
    page.get_by_role("link", name="Lucky Land-Based Streaming").click()
    page.wait_for_url("https://luckystreaklive.com/landbased/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Online Casino Customisation
    page.get_by_role("link", name="Online Casino Customisation").click()
    page.wait_for_url("https://luckystreaklive.com/online-casino-customisation/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Casino Marketing Software
    page.get_by_role("link", name="Casino Marketing Software").click()
    page.wait_for_url("https://luckystreaklive.com/casino-marketing-software-tools/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Casino Management Tools
    page.locator("#sm-17332989085946428-8").get_by_role("link", name="Casino Management Tools").click()
    page.wait_for_url("https://luckystreaklive.com/management-tools/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Online Casino Customer Support
    page.get_by_role("link", name="Online Casino Customer Support").click()
    page.wait_for_url("https://luckystreaklive.com/online-casino-customer-support/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Our iGaming Mission
    page.get_by_role("link", name="Our iGaming Mission").click()
    page.wait_for_url("https://luckystreaklive.com/company/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Live Casino Studio
    page.get_by_role("link", name="Live Casino Studio", exact=True).click()
    page.wait_for_url("https://luckystreaklive.com/our-studio/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Online Gambling Technology
    page.get_by_role("link", name="Online Gambling Technology").click()
    page.wait_for_url("https://luckystreaklive.com/technology/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Resources, News and Blog 
    page.get_by_role("link", name="Resources, News and Blog ").click()
    page.wait_for_url("https://luckystreaklive.com/resources/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Online Casino Blog
    page.get_by_role("link", name="Online Casino Blog").click()
    page.wait_for_url("https://luckystreaklive.com/category/blog/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## LuckyStreak Live Casino News
    page.get_by_role("link", name="LuckyStreak Live Casino News").click()
    page.wait_for_url("https://luckystreaklive.com/news/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Case studies
    page.get_by_role("link", name="Case studies").click()
    page.wait_for_url("https://luckystreaklive.com/category/case-studies/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Case studies
    page.get_by_role("link", name="iGaming Media Partners").click()
    page.wait_for_url("https://luckystreaklive.com/media-partners/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Careers
    page.get_by_role("link", name="Careers").click()
    page.wait_for_url("https://luckystreaklive.com/career/")
    page.get_by_role("button", name="Contact Us").click()
    
    ## Navigation Logo
    page.locator("#header-block-wrap #log").get_by_role("link").click()
    page.wait_for_url("https://luckystreaklive.com/")
    page.get_by_role("button", name="Contact Us").click()
    
