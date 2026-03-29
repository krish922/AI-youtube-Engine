from src.pipeline import run_pipeline

topic, script, audio, video = run_pipeline()

print("Topic:\n", topic)
print("Video Created Successfully!:", video)