"""Module for fetching rig and instrument data from SLIMS"""

import logging
from typing import Any, Dict, List

from slims.criteria import conjunction, contains, equals, greater_than_or_equal

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

        attachment_criteria = conjunction().add(
            greater_than_or_equal("attachmentCount", 1)
        )
        if partial_match:
            criteria = attachment_criteria.add(contains("rdrc_name", input_id))
        else:
            criteria = attachment_criteria.add(equals("rdrc_name", input_id))

        rdrc = self.session.fetch(
            table="ReferenceDataRecord",
            criteria=criteria,
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
