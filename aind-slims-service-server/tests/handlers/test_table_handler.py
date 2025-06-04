"""Tests methods in table_handler module."""

import unittest
from datetime import datetime, timezone
from unittest.mock import MagicMock, patch

import networkx as nx

from aind_slims_service_server.handlers.table_handler import (
    SlimsTableHandler,
    parse_date,
    parse_html,
)


# TODO: Add more tests
class TestSlimsTableHandler(unittest.TestCase):
    """Test class for SlimsTableHandler"""

    def test_get_date_criteria_start_no_end(self):
        """Tests get_date_criteria when start date and no end date"""
        criteria = SlimsTableHandler._get_date_criteria(
            start_date=datetime(2025, 1, 1, tzinfo=timezone.utc),
            end_date=None,
            field_name="xprn_createdOn",
        )
        expected_criteria = {
            "fieldName": "xprn_createdOn",
            "operator": "greaterOrEqual",
            "value": 1735689600000,
        }
        self.assertEqual(expected_criteria, criteria.to_dict())

    def test_get_date_criteria_no_start_with_end(self):
        """Tests get_date_criteria when end date and no start date"""
        criteria = SlimsTableHandler._get_date_criteria(
            end_date=datetime(2025, 1, 1, tzinfo=timezone.utc),
            start_date=None,
            field_name="xprn_createdOn",
        )
        expected_criteria = {
            "fieldName": "xprn_createdOn",
            "operator": "lessOrEqual",
            "value": 1735689600000,
        }
        self.assertEqual(expected_criteria, criteria.to_dict())

    def test_get_date_criteria_start_with_end(self):
        """Tests get_date_criteria when end date and start date"""
        criteria = SlimsTableHandler._get_date_criteria(
            end_date=datetime(2025, 1, 1, tzinfo=timezone.utc),
            start_date=datetime(2025, 2, 1, tzinfo=timezone.utc),
            field_name="xprn_createdOn",
        )
        expected_criteria = {
            "operator": "and",
            "criteria": [
                {
                    "fieldName": "xprn_createdOn",
                    "operator": "greaterOrEqual",
                    "value": 1738368000000,
                },
                {
                    "fieldName": "xprn_createdOn",
                    "operator": "lessOrEqual",
                    "value": 1735689600000,
                },
            ],
        }

        self.assertEqual(expected_criteria, criteria.to_dict())

    def test_parse_html(self):
        """Tests parse html"""
        protocol_html = '<a href="https://example.com">Example</a>'
        output = parse_html(protocol_html)
        self.assertEqual("https://example.com", output)

    def test_parse_malformed_html(self):
        """Tests parse_html when malformed string"""
        protocol_html = "<a>Missing Href</a>"
        output = parse_html(protocol_html)
        self.assertIsNone(output)

    def test_parse_non_html(self):
        """Tests parse_html when regular string passed in"""
        protocol_html = "Not in HTML"
        output = parse_html(protocol_html)
        self.assertEqual("Not in HTML", output)

    def test_parse_html_none(self):
        """Tests parse_html when None passed in"""
        output = parse_html(None)
        self.assertIsNone(output)

    @patch("logging.warning")
    def test_parse_error(self, mock_log_warn: MagicMock):
        """Tests parse_html when regular string passed in"""

        output = parse_html(123)  # type: ignore
        self.assertIsNone(output)
        mock_log_warn.assert_called_once()

    def test_parse_date(self):
        """Tests _parse_date method"""

        dt = parse_date(date_str="2025-02-10T00:00:00")
        expected_dt = datetime(2025, 2, 10)
        self.assertEqual(expected_dt, dt)

    def test_parse_date_none(self):
        """Tests _parse_date method when input is None"""

        dt = parse_date(date_str=None)
        self.assertIsNone(dt)

    def test_parse_date_invalid(self):
        """Tests _parse_date method when input is invalid"""

        with self.assertRaises(ValueError):
            parse_date(date_str="not-a-date")

    def test_update_graph_with_foreign_table_pk_list(self):
        """Tests _update_graph with foreign table
        and a list of foreign keys."""
        g = nx.DiGraph()
        foreign_table = "Foreign"
        input_table = "Input"
        input_table_cols = ["some_fk"]
        foreign_table_col = "some_fk_pk"

        foreign_row1 = MagicMock()
        foreign_row1.pk.return_value = 1
        foreign_row1.table_name.return_value = foreign_table
        foreign_row2 = MagicMock()
        foreign_row2.pk.return_value = 2
        foreign_row2.table_name.return_value = foreign_table

        foreign_rows = [foreign_row1, foreign_row2]

        for row in foreign_rows:
            g.add_node(f"{foreign_table}.{row.pk()}")

        input_row = MagicMock()
        input_row.table_name.return_value = input_table
        input_row.pk.return_value = 100

        with patch(
            "aind_slims_service_server.handlers.table_handler."
            "get_attr_or_none",
            return_value=[1, 2],
        ):
            SlimsTableHandler._update_graph(
                foreign_table=foreign_table,
                foreign_rows=foreign_rows,
                foreign_table_col=foreign_table_col,
                input_table=input_table,
                input_rows=[input_row],
                input_table_cols=input_table_cols,
                g=g,
            )
            self.assertIn(
                (f"{input_table}.100", f"{foreign_table}.1"), g.edges
            )
            self.assertIn(
                (f"{input_table}.100", f"{foreign_table}.2"), g.edges
            )

    def test_get_rows_from_foreign_table_no_foreign_keys(self):
        """Test when no foreign keys are present."""
        mock_session = MagicMock()
        handler = SlimsTableHandler(session=mock_session)
        input_row = MagicMock()
        with patch(
            "aind_slims_service_server.handlers.table_handler."
            "get_attr_or_none",
            return_value=None,
        ):
            result = handler.get_rows_from_foreign_table(
                input_table="Input",
                input_rows=[input_row],
                foreign_table="Foreign",
                foreign_table_col="some_fk_pk",
                input_table_cols=["some_fk"],
            )
            self.assertEqual(result, [])
            mock_session.fetch.assert_not_called()

    def test_get_rows_from_foreign_table_with_extra_criteria(self):
        """Tests conjunction when extra_criteria is provided."""
        mock_session = MagicMock()
        handler = SlimsTableHandler(session=mock_session)
        input_row = MagicMock()
        with patch(
            "aind_slims_service_server.handlers.table_handler."
            "get_attr_or_none",
            return_value=42,
        ):
            extra_criteria = MagicMock(name="extra_criteria")
            handler.get_rows_from_foreign_table(
                input_table="Input",
                input_rows=[input_row],
                foreign_table="Foreign",
                foreign_table_col="some_fk_pk",
                input_table_cols=["some_fk"],
                extra_criteria=extra_criteria,
            )
            mock_session.fetch.assert_called_once()
            _, kwargs = mock_session.fetch.call_args
            criteria = kwargs.get("criteria")
            from slims.criteria import Junction

            self.assertIsInstance(criteria, Junction)

    def test_get_rows_from_foreign_table_key_values_list(self):
        """Test get_rows_from_foreign_table where key_values is a list"""

        mock_session = MagicMock()
        handler = SlimsTableHandler(session=mock_session)
        input_row = MagicMock()
        with patch(
            "aind_slims_service_server.handlers.table_handler."
            "get_attr_or_none",
            side_effect=[[1, 2], [1, 2]],
        ):
            handler.get_rows_from_foreign_table(
                input_table="Input",
                input_rows=[input_row],
                foreign_table="Foreign",
                foreign_table_col="some_fk_pk",
                input_table_cols=["some_fk"],
            )
            mock_session.fetch.assert_called_once()
            _, kwargs = mock_session.fetch.call_args
            criteria = kwargs.get("criteria")
            self.assertTrue(
                hasattr(criteria, "to_dict")
                and set(criteria.to_dict().get("value", [])) == {1, 2}
            )


if __name__ == "__main__":
    unittest.main()
