
from xml.dom import minidom
from xml.parsers import expat


class DoxyXmlParser:
    def __init__(self, path_to_doxy_xml):
        try:
            self.__opened_doxy_xml = minidom.parse(path_to_doxy_xml)
        except expat.ExpatError:
            raise SyntaxError

        group_name_tag = self.__opened_doxy_xml.getElementsByTagName('compoundname')
        self.__compoundname_tag = group_name_tag[0].firstChild.data
        self.__testperf_tag = self.__opened_doxy_xml.getElementsByTagName('testperf')
        self.__memberdef_tag = self.__opened_doxy_xml.getElementsByTagName('memberdef')

    def get_compoundname_tag(self):
        return self.__compoundname_tag

    def get_memberdef_tag(self):
        return self.__memberdef_tag

    def get_testperf_tag(self):
        return self.__testperf_tag
