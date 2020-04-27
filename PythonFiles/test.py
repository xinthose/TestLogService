#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import log

logger = log.setup_custom_logger('root')

logger.info("Hello World")

################################# Notes ################################
# logger.info("")		// Detailed information, typically of interest only when diagnosing problems.
# logger.debug("")		// Confirmation that things are working as expected.
# logger.warning("")	// An indication that something unexpected happened, or indicative of some problem in the near future
# logger.error("")		// Due to a more serious problem, the software has not been able to perform some function.
# logger.critical("")	// A serious error, indicating that the program itself may be unable to continue running.
