#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import matplotlib.pyplot as plt
import os

from bitstring import BitArray

def file_path(string):
	if os.path.isfile(string):
		return string
	else:
		raise OSError(string)

i2s_left_data = []
i2s_right_data = []
i2s_data_count = 0

parser = argparse.ArgumentParser(description="Plot waveform from I2S values.")

parser.add_argument("input", metavar="<input file>", type=file_path, help="Path to the input file")
parser.add_argument("-o", "--output", metavar="<output file>", type=str, help="Path to the output file (.png or .pdf)", required=False)
parser.add_argument("-d", "--datawidth", metavar="<datawidth>", type=int, default=16, help="Number of bits per sample", required=False)
parser.add_argument("-c", "--channels", metavar="<channels>", type=int, choices=[1, 2], default=2, help="Number of channels", required=False)
parser.add_argument("-s", "--swap-channels", type=bool, action=argparse.BooleanOptionalAction, default=False, help="Swap left and right channels", required=False)

args = parser.parse_args()

if (args.datawidth < 1) or (args.datawidth > 32):
	print("Invalid number of bits per sample!")
	exit(0)

in_file = open(args.input, "r")
all_lines = in_file.readlines()

for line in all_lines:
	i2s_data_count = i2s_data_count + 1

	try:
		hex_str = line.strip()[-8:]
		bin_str = bin(int(hex_str, 16))[2:].zfill(args.datawidth)
		data_num = BitArray(bin=bin_str).int
	except Exception as e:
		continue

	if i2s_data_count % 2 == 1:
		i2s_left_data.append(data_num) if not args.swap_channels else i2s_right_data.append(data_num)
	else:
		i2s_right_data.append(data_num) if not args.swap_channels else i2s_left_data.append(data_num)

if args.channels == 2:
	fig, ax = plt.subplots(2)
	fig.tight_layout(pad=3.0)

	ax[0].set_title("Left Channel")
	ax[0].set(ylabel="Value", xlabel="Sample")
	ax[0].plot(i2s_left_data)

	ax[1].set_title("Right Channel")
	ax[1].set(ylabel="Value", xlabel="Sample")
	ax[1].plot(i2s_right_data)

else:
	plt.title("Waveform")
	plt.ylabel("Value")
	plt.xlabel("Sample")
	plt.plot(i2s_left_data)

if args.output:
	plt.savefig(args.output)
else:
	plt.show()