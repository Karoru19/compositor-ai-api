import os
import subprocess
from shutil import copyfile


TEST_DIR = "test/Nottingham/test/"


def make_ogg(midifile, oggfile):
    subprocess.run(["timidity", midifile, "-Ov", "-o", oggfile])


def compose(files, filename):
    for file in files:
        copyfile(file, f"{TEST_DIR}{os.path.basename(file)}")

    subprocess.run(["python2", "ai_composer/main.py"])

    subprocess.run(
        [
            "python2",
            "ai_composer/rnn_sample.py",
            "--config_file",
            "models/1219_0021/nl_2_hs_50_mc_0p5_dp_0p5_idp_0p8_tb_128.config",
            "--pickle_file",
            "test/nottingham.pickle",
        ]
    )

    make_ogg("best.midi", filename)

    os.remove("best.midi")

    for file in files:
        os.remove(f"{TEST_DIR}{os.path.basename(file)}")
