import sounddevice as sd

def main():
    audio_devices = list()
    host_apis = sd.query_hostapis()
    
    for index, device in enumerate(sd.query_devices()):
        device_name = device['name'] + ", " + host_apis[device['hostapi']]['name']
        
        isInOut = ""
        if device['max_input_channels'] > 0:
            isInOut += "入"
        
        if device['max_output_channels'] > 0:
            isInOut += "出"
        
        audio_devices.append(f'{isInOut}力： Index：{index} デバイス名："{device_name}"\n')

    with open('audio_device_list.txt', 'w', encoding='utf-8') as f:
        f.writelines(audio_devices)

    print(" 使用可能なデバイス一覧の取得が完了しました。\n audio_device_list.txt を参照してください。\n このウィンドウは閉じて問題ありません。")

if __name__ == '__main__':
    main()