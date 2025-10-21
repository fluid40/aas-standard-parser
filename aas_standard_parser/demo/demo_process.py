import logging

from aas_standard_parser.utils import create_submodel_from_file

logger = logging.getLogger(__name__)


def start() -> None:
    logger.info("Demo process started.")

    aid_submodel = create_submodel_from_file("tests/test_data/aimc_submodel.json")

    logger.info("Demo process finished.")
