import os
import time
import webbrowser
import subprocess
from pytube import YouTube
from urllib.parse import quote_plus


def get_cb():
    result = subprocess.run(['pbpaste'], capture_output=True, text=True)
    return result.stdout.strip()


def cb_check(p_cb):
    while True:
        c_cb = get_cb()
        if c_cb != p_cb:
            return c_cb
        time.sleep(0.5)


def search_on_yt(keyword):
    base_url = "https://www.youtube.com/results?search_query="
    query = quote_plus(keyword)
    return base_url + query


def dc_audio(url, filename):
    yt = YouTube(url)
    v_stream = yt.streams.filter(only_audio=True).first()
    v_path = v_stream.download()
    m_path = os.path.join(os.path.dirname(v_path), f"{filename}.mp3")
    os.rename(v_path, m_path)
    return m_path


name = input("암호를 입력하세요: ")
search_query = search_on_yt(name)
previous_cb = get_cb()

webbrowser.open(search_query)
current_cb = cb_check(previous_cb)
os.system("killall -9 'Safari'")

dc_audio(current_cb, name)
