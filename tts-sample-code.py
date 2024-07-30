from tortoise.api import TextToSpeech
import soundfile as sf


def save_pcm_to_wav(pcm_data, sample_rate, file_path):
    """
    儲存 PCM 音訊資料為 WAV 檔案。

    參數:
    pcm_data (bytes): PCM 音訊數據
    sample_rate (int): 音訊的取樣率
    file_path (str): 儲存 WAV 檔案的路徑
    """
    audio_data = pcm_data.squeeze().numpy()
    sf.write(file_path, audio_data, sample_rate)
    print(f"音訊已儲存為 {file_path}")


# 初始化TTS模型
tts = TextToSpeech(use_deepspeed=True, kv_cache=True, half=True)  # use_deepspeed=True, kv_cache=True, half=True 加快運行速度

# 定義要轉換的文字
text = "你好，歡迎使用產生高品質的語音。"
text = "hello, HAHAHA, today is sunny day"

# 生成語音
pcm_audio = tts.tts_with_preset(text, preset='ultra_fast')
print(pcm_audio)

# 儲存產生的語音為wav文件
sample_rate = 24000
file_path = 'output.wav'

save_pcm_to_wav(pcm_audio, sample_rate, file_path)
print("語音生成完成，檔案儲存為 output.wav")
