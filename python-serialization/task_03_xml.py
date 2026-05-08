#!/usr/bin/env python3
"""import XML"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """take python dictionary and a filename. Serializes dictionary into XML"""
    root = ET.Element("data")
    for key, val in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(val)
    ET.ElementTree(root).write(
        filename, encoding="utf-8",
        xml_declaration=True)
    return True


def deserialize_from_xml(filename):
    """Read xML and deserialize in dictionary"""
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    return dictionary
