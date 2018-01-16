# Copyright (c) 2018, Matias Fontanini
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# The views and conclusions contained in the software and documentation are those
# of the authors and should not be interpreted as representing official policies,
# either expressed or implied, of the FreeBSD Project.

from terminaltables import AsciiTable
from terminaltables.width_and_alignment import max_dimensions
import datetime
import dateparser
import sys
from dateutil.tz import tzutc, tzlocal

def format_float(number_format, number):
    # Format it, then remove right zeroes and remove dot if all decimals are gone
    return number_format.format(number).rstrip('0').rstrip('.')

def make_price_string(base_currency_price, base_currency_code, currency_price):
    return '{0} {1} (${2})'.format(
        format_float('{0:.8f}', base_currency_price),
        base_currency_code,
        format_float('{0:.4f}', currency_price * base_currency_price)
    )

def make_table_rows(title, table_data):
    table = AsciiTable(table_data, title)
    dimensions = max_dimensions(table.table_data, table.padding_left, table.padding_right)[:3]
    output = table.gen_table(*dimensions)
    return map(lambda i: ''.join(i), list(output))

def datetime_from_utc_time(str_time):
    return dateparser.parse(str_time).replace(tzinfo=tzutc()).astimezone(tz=tzlocal())

def show_operation_dialog():
    running = True
    while running:
        sys.stdout.write('Type "yes" or "no" to confirm or decline the operation: ')
        sys.stdout.flush()
        try:
            line = raw_input()
        except (KeyboardInterrupt, EOFError):
            return False
        if line == 'yes':
            return True
        elif line == 'no':
            return False
        else:
            print 'Invalid response'

