import requests

ba_url = "https://p9fwi1d77e.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday"

def test_next_birthday_endpoint():
    test_val_inputs()
    test_missing_parameters()
    test_invalid_dateofbirth_format()
    test_invalid_unit()
    test_future_dateofbirth()
    test_today_dateofbirth()
    test_yesterday_dateofbirth()
    test_tomorrow_dateofbirth()
    test_leap_year_dateofbirth()
    test_non_leap_year_dateofbirth()

def test_val_inputs():
    exp_results = {
        "hour": "2616 hours left",
        "day": "109 days left",
        "week": "15 weeks left",
        "month": "3 months left"
    }
    for unit, expected_result in exp_results.items():
        url = f"{ba_url}?dateofbirth=1990-10-30&unit={unit}"
        response = requests.get(url)
        assert response.status_code == 200
        assert response.json()["message"] == expected_result

def test_missing_parameters():
    url = ba_url
    response = requests.get(url)
    assert response.status_code == 400
    assert response.json()["message"] == "dateofbirth and unit parameters are required"

    url = f"{ba_url}?dateofbirth=1990-10-30"
    response = requests.get(url)
    assert response.status_code == 400
    assert response.json()["message"] == "unit parameter is required"

    url = f"{ba_url}?unit=hour"
    response = requests.get(url)
    assert response.status_code == 400
    assert response.json()["message"] == "dateofbirth parameter is required"

def test_invalid_dateofbirth_format():
    url = f"{ba_url}?dateofbirth=Oct%2030,%201990&unit=hour"
    response = requests.get(url)
    assert response.status_code == 400
    assert response.json()["message"] == "dateofbirth parameter should be in YYYY-MM-DD format"

    url = f"{ba_url}?dateofbirth=1990/10/30&unit=hour"
    response = requests.get(url)
    assert response.status_code == 400
    assert response.json()["message"] == "dateofbirth parameter should be in YYYY-MM-DD format"

    url = f"{ba_url}?dateofbirth=30-10-1990&unit=hour"
    response = requests.get(url)
    assert response.status_code == 400
    assert response.json()["message"] == "dateofbirth parameter should be in YYYY-MM-DD format"

    url = f"{ba_url}?dateofbirth=1990-13-30&unit=hour"
    response = requests.get(url)
    assert response.status_code == 400
    assert response.json()["message"] == "Invalid dateofbirth parameter"

    url = f"{ba_url}?dateofbirth=1990-10-32&unit=hour"
    response = requests.get(url)
    assert response.status_code == 400
    assert response.json()["message"] == "Invalid dateofbirth parameter"

def test_invalid_unit():
    url = f"{ba_url}?dateofbirth=1990-10-30&unit=year"
    response = requests.get(url)
    assert response.status_code == 400
    assert response.json()["message"] == "Invalid unit parameter"

    url = f"{ba_url}?dateofbirth=1990-10-30&unit=minute"
    response = requests.get(url)
    assert response.status
