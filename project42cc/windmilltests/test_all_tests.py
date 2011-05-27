# Generated by the windmill services transformer
from windmill.authoring import WindmillTestClient


def test_recordingSuite1():
    client = WindmillTestClient(__name__)

    client.open(url=u'/admin/')
    client.waits.forPageLoad(timeout=u'8000')
    client.type(text=u'admin', id=u'id_username')
    client.type(text=u'admin', id=u'id_password')
    client.click(value=u'Log in')
    client.waits.forPageLoad(timeout=u'20000')
    client.open(url=u'/')
    client.waits.forPageLoad(timeout=u'8000')
    client.waits.forElement(link=u'Edit (admin)', timeout=u'8000')
    client.click(link=u'Edit (admin)')
    client.waits.forPageLoad(timeout=u'20000')
    client.waits.forElement(timeout=u'8000', name=u'_save')
    client.click(name=u'_save')
    client.waits.forPageLoad(timeout=u'20000')

    client.open(url=u'/admin/logout/')
    client.waits.forPageLoad(timeout=u'8000')


def test_recordingSuite2():
    client = WindmillTestClient(__name__)

    client.open(url=u'/admin/logout/')
    client.waits.forPageLoad(timeout=u'8000')
    client.open(url=u'/admin/')
    client.waits.forPageLoad(timeout=u'8000')
    client.type(text=u'admin', id=u'id_username')
    client.type(text=u'admin', id=u'id_password')
    client.click(value=u'Log in')
    client.waits.forPageLoad(timeout=u'20000')
    client.open(url=u'/')
    client.waits.forPageLoad(timeout=u'8000')
    client.waits.forElement(link=u'Edit Person', timeout=u'8000')
    client.click(link=u'Edit Person')
    client.waits.forPageLoad(timeout=u'20000')
    client.waits.forElement(timeout=u'8000', id=u'id_bio')
    client.click(id=u'id_bio')
    client.type(text=u'NewName', id=u'id_name')
    client.click(value=u'Save person')
    client.asserts.assertValue(validator=u'NewName', id=u'id_name')
    client.click(id=u'id_name')
    client.type(text=u'', id=u'id_name')
    client.click(value=u'Save person')
    client.click(xpath=u"//span[@id='id_name_errror']/ul/li")
