"""Module for fetching rig and instrument data from SLIMS"""

import logging
from typing import Any, Dict, List

from slims.criteria import contains, equals

from aind_slims_service_server.handlers.table_handler import (
    SlimsTableHandler,
)


class InstrumentSessionHandler(SlimsTableHandler):
    """Class to handle getting instrument info from SLIMS."""

    def get_instrument_data(
        self,
        input_id: str,
        partial_match: bool = False,
    ) -> List[Dict[str, Any]]:
        """
        Get Instrument data from SLIMS.

        Parameters
        ----------
        input_id : str
        partial_match : bool

        Returns
        -------
        List[Dict[str, Any]]

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

        logging.info(
            f"Found {len(rdrc)} ReferenceDataRecord(s) for {input_id}"
        )
        attm_pks = [
            self.get_attr_or_none(r, "rdrc_cf_instrumentJsonAttachment")
            for r in rdrc
            if self.get_attr_or_none(r, "rdrc_cf_instrumentJsonAttachment")
            is not None
        ]
        attachments = []
        for attm_pk in attm_pks:
            response = self._get_attachment(pk=attm_pk)
            attachments.append(response.json())
        return attachments
