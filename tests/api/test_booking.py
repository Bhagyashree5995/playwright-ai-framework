def test_create_booking_returns_id_and_saved_data(booker, sample_booking):
    response = booker.create_booking(sample_booking)
    assert response.status_code == 200
    body = response.json()
    assert "bookingid" in body
    assert body["booking"]["firstname"] == sample_booking["firstname"]
    assert body["booking"]["totalprice"] == sample_booking["totalprice"]


def test_created_booking_can_be_read_back(booker, sample_booking):
    booking_id = booker.create_booking(sample_booking).json()["bookingid"]

    response = booker.get_booking(booking_id)

    assert response.status_code == 200
    saved = response.json()
    assert saved["lastname"] == sample_booking["lastname"]
    assert saved["bookingdates"]["checkin"] == sample_booking["bookingdates"]["checkin"]
    assert saved["depositpaid"] is True


def test_update_booking_changes_stored_values(booker, sample_booking, token):
    booking_id = booker.create_booking(sample_booking).json()["bookingid"]
    updated = dict(sample_booking, totalprice=500, additionalneeds="Late checkout")

    response = booker.update_booking(booking_id, updated, token)

    assert response.status_code == 200
    saved = booker.get_booking(booking_id).json()
    assert saved["totalprice"] == 500
    assert saved["additionalneeds"] == "Late checkout"


def test_update_without_token_is_rejected(booker, sample_booking):
    booking_id = booker.create_booking(sample_booking).json()["bookingid"]
    updated = dict(sample_booking, totalprice=999)

    response = booker.update_booking(booking_id, updated, token="")

    assert response.status_code == 403
    saved = booker.get_booking(booking_id).json()
    assert saved["totalprice"] == sample_booking["totalprice"]


def test_deleted_booking_is_gone(booker, sample_booking, token):
    booking_id = booker.create_booking(sample_booking).json()["bookingid"]

    delete_response = booker.delete_booking(booking_id, token)

    assert delete_response.status_code == 201
    assert booker.get_booking(booking_id).status_code == 404


def test_unknown_booking_returns_404(booker):
    assert booker.get_booking(99999999).status_code == 404