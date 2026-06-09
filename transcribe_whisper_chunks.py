from pathlib import Path
import json
import sys

import whisper


CHUNKS_DIR = Path("audio_chunks_16-04-2026_15.01")
OUTPUT_STEM = Path("16-04-2026 15.01.transcription")
CHUNK_SECONDS = 300.0


def srt_timestamp(seconds):
    milliseconds = int(round(seconds * 1000))
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    seconds, milliseconds = divmod(remainder, 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"


def vtt_timestamp(seconds):
    return srt_timestamp(seconds).replace(",", ".")


def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else None
    chunks = sorted(CHUNKS_DIR.glob("chunk_*.mp3"))
    if limit is not None:
        chunks = chunks[:limit]
    if not chunks:
        raise SystemExit(f"No chunks found in {CHUNKS_DIR}")

    model = whisper.load_model("tiny")

    txt_path = OUTPUT_STEM.with_suffix(".txt")
    md_path = OUTPUT_STEM.with_suffix(".md")
    srt_path = OUTPUT_STEM.with_suffix(".srt")
    vtt_path = OUTPUT_STEM.with_suffix(".vtt")
    json_path = OUTPUT_STEM.with_suffix(".json")

    all_segments = []
    srt_index = 1

    with txt_path.open("w", encoding="utf-8") as txt_file, \
            md_path.open("w", encoding="utf-8") as md_file, \
            srt_path.open("w", encoding="utf-8") as srt_file, \
            vtt_path.open("w", encoding="utf-8") as vtt_file:
        md_file.write("# Trascrizione - 16-04-2026 15.01.mp3\n\n")
        md_file.write("Modello: OpenAI Whisper tiny, lingua italiana, audio diviso in chunk da 5 minuti.\n\n")
        vtt_file.write("WEBVTT\n\n")

        for chunk_index, chunk_path in enumerate(chunks):
            offset = chunk_index * CHUNK_SECONDS
            print(f"Processing {chunk_path.name} at offset {vtt_timestamp(offset)}", flush=True)
            result = model.transcribe(
                str(chunk_path),
                language="it",
                task="transcribe",
                fp16=False,
                verbose=False,
                condition_on_previous_text=False,
            )

            for segment in result.get("segments", []):
                start = offset + float(segment["start"])
                end = offset + float(segment["end"])
                text = segment["text"].strip()
                if not text:
                    continue

                all_segments.append({"start": start, "end": end, "text": text})
                line = f"[{vtt_timestamp(start)} --> {vtt_timestamp(end)}] {text}"
                print(line, flush=True)

                txt_file.write(line + "\n")
                txt_file.flush()

                md_file.write(f"**{vtt_timestamp(start)} - {vtt_timestamp(end)}**  \n{text}\n\n")
                md_file.flush()

                srt_file.write(f"{srt_index}\n{srt_timestamp(start)} --> {srt_timestamp(end)}\n{text}\n\n")
                srt_file.flush()

                vtt_file.write(f"{vtt_timestamp(start)} --> {vtt_timestamp(end)}\n{text}\n\n")
                vtt_file.flush()
                srt_index += 1

    json_path.write_text(json.dumps({"segments": all_segments}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Done: {txt_path}, {md_path}, {srt_path}, {vtt_path}, {json_path}", flush=True)


if __name__ == "__main__":
    main()