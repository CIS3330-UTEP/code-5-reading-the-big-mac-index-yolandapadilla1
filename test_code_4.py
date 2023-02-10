import os,sys
from code_4 import get_big_mac_price_by_year
from code_4 import get_big_mac_price_by_country
from code_4 import get_the_cheapest_big_mac_price_by_year
from code_4 import get_the_most_expensive_big_mac_price_by_year

def check_if_file_exists():
    try:
        exists = os.path.exists("code_4.py")
        assert exists == True
    except:
        sys.exit()

def test_big_mac_price_by_year():
    check_if_file_exists

def test_big_mac_price_by_country():
    check_if_file_exists

def test_the_cheapest_big_mac_price_by_year():
    check_if_file_exists
    
def test_the_most_expensive_big_mac_price_by_year():
    check_if_file_exists

