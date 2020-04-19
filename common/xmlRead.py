# -*- coding: utf-8 -*-
"""
by: 老屋
"""

from xml.dom import minidom
import os

currentDir = __file__
father = os.path.dirname(os.path.dirname(currentDir))
caseDataPath = father + "/testData/caseData.xml"


def xml_read(first_node, second_node):
    file = minidom.parse(caseDataPath)
    one_node = file.getElementsByTagName(first_node)[0]
    two_node = one_node.getElementsByTagName(second_node)[0].childNodes[0].nodeValue
    return two_node
