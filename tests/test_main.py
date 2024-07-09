from echo.main import main

import pytest


class TestMain:

    @pytest.mark.timeout(3)
    def test_client_send_messages_and_is_broadcast_to_other_clients(self):
        pass
