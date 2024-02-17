import requests
import execjs
import time

word = input('请输入需要翻译的内容:')
url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'

with open('baidu.js', encoding='utf-8') as js:
    js_content = js.read()
    compile = execjs.compile(js_content)
    sign = compile.call('get_sign', word)
ts = int(round(time.time() * 1000))
print(ts)
cookies = {
    'BIDUPSID': '1C6C00AAB415EBC71A53E105000D70BA',
    'PSTM': '1682770137',
    'BAIDUID': 'D8AFC62FB2EBF1D08C9AF78D2E32D0F9:FG=1',
    'REALTIME_TRANS_SWITCH': '1',
    'FANYI_WORD_SWITCH': '1',
    'HISTORY_SWITCH': '1',
    'SOUND_SPD_SWITCH': '1',
    'SOUND_PREFER_SWITCH': '1',
    'BDUSS': 'w4ajgtcHltZHRlWEMyU081emNnVVJobDhMLVdyYWFuVTZuV1JqR1UwbVlIamRsRVFBQUFBJCQAAAAAAAAAAAEAAACGb3ePwMvX0830z8zT4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJiRD2WYkQ9lTU',
    'BDUSS_BFESS': 'w4ajgtcHltZHRlWEMyU081emNnVVJobDhMLVdyYWFuVTZuV1JqR1UwbVlIamRsRVFBQUFBJCQAAAAAAAAAAAEAAACGb3ePwMvX0830z8zT4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJiRD2WYkQ9lTU',
    'H_WISE_SIDS_BFESS': '40016_40044',
    'H_WISE_SIDS': '40125_39996_40170_39662_40207_40211_40216',
    'H_PS_PSSID': '40125_39996_40170_39662_40207_40211_40216',
    'APPGUIDE_10_6_9': '1',
    'BA_HECTOR': 'a4a50020a40h00810h84242gti7n0o1it18jl1t',
    'ZFY': '7uUjPQx:AFg8WwLwx:Bl78Kg0ztvHw1pHC9hFfCsXa:A8k:C',
    'BAIDUID_BFESS': 'D8AFC62FB2EBF1D08C9AF78D2E32D0F9:FG=1',
    'delPer': '0',
    'PSINO': '2',
    'BDRCVFR[E-fQi7m9KnT]': '5AxZxS6heqDpvVzThm8mvqV',
    'BDORZ': 'FFFB88E999055A3F8A630C64834BD6D0',
    'Hm_lvt_64ecd82404c51e03dc91cb9e8c025574': '1706369202,1708177565',
    'Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574': '1708177927',
    'ab_sr': '1.0.1_MjY2NzE5MzJkN2UxYTJkNDQ0NzRiM2MzNGRjYTc2NTUxNzhiNDdmODEwNDQwZjcwOTBmNjE4MmFmZTEwOTJhZDI2ODM0M2FmYWIwMjI5ZjdjMjI4OTdiYTQ5ZTI3OWM5YjlkYjA4NzQzNTQ0OTM4NWQ3ZmVmOTg5ZmExZjE4ZWU0NTQ4Y2VlOThhZTFiNzFhNDY5OGFlMzIwNDZmMjc0NDFiN2VmN2YzMGZhZDRhMWUxZjZiNTZhYjgzYjk1YjBm',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Acs-Token': '1708171204432_1708179569658_aq2Qw40hj3rAzq1mh/1MajlqycWBYd2w9APQxEMmWgbHbxO1+mUJEQb9HZmUYhHHNn7fGI4bWpK+OBMV6EaXUdDITXOCPu0PHjAFymAedhxaHQFrx8Mw47KJe73Y43JvQQM/DaW2hlhbqAr/z4gQjuxcFnwtDl7gbWlGW7n7RJs4s9eGQ/UNGtQSWFlmzFzJe3PofFeruGYiS7N7m/sq8rVCo2Pu7ehJvQzi8D2Fdqi1ycw7+gyhlgHHC2cLV6/6Il2RF9Za2plieJoFhvf1QVIvuA9atZKoLYBoGn2byMwIKsObihRglrUzo4+M9LU3e+8/zYmFl2eZteypgj9Cg+lt2QjQWkY0jEzcYDyMOy/EUOcLOwf9dCslOTpsdc6nklRCayrJhomsaG/iDDJ5wI4b61gEQT8j3DyERU7jww2h4/EQVCNjtn661o9OoCLEOFUR9rPRsktwPyqUc/GqMqf7vb4uu4GdzV6O+u39dxU=',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'BIDUPSID=1C6C00AAB415EBC71A53E105000D70BA; PSTM=1682770137; BAIDUID=D8AFC62FB2EBF1D08C9AF78D2E32D0F9:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=w4ajgtcHltZHRlWEMyU081emNnVVJobDhMLVdyYWFuVTZuV1JqR1UwbVlIamRsRVFBQUFBJCQAAAAAAAAAAAEAAACGb3ePwMvX0830z8zT4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJiRD2WYkQ9lTU; BDUSS_BFESS=w4ajgtcHltZHRlWEMyU081emNnVVJobDhMLVdyYWFuVTZuV1JqR1UwbVlIamRsRVFBQUFBJCQAAAAAAAAAAAEAAACGb3ePwMvX0830z8zT4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJiRD2WYkQ9lTU; H_WISE_SIDS_BFESS=40016_40044; H_WISE_SIDS=40125_39996_40170_39662_40207_40211_40216; H_PS_PSSID=40125_39996_40170_39662_40207_40211_40216; APPGUIDE_10_6_9=1; BA_HECTOR=a4a50020a40h00810h84242gti7n0o1it18jl1t; ZFY=7uUjPQx:AFg8WwLwx:Bl78Kg0ztvHw1pHC9hFfCsXa:A8k:C; BAIDUID_BFESS=D8AFC62FB2EBF1D08C9AF78D2E32D0F9:FG=1; delPer=0; PSINO=2; BDRCVFR[E-fQi7m9KnT]=5AxZxS6heqDpvVzThm8mvqV; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1706369202,1708177565; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1708177927; ab_sr=1.0.1_MjY2NzE5MzJkN2UxYTJkNDQ0NzRiM2MzNGRjYTc2NTUxNzhiNDdmODEwNDQwZjcwOTBmNjE4MmFmZTEwOTJhZDI2ODM0M2FmYWIwMjI5ZjdjMjI4OTdiYTQ5ZTI3OWM5YjlkYjA4NzQzNTQ0OTM4NWQ3ZmVmOTg5ZmExZjE4ZWU0NTQ4Y2VlOThhZTFiNzFhNDY5OGFlMzIwNDZmMjc0NDFiN2VmN2YzMGZhZDRhMWUxZjZiNTZhYjgzYjk1YjBm',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh&ext_channel=Aldtype',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'from': 'zh',
    'to': 'en',
}

data = {
    'from': 'zh',
    'to': 'en',
    'query': word,
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': sign,
    'token': 'ba4d5a907fe58ed48679210bb16fb698',
    'domain': 'common',
    'ts': '1708179569640',
}
response = requests.post('https://fanyi.baidu.com/v2transapi', params=params, cookies=cookies, headers=headers, data=data)

print(response.json())
dst = response.json()['trans_result']['data'][0]['dst']
print(dst)