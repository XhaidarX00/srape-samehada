data = [
    {'index': 0, 'category': 'buah'},
    {'index': 5, 'category': 'buah' },
    {'title': 'hewan'},
    {'index': 2, 'category': 'buah' },
    {'index': 6, 'category': 'buah' },
    {'index': 3, 'category': 'buah' },
    {'index': 1, 'category': 'buah' },
    {'index': 0, 'category': 'hewan'},
    {'index': 5, 'category': 'hewan' },
    {'index': 2, 'category': 'hewan' },
    {'index': 6, 'category': 'hewan' },
    {'title': 'buah'},
    {'index': 3, 'category': 'hewan' },
    {'index': 1, 'category': 'hewan' },
]


def sorted_(data):
    sorted_data = sorted(data, key=lambda x: x['index'])
    return sorted_data
    
# def main(data):
#     temp_title = []
#     temp_episode = []
#     for item in data:
#         if 'title' in item:
#             temp_title.append(item)
#         else:
#             temp_episode.append(item)
    
#     # print(temp_episode[1])
#     # print(temp_title[1])
#     # return
#     temp_main = {}
#     for eindex, eps in enumerate(temp_episode):
#         for tindex, title in enumerate(temp_title):
#             if title['title'] == eps['category']:
#                 if title['title'] not in temp_main:
#                     temp_main[title['title']] = [
#                             temp_title[tindex],
#                             temp_episode[eindex],
#                         ]
#                 else:
#                     temp_main[title['title']].append(temp_episode[eindex])
#     # print(temp_main['buah'])
#     # return
#     text = ''
#     for key, value in temp_main.items():
#         text += "*"*16 + 'Key' + '*'*16 + '\n'
#         text += key + '\n'
#         text += "-"*35 +'\n'
#         data_sorted = sorted_(value[1:])
#         data_sorted = [value[0]] + data_sorted
#         for index, data in enumerate(data_sorted):
#             text += f'{index + 1} {data}\n'
#         text += "*"*35 +'\n\n'
        
#         print(text)


def main():
    name_title = "Title dari Title Detail Anime 100-man no Inochi no Ue ni Ore wa Tatteiru 2nd Season"
    name_episode = "100-man no Inochi no Ue ni Ore wa Tatteiru 2nd Season Episode 12 [END]"
    name_title = name_title.split('Detail Anime')[1].strip().lower()
    name_episode = name_episode.split('Episode')[0].strip().lower()
    
    if name_episode == name_title:
        print('Kata Sama')
    else:
        print('Kata Tidak Sama')

if __name__ == "__main__":
    main()




# data = [
#     {'title': 'buah - buahan'},
#     {'index': 0, 'buah': 'pisang'},
#     {'index': 5, 'buah': 'nanas' },
#     {'index': 2, 'buah': 'semangka' },
#     {'index': 6, 'buah': 'strawbery' },
#     {'index': 3, 'buah': 'melon' },
#     {'index': 1, 'buah': 'kopi' },
#     {'title': 'para hewan'},
#     {'index': 0, 'hewan': 'ayam'},
#     {'index': 5, 'hewan': 'sapi' },
#     {'index': 2, 'hewan': 'anjing' },
#     {'index': 6, 'hewan': 'kangguru' },
#     {'index': 3, 'hewan': 'burung' },
#     {'index': 1, 'hewan': 'trex' },
# ]

# def main():
#     # Memisahkan data buah dan hewan
#     buah_data = [item for item in data if 'buah' in item]
#     hewan_data = [item for item in data if 'hewan' in item]

#     # Mengurutkan data berdasarkan nilai 'index'
#     sorted_buah = sorted(buah_data, key=lambda x: x['index'])
#     sorted_hewan = sorted(hewan_data, key=lambda x: x['index'])

#     # Menggabungkan hasil urutan buah dan hewan
#     sorted_data = sorted_buah + sorted_hewan

#     # Menampilkan hasil
#     for item in sorted_data:
#         print(item)

# if __name__ == "__main__":
#     main()








# path = 'SamehadaScrape/scrapesamehada/spiders/animes.json'
# import json
# import re

# def sort_listeps(data):
#     sorted_data = sorted(data, key=extract_episode_number)
#     return sorted_data

# def extract_episode_number(item):
#         # match = re.search(r'Episode (\d+)', item['title'])
#         match = re.search(r'Episode (\d+)', item['title'])
#         return int(match.group(1)) if match else 0


# def main():
#     # Membaca data JSON dari file dengan encoding UTF-8
#     with open(path, 'r', encoding='utf-8') as file:
#         data = json.load(file)
#     # data = [{'title':'100-man no Inochi no Ue ni Ore wa Tatteiru 2nd Season Episode 1'}, {'title':'100-man no Inochi no Ue ni Ore wa Tatteiru 2nd Season Episode 10'}, {'title':'100-man no Inochi no Ue ni Ore wa Tatteiru 2nd Season Episode 11'}, {'title':'100-man no Inochi no Ue ni Ore wa Tatteiru 2nd Season Episode 12 [END]'}, {'title':'100-man no Inochi no Ue ni Ore wa Tatteiru 2nd Season Episode 2'}, {'title':'100-man no Inochi no Ue ni Ore wa Tatteiru 2nd Season Episode 3'}, {'title':'100-man no Inochi no Ue ni Ore wa Tatteiru 2nd Season Episode 4'}, {'title':'100-man no Inochi no Ue ni Ore wa Tatteiru 2nd Season Episode 5'}, {'title':'100-man no Inochi no Ue ni Ore wa Tatteiru 2nd Season Episode 6'}, {'title':'100-man no Inochi no Ue ni Ore wa Tatteiru 2nd Season Episode 7'}, {'title':'100-man no Inochi no Ue ni Ore wa Tatteiru 2nd Season Episode 8'}, {'title':'100-man no Inochi no Ue ni Ore wa Tatteiru 2nd Season Episode 9'}]

#     # Mengurutkan data berdasarkan nomor episode
#     for entry in data:
#         if 'listeps' in entry:
#             for key, value in entry.items():
#                 for key_, value_ in value.items():
#                     sorted_data = sort_listeps(value)

#     # Menampilkan hasil
#     for episode in sorted_data:
#         print(episode)
    
    # Memeriksa dan mengurutkan setiap entry yang memiliki 'listeps'
    # data_name = []
    # for entry in data:
    #     if 'listeps' in entry:
    #         for key, value in entry.items():
    #             keys = [key for key in value.keys()]
    #             print(f'Adding Name {keys[0]}')
    #             data_name.append(keys[0])
                # data_name.append(extract_episode_number(keys[0]))
    
    # print(data_name)
    # print()
    # print(sorted(data_name))
    # # Menyimpan data yang telah diurutkan ke file baru
    # with open('sorted_data.json'}, 'w', encoding='utf-8') as file:
    #     json.dump(data, file, indent=4, ensure_ascii=False)

# if __name__ == "__main__":
#     main()

