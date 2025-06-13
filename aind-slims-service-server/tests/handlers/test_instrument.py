"""Tests methods in instrument handler module"""

from unittest.mock import MagicMock, patch

import pytest

from aind_slims_service_server.handlers.instrument import (
    InstrumentSessionHandler,
)


class TestInstrumentSessionHandler:
    """Test class for InstrumentSessionHandler"""

    def test_get_instrument_data(
        self,
        mock_get_instrument_data: MagicMock,
    ):
        """Tests get_instrument_data method"""
        handler = InstrumentSessionHandler(
            session=MagicMock(fetch=mock_get_instrument_data)
        )
        instrument_name = "SmartSPIM2-2"
        instrument_data = handler.get_instrument_data(instrument_name)
        assert instrument_data[0]["instrument_id"] == instrument_name

    def test_get_instrument_data_empty_input(self):
        """Test ValueError when input_id is empty"""
        handler = InstrumentSessionHandler(
            session=MagicMock(fetch=MagicMock())
        )
        with pytest.raises(ValueError):
            handler.get_instrument_data("")

    def test_get_instrument_data_no_records(self):
        """Test None returned when no ReferenceDataRecord found"""
        mock_session = MagicMock()
        mock_session.fetch.return_value = []
        handler = InstrumentSessionHandler(session=mock_session)
        result = handler.get_instrument_data("NonExistentInstrument")
        assert result == []

    def test_get_instrument_data_partial_match(
        self,
        mock_get_instrument_data: MagicMock,
    ):
        """Test partial_match=True uses contains criteria"""
        handler = InstrumentSessionHandler(
            session=MagicMock(fetch=mock_get_instrument_data)
        )
        partial_instrument_name = "SmartSPIM"
        instrument_data = handler.get_instrument_data(
            partial_instrument_name, partial_match=True
        )
        assert instrument_data[0]["instrument_id"] == "SmartSPIM2-2"


if __name__ == "__main__":
    pytest.main([__file__])
