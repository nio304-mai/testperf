
from collections import namedtuple
import re


class MemberdefTagParser:
    def __init__(self, memberdef_tag):
        self.__memberdef_tag = memberdef_tag
        self.__function = namedtuple('Function', ['name',
                                                  'prototype',
                                                  'arguments_names',
                                                  'arguments_types',
                                                  'point_type'
                                                  ])
        self.__function.name = ''
        self.__function.prototype = ''
        self.__function.arguments_names = []
        self.__function.arguments_types = []
        self.__function.point_type = ''

    def parse_memberdef_tag(self):
        self.parse_name()
        self.parse_prototype()
        self.parse_arguments_types_and_names()
        self.identify_point_type()

    def get_function(self):
        return self.__function

    def identify_point_type(self):
        for arg_type in self.__function.arguments_types:
            if arg_type.find('f') != -1 or arg_type.find('double') != -1:
                self.__function.point_type = 'floating'
                return
        self.__function.point_type = 'fixed'

    def parse_prototype(self):
        return_type_and_name_func = self.__memberdef_tag.childNodes[3].firstChild.data
        arguments_func = self.__memberdef_tag.childNodes[5].firstChild.data
        self.__function.prototype = '{}{};'.format(return_type_and_name_func, arguments_func)

    def parse_name(self):
        return_type_and_name_func = self.__memberdef_tag.childNodes[3].firstChild.data
        name_func = return_type_and_name_func.split(' ')[1]
        self.__function.name = name_func.strip()

    def parse_arguments_types_and_names(self):
        arguments_func = self.__memberdef_tag.childNodes[5].firstChild.data
        arguments_func = re.sub(r'const ', '', arguments_func)
        arguments_func = arguments_func.lstrip('(').rstrip(')')
        if arguments_func:
            for arg in arguments_func.split(','):
                try:
                    equal_symbol_pos = arg.index('=')
                    arg = arg[:equal_symbol_pos]
                except ValueError:
                    pass
                arg = arg.lstrip()
                if '*' in arg:
                    self.__function.arguments_types.append(arg.split('*')[0] + '*')
                    self.__function.arguments_names.append(arg.split('*')[1])
                else:
                    self.__function.arguments_types.append(arg.split(' ')[0])
                    self.__function.arguments_names.append(arg.split(' ')[1])

if __name__ == '__main__':
    pass