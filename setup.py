import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deepspeech-pipeline", # Replace with your own username
    version="0.0.1",
    author="Kejiong Li",
    author_email="kejiong.li@gmail.com",
    description="Build pipeline for multichannel audio S2T JSON transcription and the expected JSON output",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kejiongli/deepspeech-pipeline",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)