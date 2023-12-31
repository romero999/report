import pytest
import datetime
from report1 import DateConverter

@pytest.mark.parametrize(('string', 'expected'), [
    ('平成元年13月16日', '日付データを入力ください!'),
    ('平成元年12月32日', '日付データを入力ください!'),
    ('平成30年13月32日', '日付データを入力ください!'),
    ('R3.13.30', '日付データを入力ください!'),
    ('R3.12.32', '日付データを入力ください!'),
    ('R3.13.32', '日付データを入力ください!'),
    ('日付じゃないよ！', '日付データを入力ください!'),
    ('2022/222/2', '日付データを入力ください!'),
    ('令和0年１２月３日', datetime.date(2018,12,3)),
    ('１９９５．２．４', datetime.date(1995,2,4)),
    ('１９９５．2.4', datetime.date(1995,2,4)),
    ('h1.8.3', datetime.date(1989,8,3))
])
def test_general(string, expected):
    date_converter = DateConverter()
    assert date_converter.main(string) == expected

@pytest.mark.parametrize(('string', 'expected'), [
    ('平成5年2月6日', datetime.date(1993,2,6)),
    ('平和5年2月6日', '日付データを入力ください!'),
    ('平成1年2月6日', datetime.date(1989,2,6)),
    ('平成元年2月6日', datetime.date(1989,2,6)),
    ('平成元年12月16日', datetime.date(1989,12,16)),
    ('平成元年12月6日', datetime.date(1989,12,6)),
    ('平成元年2月16日', datetime.date(1989,2,16)),
    ('明治元年2月6日', datetime.date(1868,2,6)),
    ('大正元年2月6日', datetime.date(1912,2,6)),
    ('昭和元年2月6日', datetime.date(1926,2,6)),
    ('令和元年2月6日', datetime.date(2019,2,6)),
    ('令和５年１２月３日', datetime.date(2023,12,3)),
    ('R3/08/30', datetime.date(2021,8,30)),
    ('R3/08.30', datetime.date(2021,8,30)),
    ('R3.08.30', datetime.date(2021,8,30)),
    ('R3.8.3', datetime.date(2021,8,3)),
    ('H1/08/30', datetime.date(1989,8,30)),    
    ('S1/08/30', datetime.date(1926,8,30)),
    ('T1/08/30', datetime.date(1912,8,30)),
    ('M1/08/30', datetime.date(1868,8,30))
])
def test_japan_era(string, expected):
    date_converter = DateConverter()
    assert date_converter.main(string) == expected

@pytest.mark.parametrize(('string', 'expected'), [
    ('199524', '日付データを入力ください!'),
    ('1978908', '日付データを入力ください!'),
    ('20222222', '日付データを入力ください!'),
    ('20080203', datetime.date(2008,2,3)),
    ('2008/12/23', datetime.date(2008,12,23)),
    ('2008/12.23', datetime.date(2008,12,23)),
    ('2008.12/23', datetime.date(2008,12,23)),
    ('2008.12.23', datetime.date(2008,12,23)),
    ('2008/02/03', datetime.date(2008,2,3)),
    ('2008/12/03', datetime.date(2008,12,3)),
    ('2008/2/3', datetime.date(2008,2,3)),
    ('2022/12/2', datetime.date(2022,12,2)),
    ('2022/2/12', datetime.date(2022,2,12)),
])
def test_mark_date(string, expected):
    date_converter = DateConverter()
    assert date_converter.main(string) == expected
