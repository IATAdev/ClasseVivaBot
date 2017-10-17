# This file is a part of ClasseVivaBot, a Telegram bot for Classe Viva electronic register
#
# Copyright (c) 2016-2017 The ClasseVivaBot Authors (see AUTHORS)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Rename this file to config.py

from datetime import datetime as dt

# -- Redis configuration --
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = None

# -- PostgreSQL configuration --
POSTGRESQL_DBNAME = ''
POSTGRESQL_HOST = 'localhost'
POSTGRESQL_PORT = 5432
POSTGRESQL_USER = ''
POSTGRESQL_PASSWORD = ''

# -- Telegram configuration --
BOT_TOKEN = ''

# -- ClasseViva configuration --
SCHOOL_YEAR_BEGINNING = dt(year=2017, month=9, day=1)
SCHOOL_YEAR_END = dt(year=2018, month=6, day=30)
