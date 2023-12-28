from datetime import datetime


class FourDigitYearConverter:
    regex = "[0-9]{4}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return "%04d" % value


class MyFloatConverter:
    regex = '[+-]?([0-9]*[.])?[0-9]+'

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)


class MyDateConverter:
    regex = "(0?[1-9]|[12]\d|30|31)[^\w\d\r\n:](0?[1-9]|1[0-2])[^\w\d\r\n:](\d{4}|\d{2})"

    def to_python(self, value):
        return datetime.strptime(value, '%d-%m-%Y')

    def to_url(self, value):
        return value.strftime('%d-%m-%Y')


class SplitConvertor:
    regex = r'(\w+,)+\w+'

    def to_python(self, value):
        return value.split(",")

    def to_url(self, value):
        return ",".join(value)



class UpperConvertor:
    regex = r'\w+'

    def to_python(self, value):
        return value.upper()

    def to_url(self, value):
        return value