"""Module for fetching rig and instrument data from SLIMS"""

from slims.criteria import equals, contains

from aind_slims_service_server.handlers.table_handler import (
    SlimsTableHandler,
    get_attr_or_none,
)


#TODO: figure out if we want to support multiple responses (partial match)
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

        # Fetch ReferenceDataRecord(s)
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

        # Handle no results
        if not rdrc:
            return None

        # Handle multiple results
        if len(rdrc) > 1:
            # You could return all, or raise an error, or pick the first
            # Here, let's return a list of available names/ids
            return {
                "error": "Multiple instruments found",
                "matches": [
                    {
                        "pk": r.get("pk") or r.get("rdrc_pk"),
                        "name": r.get("rdrc_name"),
                        "uniqueIdentifier": r.get("rdrc_uniqueIdentifier"),
                    }
                    for r in rdrc
                ],
            }

        # Handle single result
        record = rdrc[0]
        att_pk = get_attr_or_none(record, "rdrc_cf_instrumentJsonAttachment")
        if not att_pk:
            return {
                "error": "Instrument JSON attachment not found for this record.",
                "record": record,
            }

        response = self._get_attachment(pk=att_pk)
        if hasattr(response, "status_code"):
            # TODO: check if we need to do this check for status code? 
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 401:
                raise ValueError("Unauthorized access to SLIMS")
            else:
                raise ValueError(f"Error fetching attachment: {response.status_code}")
        else:
            # If _get_attachment returns a dict directly
            return response

