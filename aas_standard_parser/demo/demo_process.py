import logging

import aas_standard_parser.aimc_parser as aimc_parser
from aas_standard_parser.utils import create_submodel_from_file

logger = logging.getLogger(__name__)


def start() -> None:
    logger.info("Demo process started.")

    aimc_submodel = create_submodel_from_file("tests/test_data/aimc_submodel.json")

    root = aimc_parser.get_mapping_configuration_root_element(aimc_submodel)

    logger.info("Demo process finished.")
