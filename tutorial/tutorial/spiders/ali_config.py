#
class duvetClass:
    size = [['Twin',69,89],['Full',79,129],['Queen',89,139]]
    body = """<h3><strong>Description:</strong></h3>
            <p>1)This Item&nbsp;Is Customize Style,The Producing Time Is 7-10 Days.</p>
            <p>2)100% Microfiber,Soft and Comfortable.</p>
            <p>3)Environmental Dyeing,Never Lose Color.</p>
            <p>4)2017 Newest Design,German Shepherd,Fashion and Personality.</p>
            <p>5)3pcs Total Have 1pc Duvet Cover/2pcs Pillowcases(Twin Size 1pc),Not Have Any Quilt/Comforter/Filling.</p>
            <p>6)Free Shipping By DHL,Fedex,UPS Express,Safe and Fast.Pls Don't Forget Give Us Your Phone No.</p>
            <div></div>
            <h3><strong>Before You Take Order,Pls Check The Size Chart Below:</strong></h3>
            <p>Twin Size(2 pcs)</p>
            <p>1 pc duvet cover:172*218cm(68*86inch)<br>1 pc pillowcase:50*75cm(19*29inch)<br><br>Full Size(3 pcs)<br>1 pc duvet cover:200*229cm(79*90inch)<br>2 pcs pillowcase:50*75cm(19*29inch)<br><br>Queen Size(3 pcs)<br>1 pc duvet cover:228*228cm(90*90inch)<br>2 pcs pillowcase:50*75cm(19*29inch)<br><br>King Size(3 pcs)<br>1 pc duvet cover:259*229cm(102*90inch)<br>2 pcs pillowcase:50*75cm(19*29inch)</p>
            <p><span>California King Size(3 pcs)</span><br><span>1 pc duvet cover:264*239cm(104*94inch)</span><br><span>2 pcs pillowcase:50*75cm(19*29inch)</span></p>
            <h3>
            <br>Specification:</h3>
            <p><br>1)100% Microfiber Polyester,soft,comfortable and durable.<br>2)Reactive Dying,Non-Fading,Non-Pilling, Non-Wrinkle.<br>3)Fabric Density:130x70,Fabric Count:50x50<br>4)Best choice for your unique bedroom</p>
            <h3>
            <br><br><span>Care:</span>
            </h3>
            <p><br><span>Machine Wash in Cold, Dry on Low.</span></p> """
    taglist = "duvet cover, bedding sets"
    productType = "duvet cover, bedding sets"
    # start from this url 
    url = ['https://www.aliexpress.com/store/product/BeddingOutlet-Watercolor-Dreamcatcher-Bedding-Set-King-Blue-Bedclothes-for-Adult-Kids-Luxury-Chinese-Style-Quilt-Cover/1160570_32831117756.html']
    urls = ['https://beddingoutlet.aliexpress.com/store/group/Galaxy-Sea-Duvet-Cover-Set/1160570_512585898.html']

    # list keyword filter from title 
    replaceList = ['BeddingOutlet','Chinese','King ', 'Blue ','for Adult Kids ','3 Pcs']
    spiltImage = "#j-image-thumb-list img::attr(src)"
    title = "h1.product-name::text"
    
    # get list page 
    pageDetail = "ul.items-list div.pic"
    nextPage = "a.ui-pagination-next::attr(href)"

class jesmine():
    size = [['Twin',69,89],['Full',79,129],['Queen',89,139]]
    body = """<h3><strong>Description:</strong></h3>
            <p>1)This Item&nbsp;Is Customize Style,The Producing Time Is 7-10 Days.</p>
            <p>2)100% Microfiber,Soft and Comfortable.</p>
            <p>3)Environmental Dyeing,Never Lose Color.</p>
            <p>4)2017 Newest Design,German Shepherd,Fashion and Personality.</p>
            <p>5)3pcs Total Have 1pc Duvet Cover/2pcs Pillowcases(Twin Size 1pc),Not Have Any Quilt/Comforter/Filling.</p>
            <p>6)Free Shipping By DHL,Fedex,UPS Express,Safe and Fast.Pls Don't Forget Give Us Your Phone No.</p>
            <div></div>
            <h3><strong>Before You Take Order,Pls Check The Size Chart Below:</strong></h3>
            <p>Twin Size(2 pcs)</p>
            <p>1 pc duvet cover:172*218cm(68*86inch)<br>1 pc pillowcase:50*75cm(19*29inch)<br><br>Full Size(3 pcs)<br>1 pc duvet cover:200*229cm(79*90inch)<br>2 pcs pillowcase:50*75cm(19*29inch)<br><br>Queen Size(3 pcs)<br>1 pc duvet cover:228*228cm(90*90inch)<br>2 pcs pillowcase:50*75cm(19*29inch)<br><br>King Size(3 pcs)<br>1 pc duvet cover:259*229cm(102*90inch)<br>2 pcs pillowcase:50*75cm(19*29inch)</p>
            <p><span>California King Size(3 pcs)</span><br><span>1 pc duvet cover:264*239cm(104*94inch)</span><br><span>2 pcs pillowcase:50*75cm(19*29inch)</span></p>
            <h3>
            <br>Specification:</h3>
            <p><br>1)100% Microfiber Polyester,soft,comfortable and durable.<br>2)Reactive Dying,Non-Fading,Non-Pilling, Non-Wrinkle.<br>3)Fabric Density:130x70,Fabric Count:50x50<br>4)Best choice for your unique bedroom</p>
            <h3>
            <br><br><span>Care:</span>
            </h3>
            <p><br><span>Machine Wash in Cold, Dry on Low.</span></p> """
    taglist = "duvet cover, bedding sets"
    productType = "duvet cover, bedding sets"
    # start from this url 
    url = ['https://www.aliexpress.com/store/product/BeddingOutlet-Watercolor-Dreamcatcher-Bedding-Set-King-Blue-Bedclothes-for-Adult-Kids-Luxury-Chinese-Style-Quilt-Cover/1160570_32831117756.html']
    urls = ['https://beddingoutlet.aliexpress.com/store/group/Galaxy-Sea-Duvet-Cover-Set/1160570_512585898.html']

    # list keyword filter from title 
    replaceList = ['BeddingOutlet','Chinese','King ', 'Blue ','for Adult Kids ','3 Pcs']
    spiltImage = "#j-image-thumb-list img::attr(src)"
    title = "h1.product-name::text"
    
    # get list page 
    pageDetail = "ul.items-list div.pic"
    nextPage = "li.next a::attr(href)"
