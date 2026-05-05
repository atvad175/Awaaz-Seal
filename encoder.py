import numpy as np
from scipy.io import wavfile

def inject_seal(input_file, output_file):
    
    try:
        
        fs, data = wavfile.read(input_file)
        
        
        if data.dtype != np.int16:
            data = (data / np.max(np.abs(data)) * 32767).astype(np.int16)

        
        duration = len(data) / fs
        t = np.linspace(0, duration, len(data))
        seal_freq = 19000  # 19kHz
        amplitude = 500    # Low volume for inaudibility
        seal = amplitude * np.sin(2 * np.pi * seal_freq * t)

        
        protected_data = data + seal.astype(np.int16)

        
        wavfile.write(output_file, fs, protected_data)
        print(f"Success! '{output_file}' is now protected with Awaaz-Seal.")
        
    except Exception as e:
        print(f"Error: {e}. Please ensure your file is a 16-bit .wav file.")

