"""Module for fetching rig and instrument data from SLIMS"""

from slims.criteria import equals, contains

from aind_slims_service_server.handlers.table_handler import (
    SlimsTableHandler,
)
import logging


class InstrumentSessionHandler(SlimsTableHandler):
    """Class to handle getting instrument info from SLIMS."""

    def get_instrument_data(
        self,
        input_id: str,
        partial_match: bool = False,
    ):
        """
        Get Instrument data from SLIMS.
        Raises
        ------
        ValueError
          The input_id cannot be an empty string.
        """
        if not input_id:
            raise ValueError("input_id must not be empty!")

        if partial_match:
            rdrc = self.session.fetch(
                table="ReferenceDataRecord",
                criteria=contains("rdrc_name", input_id),
            )
        else:
            rdrc = self.session.fetch(
                table="ReferenceDataRecord",
                criteria=equals("rdrc_name", input_id),
            )
        if not rdrc:
            return None

        # TODO: Handle the case where multiple records are found
        logging.info(
            f"Found {len(rdrc)} ReferenceDataRecord(s) for {input_id}"
        )
        attm_pk = self.get_attr_or_none(
            rdrc[0], "rdrc_cf_instrumentJsonAttachment"
        )
        if not attm_pk:
            logging.warning(
                f"No attachment found for ReferenceDataRecord with {input_id}"
            )
            return None
        response = self._get_attachment(pk=attm_pk)
        return response.json()
