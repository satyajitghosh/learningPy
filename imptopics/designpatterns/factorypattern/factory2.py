# The main purpose of the factory pattern is to separate creation of an object from it's usage.
# Separation of the creation and the usage leads to abstraction and reduces coupling.
# This file shows the code before te application of the factory design pattern.
# The main function currently has the logic for creating the objects of the appropriate video and audio
# exporter classes depending on the export quality received as input from the user.
# The idea is to move this logic to a factory class that creates and returns an object of the relevant class.
# This way we achieve the first objective of separation of creation of an object from it's usage.
# Also important, is the fact that the main function currently needs to know about each of the 
# exporter classes, which increases coupling. We will reduce the same. 

"""
Basic video exporting example
"""

import pathlib
from abc import ABC, abstractmethod


class VideoExporter(ABC):
    """Basic representation of video exporting codec."""

    @abstractmethod
    def prepare_export(self, video_data):
        """Prepares video data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the video data to a folder."""


class LosslessVideoExporter(VideoExporter):
    """Lossless video exporting codec."""

    def prepare_export(self, video_data):
        print("Preparing video data for lossless export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in lossless format to {folder}.")


class H264BPVideoExporter(VideoExporter):
    """H.264 video exporting codec with Baseline profile."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Baseline) export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Baseline) format to {folder}.")


class H264Hi422PVideoExporter(VideoExporter):
    """H.264 video exporting codec with Hi422P profile (10-bit, 4:2:2 chroma sampling)."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Hi422P) export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Hi422P) format to {folder}.")


class AudioExporter(ABC):
    """Basic representation of audio exporting codec."""

    @abstractmethod
    def prepare_export(self, audio_data):
        """Prepares audio data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the audio data to a folder."""


class AACAudioExporter(AudioExporter):
    """AAC audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for AAC export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in AAC format to {folder}.")


class WAVAudioExporter(AudioExporter):
    """WAV (lossless) audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for WAV export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in WAV format to {folder}.")

class ExporterFactory(ABC):
    def get_video_exporter(self)->VideoExporter:
        pass
    def get_audio_exporter(self)->AudioExporter:
        pass

class FastExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return H264BPVideoExporter()
    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()

class HighQualityExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return H264Hi422PVideoExporter()
    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()
    
class MasterQualityExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return LosslessVideoExporter()
    def get_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()
    
def get_exporter_factory() -> ExporterFactory:

    factories = {
                    "low":FastExporter(),
                    "high":HighQualityExporter(),
                    "master":MasterQualityExporter()
                 }
    
    export_quality: str
    while True:
        export_quality = input("Enter desired output quality (low, high, master): ")
        if export_quality in factories:
            return factories[export_quality]
        print(f"Unknown output quality option: {export_quality}.")


def main() -> None:
    """Main function."""

    exporter_factory = get_exporter_factory()
    video_exporter = exporter_factory.get_video_exporter()
    audio_exporter = exporter_factory.get_audio_exporter()
    
    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")

    # do the export
    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    main()