import numpy as np
from scipy.io import wavfile

def verify_seal(file_path):
    
    try:
        fs, data = wavfile.read(file_path)
        
        
        n = len(data)
        f_values = np.fft.rfftfreq(n, 1/fs)
        fft_values = np.abs(np.fft.rfft(data))

        
        target_idx = np.argmin(np.abs(f_values - 19000))
        peak_strength = fft_values[target_idx]

        
        if peak_strength > 1e5: 
            print("✅ AUTHENTIC: Awaaz-Seal detected. This voice is verified.")
        else:
            print("❌ WARNING: No seal found. Potential AI-Generated Deepfake.")
            
    except Exception as e:
        print(f"Error: {e}. Ensure the file exists and is a valid .wav.")

