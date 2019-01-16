class hoodieClass:
    size = [['HOODIE',42.5,79.5],['SWEATSHIRT',36.5,69.5],['T-SHIRT',27.5,44.5],['ZIP',45.5,79.5],['TANK',26.5,39.5],['KID',24.5,39.5]]
    taglist = "ALL OVER PRINT"
    productType = "ALL OVER PRINT"
    # start from this url 
    url = ['https://vio-store.com/collections/all-over-print-shirts/products/anime-ghibli-my-neighbor-totoro-sleep-in-the-green-forest-3d-all-over-print-tshirt-hoodie-sweater-tank']
    urls = ['https://vio-store.com/collections/all-over-print-shirts']

    # list keyword filter from title 
    replaceList = ['BeddingOutlet','Chinese','King ', 'Blue ','for Adult Kids ','3 Pcs','Dropship','King ','Queen ','Size ', 'Full Queen',]
    spiltImage = "#j-image-thumb-list img::attr(src)"
    title = "//title/text()" 
    #heading = "//h1[@itemprop="name"]/text()"
    
    
    # get list page 
    pageDetail = "ul.items-list div.pic"
    nextPage = "a.ui-pagination-next::attr(href)"

    #body list 
    body1 = """<div>
            <h3><strong><span>UPGRADE YOUR LIFESTYLE WITH TRENDY BEDCOVER</span></strong></h3>
            <p><span>Trends change a lot with the passage of time. That’s why we make sure to bring you the trendiest fashionable bed covers.</span></p>
            <h3><strong><span>SLEEP IN AVANT-GARDE STYLE</span></strong></h3>
            <p><span>This bedding set has the most fascinating catchy look, with colourful artwork that leaves everyone staring in awe. Let your bed cover remind you to <em>laugh, live every moment</em> and <em>love beyond words</em>.</span></p>
            <h3><strong><span>UPDATE YOUR BEDROOM APPEAL</span></strong></h3>
            <p><span>Give your bedroom a supreme trendy look with this bed cover that reflects your stylish and happy-go-lucky lifestyle. Your exclusive tastes can only be satisfied with a unique microfiber bed cover like this one.</span></p>
            <h3><strong><span>MADE WITH 100% PURE AND SUPERIOR FABRIC</span></strong></h3>
            The quality of this bed cover is owed to the use of microfiber material. That’s what makes it not only good-looking, but also comfortable, soft, relaxing, and surprisingly long-lasting. We give 100% guarantee to our customers when it comes to quality and durability. This wrinkle-free and fade-resistant bed cover set is easy to use, easy to care for and easy to wash.
            <div>
                <br />
                <h3><strong><span>BED SET INCLUDES: 1* DUVET COVER 2* PILLOWCASES</span></strong></h3>
            </div>
            </div>"""
    body2 = """<h3><strong><span>SWEET BEDCOVER FOR YOUR SWEET DREAMS</span></strong></h3>
        <p><span>When anyone enters a bedroom, the first thing they notice is the bed. This is precisely why an aesthetic bed cover with gorgeous design is a must.</span></p>
        <h3><strong><span>A BEDCOVER YOU CAN’T TAKE YOUR EYES OFF</span></strong></h3>
        <p><span>With a remarkable cluster of brilliant colours and fancy artwork, this bed set highlights the impression of your bedroom in an exquisite manner. The impressive arrangement of sundry designs in catchy colors and pattern make it a magnificent view for all.</span></p>
        <h3><strong><span>SUPERIOR FABRIC QUALITY THAT YOU DESERVE</span></strong></h3>
        <p>Our premium quality bed covers are made of microfiber, and that’s what makes them special. Microfiber bed covers offer unmatched softness and durability. What makes this bed cover unique from the rest are its qualities of wrinkle and fade resistance. The 1 quilt cover and 2 matching pillowcases, all are made of 100% pure and premier microfiber for luxurious feel. You’ll never want to leave your bed!</p>
        <br />
        <h3><strong><span>BED SET INCLUDES: 1* DUVET COVER 2* PILLOWCASES</span></strong></h3>"""
    body3 = """<h3><strong>FASHIONABLE BED COVERS<span> FOR ULTIMATE COMFORT AND QUALITY</span></strong></h3>
        <p><span>We all place our comfort at top priority, especially in the bedroom. At the close of a hectic daily routine, all we want is to snuggle in our comfortable bed.  Well, your bed can’t be the ultimate relaxation spot without a comfortable bedcover!</span></p>
        <h3><strong><span>LIE DOWN ON LUXURY DUVET</span></strong></h3>
        <p><span>This bed set is made of the most comfortable and soft fabric: microfiber cloth. With 100% satisfaction guarantee, we deliver our customers the finest quality bed covers that will redefine comfort.</span></p>
        <h3><strong><span>EXPERIENCE PREMIUM QUALITY BED COVERS</span></strong></h3>
        <p><span>Other materials make the bedcover sheets irritable after a time of use, but microfiber bed covers are exceptional. No matter how often you use it, it will feel comfy and new every time. Softness and strength come together in microfiber fabric to produce luxurious comfort and tough durability.</span></p>
        <h3><strong><span>USE AGAIN AND AGAIN</span></strong></h3>
        <p>Microfiber fabric worn-out and the colours, print and textile are guaranteed to work longer and remain intact. So, never lose your comfort with this Bohemian bedcover. With tender washing and line dry, you can use this bedcover with ultimate assurance.</p>
        <br />
        <h3><strong><span>BED SET INCLUDES:  1* DUVET COVER 2* PILLOWCASES</span></strong></h3>"""
    body4 = """<div>
            <h3><strong>QUALITY BEDCOVER<span> FOR YOUR BEDROOM.</span></strong></h3>
            <p><span>Are you worried about the quality of bedcovers because of your sensitive skin? The solution is here.</span></p>
            <h3><strong><span>THE BEST BED COVER FOR SENSITIVE SKIN.</span></strong></h3>
            <p><span>Our 100% microfiber bed cover is made of the finest material that caresses your skin with the most gentle and soft touch. Microfiber is the best fabric for sensitive skin which is prone to allergies or skin problems.</span></p>
            <h3><strong><span>ELEGANCE AND EXCELLENCE IN ONE BED COVER.</span></strong></h3>
            <p><span>This bedding set is designed to stand out in terms of aesthetics as well as class. Washing such printed bed covers is usually difficult because machines fade the colours and impair the quality. But, with this high-quality bedcover, you don’t need to worry about because its charm and quality will not fade away.</span></p>
            <h3><strong><span>FEELS GOOD AS NEW, EVERY SINGLE TIME.</span></strong></h3>
            <p><span>Microfiber cloth is specially chosen for our bed covers because it is wrinkle- and fade-resistant with 100% guarantee for enduring use. While other bed covers become rough, dull and threadbare over time, the Bohemian bed cover is threaded to perfection and stays that way for years.</span></p>
            But remember not to use bleach, wash it gently, and let it cool tumble and line dry for the long-lasting usage.</div>
        <div></div>
        <div>
            <h3><strong><span>BED SET INCLUDES:  1* DUVET COVER 2* PILLOWCASES</span></strong></h3>
        </div>"""
    body = [body1,body2,body3,body4]
