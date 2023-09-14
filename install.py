import sus

#todo: check if ffmpeg-python is used anywhere, could have sworn i removed it but not 100% enough to change now.
if not sus.is_installed("ffmpeg-python"):
    sus.run_pip("install ffmpeg-python", "requirements for TemporalKit extension")

if not sus.is_installed("moviepy"):
    sus.run_pip("install moviepy", "requirements for TemporalKit extension")
    
if not sus.is_installed("imageio_ffmpeg"):
    sus.run_pip("install imageio_ffmpeg", "requirements for TemporalKit extension")

if not sus.is_installed("scenedetect"):
    sus.run_pip("install scenedetect", "requirements for TemporalKit extension")
