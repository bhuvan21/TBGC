from lxml import etree

xmlschema_doc = etree.parse("schema.xsd")
xmlschema = etree.XMLSchema(xmlschema_doc)

# checks the game.xml file against schema.xsd returning a bool of validity
def validate_game():
    try:
        doc = etree.parse("game.xml")
    except etree.XMLSyntaxError as err:
        print(err)
        return False

    try:
        xmlschema.assertValid(doc)
        return True

    except etree.DocumentInvalid as err:
        print(err)
        return False
