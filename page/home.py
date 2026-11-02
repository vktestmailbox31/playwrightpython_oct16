from playwright.sync_api import Page, expect
class HomePage:
    def __init__(self , page):
        self.search = page.get_by_role("link", name="Amazon.in")
        self.searchbox = page.get_by_role("searchbox", name="Search Amazon.in")
        self.cart = page.get_by_role("link", name="items in cart")
        
    def validateSearchedVisibilities(self):
        expect(self.search).to_be_visible()
        
    def ValidatingSearchBox(self):    
        expect(self.searchbox).to_be_visible()
        
    def validateCartTextVisibiblities(self):    
        expect(self.cart).to_be_visible()    