#!/usr/bin/env python3
import logging
import math
import pathlib
import random
import sys
import threading
import time

import ltr559
import RPi.GPIO as GPIO
import ST7735
from fonts.ttf import RobotoMedium as UserFont
from PIL import Image, ImageDraw, ImageFont

import yaml
from grow import Piezo
from grow.moisture import Moisture
from grow.pump import Pump

BUTTONS = [5, 6, 16, 24]
LABELS = ["A", "B", "X", "Y"]

WATER_LEVEL = 26

def main():

	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(BUTTONS, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	GPIO.setup(WATER_LEVEL, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	while True:

		water_level_input = GPIO.input(WATER_LEVEL)
		print(water_level_input)
		time.sleep(1)

if __name__ == "__main__":
    main()
