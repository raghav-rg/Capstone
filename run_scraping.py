from scraping.investing_com import get_pair
from scraping.fx_calendar import get_fx_calendar
from scraping.reuters_com import reuters_com

from dateutil import parser


if __name__ == "__main__":

    print("\ninvesting_com()")
    print(get_pair("EUR_USD", "H1"))

    print("\nreuters_com")
    print(reuters_com())

    print("\nfx_calendar")
    print(get_fx_calendar(parser.parse("2024-12-15 00:00:00")))
    
