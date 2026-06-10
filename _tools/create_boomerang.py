from moviepy import VideoFileClip, concatenate_videoclips, vfx

input_path = "assets/videos/Blue_glass_logo_rotating_202605071816 (1).mp4"
output_path = "assets/videos/boomerang.mp4"

video = VideoFileClip(input_path)
D = video.duration
t30 = D * (30.0 / 360.0)

clip_r_fwd = video.subclipped(0, t30)
clip_r_bwd = clip_r_fwd.with_effects([vfx.TimeMirror()])

clip_l_fwd = video.subclipped(D - t30, D)
clip_l_bwd = clip_l_fwd.with_effects([vfx.TimeMirror()])

# Sequence: Center -> Right -> Center -> Left -> Center
# Since clip_l_fwd is Left -> Center, its reverse (clip_l_bwd) is Center -> Left
final_clip = concatenate_videoclips([clip_r_fwd, clip_r_bwd, clip_l_bwd, clip_l_fwd])

final_clip.write_videofile(output_path, codec="libx264", audio=False, preset="fast")
