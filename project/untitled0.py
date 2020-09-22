# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 14:53:47 2020

@author: dudnj
"""

#내용 물이 없는 경우에는 <엘리먼트 이름 />
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import ElementTree
def indent(elem, level = 0):
    mytab = '\t'
    i = '\n' + level * mytab

    if len(elem) :
        if not elem.text or not elem.text.strip() :
            elem.text = i + mytab

        if not elem.tail or not elem.tail.strip() :
            elem.tail = i

        for elem in elem :
            indent(elem, level + 1)

        if not elem.tail or not elem.tail.strip() :
            elem.tail = i
    else :
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

note=Element('note')
SubElement(note,'to').text = 'Tove'

SubElement(note,'from').text = 'Jani'
SubElement(note,'heading').text = 'Reminder'
SubElement(note,'body').text = "Don't forget me this weekend!"
indent(note)
xmlFile = 'xmlEx_02.xml'
ElementTree(note).write(xmlFile,encoding= 'utf-8')

