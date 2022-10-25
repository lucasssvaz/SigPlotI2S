# SigPlotI2S
Script to plot audio waves from I2S generated from sigrok/PulseView. This was created to provide visual aid when debugging I2S drivers.

## Requirements
- Python 3.9+
- [matplotlib](https://pypi.org/project/matplotlib/)
- [bitstring](https://pypi.org/project/bitstring/)

## Usage

```
python SigPlotI2S.py [Options] <input file>

Required arguments:
  <input file>          Path to the input file

Options:
  -h, --help            Show help message
  -o <output file>, --output <output file>
                        Path to the output file (.png or .pdf). Save image into a file
                        instead of opening a pop-up.
  -d <datawidth>, --datawidth <datawidth>
                        Number of bits per sample (default: 16)
  -c <channels>, --channels <channels>
                        Number of channels (default: 2)
  -s, --swap-channels, --no-swap-channels
                        Swap left and right channels (default: False)
```

## Example

In this example we will use a 44.1kHz, 16-bit, stereo WAV file containing a sine wave and, from the
I2S data recorded, generate the resulting waveform of the output audio.

1. Scan the I2S bus to be analysed;

![1](https://user-images.githubusercontent.com/32426024/197887339-5ffd3890-6d82-4c67-8d36-618bcceb0231.png)

2. Add and configure I2S decoder;

![2](https://user-images.githubusercontent.com/32426024/197887734-78943c8c-9cb2-4cf1-9e7d-68e4c376147f.png)

3. Export I2S annotation as `sinewave.txt`;

![3](https://user-images.githubusercontent.com/32426024/197888740-b53aa91c-5e21-45b6-a5b2-82637390f921.png)

4. Run SigPlotI2S to convert and plot the I2S samples;

```
python SigPlotI2S.py -d 16 -c 2 sinewave.txt
```

5. Get the resulting waveform.

![5](https://user-images.githubusercontent.com/32426024/197889906-2634f7d0-aa2b-4420-9390-1c87af7480bd.png)
