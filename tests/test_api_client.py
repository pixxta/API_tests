import allure


@allure.title("Get object")
def test_get_object(api_client, test_object):
    """
    Test function to GET object by id.

    This function tests the functionality of retrieving an object from the API by id.
    It checks the following:
    - The status code of the response is 200.
    - The ID of the received object matches the expected ID.
    """
    try:
        response = api_client.get_object(test_object['id'])
        object_data = response.json()

        with allure.step("Check GET object response status code"):
            assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        with allure.step("Check GET response id"):
            assert object_data['id'] == test_object['id'], "Received object id doesn't match the expected id"
    except Exception as e:
        allure.attach(str(e), name='Exception')
        raise e


@allure.title("Get objects by ids")
def test_get_objects(api_client, test_object):
    """
    Test function to GET objects by ids [1, 2, 3].

    This function tests the functionality of retrieving an objects from the API by ids.
    It checks the following:
    - The status code of the response is 200.
    - The ids of the received objects matches the expected ids.
    """
    try:
        response = api_client.get_objects(ids=[1, 2, 3])
        object_data = response.json()

        with allure.step("Check GET objects response status code"):
            assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        with allure.step("Check GET first object response id"):
            assert object_data[0]['id'] == '1', "Received object id doesn't match the expected id"
        with allure.step("Check GET second object response id"):
            assert object_data[1]['id'] == '2', "Received object id doesn't match the expected id"
        with allure.step("Check GET second object response id"):
            assert object_data[2]['id'] == '3', "Received object id doesn't match the expected id"
    except Exception as e:
        allure.attach(str(e), name='Exception')
        raise e


@allure.title("Create object")
def test_create_object(api_client):
    """
    Test function to CREATE/POST object and checking with GET by id.

    This function checks the functionality of object creation.
    It checks the following:
    - The status code of the response is 200.
    - The name of the created object matches the expected name.
    """
    try:
        obj = {
            "name": "Xiaomi Poco X3",
            "data": {
                "color": "Dark black",
                "capacity": "256 GB"
            }
        }
        response = api_client.create_object(obj)
        created_object = response.json()

        with allure.step("Check CREATE response status code"):
            assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        with allure.step("Check Create response data name"):
            assert created_object['name'] == 'Xiaomi Poco X3', "Received object name doesn't match the expected name"
    except Exception as e:
        allure.attach(str(e), name='Exception')
        raise e


@allure.title("Update object")
def test_update_object(api_client, test_object):
    """
    Test function to UPDATE/PUT object and checking with GET by id.

    This function checks the functionality of object creation.
    It checks the following:
    - The status code of the response is 200.
    - The name of the updated object matches the expected name.
    """
    try:
        updated_obj = {
            "name": "Xiaomi Poco X4",
            "data": {
                "color": "Dark black",
                "capacity": "256 GB"
            }
        }
        response = api_client.update_object(test_object['id'], updated_obj)
        updated_object = response.json()

        with allure.step("Check CREATE response status code"):
            assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        with allure.step("Check UPDATE response data name"):
            assert updated_object['name'] == 'Xiaomi Poco X4', "Received object name doesn't match the expected name"
    except Exception as e:
        allure.attach(str(e), name='Exception')
        raise e


@allure.title("Delete object")
def test_delete_object(api_client, test_object):
    """
    Test function to DELETE object and checking with GET by id.

    This function checks the functionality of object creation.
    It checks the following:
    - The status code of the response is 200.
    - The status code of the GET by deleted id response is 404.
    """
    try:
        response = api_client.delete_object(test_object['id'])
        with allure.step("Check DELETE response status code"):
            assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response.status_code == 200
        get_response = api_client.get_object(test_object['id'])
        with allure.step("Check GET response status code after deleting object"):
            assert get_response.status_code == 404, f"Unexpected status code: {response.status_code}"
    except Exception as e:
        allure.attach(str(e), name='Exception')
        raise e
