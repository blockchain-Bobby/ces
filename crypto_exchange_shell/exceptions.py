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

class BaseException(Exception):
    pass

class ConfigException(BaseException):
    pass

class KeyMissingConfigException(ConfigException):
    def __init__(self, missing):
        ConfigException.__init__(self, '"{0}" key not found in config file')

class UnknownCurrencyException(BaseException):
    def __init__(self, currency_code):
        BaseException.__init__(self, 'Unknown currency {0}'.format(currency_code))
        self.currency_code = currency_code

class ExchangeAPIException(BaseException):
    pass

class InvalidArgumentException(BaseException):
    pass

class CommandExecutionException(BaseException):
    pass

class UnknownCommandException(CommandExecutionException):
    def __init__(self, command):
        CommandExecutionException.__init__(self, 'Unknown command "{0}"'.format(command))
        self.command = command

class ParameterCountException(CommandExecutionException):
    def __init__(self, command, expected):
        CommandExecutionException.__init__(self, 'Expected {0} parameters'.format(expected))
        self.command = command
        self.expected = expected
