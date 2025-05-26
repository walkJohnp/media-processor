import ffmpeg
# 视频处理

# 视频合并
def merge_video(video_list, output_video):
    """
    :param video_list: 视频列表
    :param output_video: 合并后的视频
    :return:
    """
    ffmpge.concat(video_list).output(output_video).run()



def clip_video(input_video, start_time, duration, output_video):
    (
        ffmpeg
        .input(input_video, ss=start_time, t=duration)  # 指定开始时间和裁剪时长
        .output(output_video, c='copy')  # 输出并复制编码
        .run()  # 执行命令
    )