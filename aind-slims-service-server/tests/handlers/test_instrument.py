"""Tests methods in instrument handler module"""

from unittest.mock import MagicMock, patch
import pytest
from aind_slims_service_server.handlers.instrument import (
    InstrumentSessionHandler,
)


@pytest.fixture
def reference_data_record_with_attachment(load_json, form_record):
    """Fixture for a ReferenceDataRecord with an attachment."""
    return [
        form_record(j)
        for j in load_json(
            "reference_data_record.json", subdir="aind_instruments"
        )
    ]


class TestInstrumentSessionHandler:
    """Test class for InstrumentSessionHandler"""

    @patch("slims.slims.Slims")
    @patch.object(InstrumentSessionHandler, "_get_attachment")
    def test_get_instrument_data(
        self,
        mock_get_attachment,
        mock_slims: MagicMock,
        test_slims_instrument,
        reference_data_record_with_attachment,
    ):
        """Tests get_instrument_data method"""
        handler = InstrumentSessionHandler(session=mock_slims)
        instrument_name = "SmartSPIM2-2"
        mock_slims.fetch.return_value = reference_data_record_with_attachment
        mock_response = MagicMock()
        mock_response.json.return_value = test_slims_instrument
        mock_get_attachment.return_value = mock_response

        result = handler.get_instrument_data(instrument_name)
        assert result == test_slims_instrument

    @patch("slims.slims.Slims")
    def test_get_instrument_data_empty_input(self, mock_slims: MagicMock):
        """Test ValueError when input_id is empty"""
        handler = InstrumentSessionHandler(session=mock_slims)
        with pytest.raises(ValueError):
            handler.get_instrument_data("")

    @patch("slims.slims.Slims")
    def test_get_instrument_data_no_records(self, mock_slims: MagicMock):
        """Test None returned when no ReferenceDataRecord found"""
        handler = InstrumentSessionHandler(session=mock_slims)
        mock_slims.fetch.return_value = []
        result = handler.get_instrument_data("NonExistentInstrument")
        assert result is None

    @patch("slims.slims.Slims")
    @patch.object(InstrumentSessionHandler, "_get_attachment")
    @patch("aind_slims_service_server.handlers.instrument.get_attr_or_none")
    def test_get_instrument_data_no_attachment(
        self,
        mock_get_attr,
        mock_get_attachment,
        mock_slims: MagicMock,
        reference_data_record_with_attachment,
    ):
        """Test None returned when attachment column is missing"""
        handler = InstrumentSessionHandler(session=mock_slims)
        mock_slims.fetch.return_value = reference_data_record_with_attachment
        mock_get_attr.return_value = None
        result = handler.get_instrument_data("SmartSPIM2-2")
        assert result is None
        mock_get_attachment.assert_not_called()

    @patch("slims.slims.Slims")
    @patch.object(InstrumentSessionHandler, "_get_attachment")
    def test_get_instrument_data_partial_match(
        self,
        mock_get_attachment,
        mock_slims: MagicMock,
        test_slims_instrument,
        reference_data_record_with_attachment,
    ):
        """Test partial_match=True uses contains criteria"""
        handler = InstrumentSessionHandler(session=mock_slims)
        mock_slims.fetch.return_value = reference_data_record_with_attachment
        mock_response = MagicMock()
        mock_response.json.return_value = test_slims_instrument
        mock_get_attachment.return_value = mock_response

        result = handler.get_instrument_data("SmartSPIM2", partial_match=True)
        assert result == test_slims_instrument

    @patch("slims.slims.Slims")
    @patch.object(InstrumentSessionHandler, "_get_attachment")
    def test_get_instrument_data_multiple_records(
        self,
        mock_get_attachment,
        mock_slims: MagicMock,
        test_slims_instrument,
        reference_data_record_with_attachment,
    ):
        """Test multiple ReferenceDataRecords found (should use the first)"""
        handler = InstrumentSessionHandler(session=mock_slims)
        mock_slims.fetch.return_value = (
            reference_data_record_with_attachment * 2
        )
        mock_response = MagicMock()
        mock_response.json.return_value = test_slims_instrument
        mock_get_attachment.return_value = mock_response

        result = handler.get_instrument_data("SmartSPIM2-2")
        assert result == test_slims_instrument


if __name__ == "__main__":
    pytest.main([__file__])
