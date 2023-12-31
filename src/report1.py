import re
import datetime
import unicodedata

class DateConverter:
    def __init__(self) -> None:
        self.input_date = ''
        self.output_date = ''
        self.year = ''
        self.month = ''
        self.day = ''
        self.japan_era_pattern = ''
        self.japan_alphabet_era_pattern = ''
        self.numeric_pattern = ''
        self.mark_pattern = ''
        self.japan_era_date = ''
        self.japan_alphabet_era_date = ''
        self.numeric_pattern = ''
        self.mark_date = ''
        self.japan_era_name = {
            '明治':1868,            
            '大正':1912,            
            '昭和':1926,            
            '平成':1989,            
            '令和':2019,
            'M':1868,
            'T':1912,
            'S':1926,
            'H':1989,
            'R':2019            
        }
        self.era_list = ''
    
    def formatting_date(self, era, year, month, day) -> None:
        if era:
            if year == '元':
                self.year = self.japan_era_name[era]
            else:
                self.year = self.japan_era_name[era] + int(year) - 1
        else:
            self.year = int(year)
        self.month = int(month)
        self.day = int(day)
        try:
            self.output_date = datetime.date(self.year, self.month, self.day) 
        except:
            self.output_date = '日付データを入力ください!'

    def main(self, input:str) -> object:
        self.input_date = unicodedata.normalize('NFKC', input)
        self.input_date = self.input_date.upper()

        self.era_list = '|'.join(self.japan_era_name.keys())
        self.japan_era_pattern = r'(?P<era>{era_list})(?P<year>\d{{1,2}}|元)年(?P<month>\d{{1,2}})月(?P<day>\d{{1,2}})日'.format(era_list=self.era_list)
        self.japan_alphabet_era_pattern = r'(?P<era>{era_list})(?P<year>\d{{1,2}})[./](?P<month>\d{{1,2}})[./](?P<day>\d{{1,2}})'.format(era_list=self.era_list)
        self.numeric_pattern = r'^\d{8}$'
        self.mark_pattern = r'(?P<year>\d{4})[./](?P<month>\d{1,2})[./](?P<day>\d{1,2})'

        self.japan_era_date = re.search(self.japan_era_pattern, self.input_date)
        self.japan_alphabet_era_date = re.search(self.japan_alphabet_era_pattern, self.input_date)
        self.numeric_date = re.search(self.numeric_pattern, self.input_date)
        self.mark_date = re.search(self.mark_pattern, self.input_date)

        if self.japan_era_date:
            self.formatting_date(self.japan_era_date.group('era'), self.japan_era_date.group('year'), self.japan_era_date.group('month'), self.japan_era_date.group('day'))
        elif self.japan_alphabet_era_date:
            self.formatting_date(self.japan_alphabet_era_date.group('era'), self.japan_alphabet_era_date.group('year'), self.japan_alphabet_era_date.group('month'), self.japan_alphabet_era_date.group('day'))
        elif self.numeric_date:
            self.formatting_date('', self.input_date[:4], self.input_date[4:6], self.input_date[6:])
        elif self.mark_date: 
            self.formatting_date('', self.mark_date.group('year'), self.mark_date.group('month'), self.mark_date.group('day'))
        else:
            self.output_date = '日付データを入力ください!'
        
        return self.output_date

# date_converter = DateConverter()
# date_converter.check_date_pattern('1995.12.14')