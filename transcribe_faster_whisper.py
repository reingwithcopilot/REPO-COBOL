from pathlib import Path
import json

from faster_whisper import WhisperModel


AUDIO_PATH = Path("16-04-2026 15.01.mp3")
OUTPUT_STEM = AUDIO_PATH.with_suffix("")


def srt_timestamp(seconds):
    milliseconds = int(round(seconds * 1000))
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    seconds, milliseconds = divmod(remainder, 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"


def vtt_timestamp(seconds):
    return srt_timestamp(seconds).replace(",", ".")


def main():
    model = WhisperModel("base", device="cpu", compute_type="int8")
    segments, info = model.transcribe(
        str(AUDIO_PATH),
        language="it",
        task="transcribe",
        beam_size=1,
        vad_filter=True,
        initial_prompt="Trascrizione di una conversazione tecnica in italiano su INAIL, Power BI, Qlik, Access, controllo direzionale e progetti.",
    )

    metadata = {
        "audio": str(AUDIO_PATH),
        "language": info.language,
        "language_probability": info.language_probability,
        "duration": info.duration,
        "model": "base",
        "device": "cpu",
        "compute_type": "int8",
    }

    txt_path = OUTPUT_STEM.with_suffix(".faster.txt")
    md_path = OUTPUT_STEM.with_suffix(".faster.md")
    srt_path = OUTPUT_STEM.with_suffix(".faster.srt")
    vtt_path = OUTPUT_STEM.with_suffix(".faster.vtt")
    json_path = OUTPUT_STEM.with_suffix(".faster.json")

    all_segments = []
    with txt_path.open("w", encoding="utf-8") as txt_file, \
            md_path.open("w", encoding="utf-8") as md_file, \
            srt_path.open("w", encoding="utf-8") as srt_file, \
            vtt_path.open("w", encoding="utf-8") as vtt_file:
        md_file.write(f"# Trascrizione - {AUDIO_PATH.name}\n\n")
        md_file.write(f"- Lingua rilevata: {info.language} ({info.language_probability:.2f})\n")
        md_file.write(f"- Durata audio: {info.duration:.2f} secondi\n")
        md_file.write("- Modello: faster-whisper base, CPU int8\n\n")
        vtt_file.write("WEBVTT\n\n")

        for index, segment in enumerate(segments, start=1):
            text = segment.text.strip()
            all_segments.append({"start": segment.start, "end": segment.end, "text": text})

            line = f"[{vtt_timestamp(segment.start)} --> {vtt_timestamp(segment.end)}] {text}"
            print(line, flush=True)
            txt_file.write(line + "\n")
            txt_file.flush()

            md_file.write(f"**{vtt_timestamp(segment.start)} - {vtt_timestamp(segment.end)}**  \n{text}\n\n")
            md_file.flush()

            srt_file.write(f"{index}\n{srt_timestamp(segment.start)} --> {srt_timestamp(segment.end)}\n{text}\n\n")
            srt_file.flush()

            vtt_file.write(f"{vtt_timestamp(segment.start)} --> {vtt_timestamp(segment.end)}\n{text}\n\n")
            vtt_file.flush()

    json_path.write_text(json.dumps({"metadata": metadata, "segments": all_segments}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Done: {txt_path}, {md_path}, {srt_path}, {vtt_path}, {json_path}", flush=True)


if __name__ == "__main__":
    main()