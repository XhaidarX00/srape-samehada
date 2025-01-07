# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import re
from itemadapter import ItemAdapter


class ScrapesamehadaPipeline:
    def process_item(self, item, spider):
        pass
        # adapter = ItemAdapter(item)
        # field_names = adapter.field_names()
        # for field_name in field_names:
        
        
        # for field_name in field_names:
        #     if field_name in ['detail', 'listeps']:
        #         item_ = adapter.get(field_name)
        #         new_dict = {}
        #         try:
        #             for key, value in item_.items():
        #                 new_dict[str(key).strip()] = str(value).strip()
        #                 print(f'*****{field_name}*****')
        #                 print(key)
        #                 print(value)
        #                 print('*'*10)
        #             adapter[field_name] = new_dict
        #         except:
        #             pass
                
        #     elif field_name == 'title':
        #         try:
        #             value = adapter.get(field_name)
        #             adapter[field_name] = value.strip()
        #         except:
        #             pass
        
        


from .items import AnimeEps, AnimesItems
from itemadapter import ItemAdapter

import json
from scrapy.exceptions import DropItem


class sortedData:
    def sorted_(self, data):
        sorted_data = sorted(data, key=lambda x: x['index'])
        return sorted_data
        
    def dataSorted(self, dataTitle, dataEps):
        temp_title = []
        temp_episode = []
        for item in dataTitle:
            if item not in temp_title:
                temp_title.append(item)
        
        temp_main = {}
        for eindex, eps in enumerate(temp_episode):
            for tindex, title in enumerate(temp_title):
                print('-'*30)
                print(f'Title dari Title {title['title'].strip()}')
                print(f'Title dari Episode {eps['title'].strip()}')
                print('-'*30)
                if title['title'].strip() == eps['title'].strip():
                    print(f'Titel sama nih {title['title'].strip()}')
                    if title['title'] not in temp_main:
                        temp_main[title['title']] = [
                                temp_title[tindex],
                                temp_episode[eindex],
                            ]
                    else:
                        temp_main[title['title']].append(temp_episode[eindex])
        
        data_sorted = None
        for key, value in temp_main.items():
            data_sorted = self.sorted_(value[1:])
            data_sorted = [value[0]] + data_sorted
        
        return data_sorted
    
        # return temp_main
        # text = ''
        # for key, value in temp_main.items():
        #     text += "*"*16 + 'Key' + '*'*16 + '\n'
        #     text += key + '\n'
        #     text += "-"*35 +'\n'
        #     data_sorted = sorted_(value[1:])
        #     data_sorted = [value[0]] + data_sorted
        #     for index, data in enumerate(data_sorted):
        #         text += f'{index + 1} {data}\n'
        #     text += "*"*35 +'\n\n'
            
        #     print(text)

sorted_data = sortedData()


class AnimePipeline:
    def __init__(self):
        self.anime_items = []
        self.anime_eps = []
    
    def sorted_(self, data):
        sorted_data = sorted(data, key=lambda x: x['index'])
        return sorted_data
    
    def cleanName(self, name_title, name_episode):
        name_title = name_title.split('Detail Anime')[1].strip().lower()
        name_episode = name_episode.split('Episode')[0].strip().lower()
        if name_episode == name_title:
            return True
        else:
            return False
        
    def dataSorted(self, dataTitle, dataEps):
        # temp_title = []
        # temp_episode = []
        # for item in dataTitle:
        #     if item not in temp_title:
        #         temp_title.append(item)
        try: 
            temp_main = {}
            for eindex, eps in enumerate(dataEps):
                for tindex, title in enumerate(dataTitle):
                    # print('-'*30)
                    # print(f'Title dari Title {title['title'].strip()}')
                    # print(f'Title dari Episode {eps['title'].strip()}')
                    # print('-'*30)
                    try:
                        if self.cleanName(title['title'], eps['title']):
                            # print(f'Titel sama nih {title['title'].strip()}')
                            if title['title'] not in temp_main:
                                temp_main[title['title']] = [
                                        dataTitle[tindex],
                                        dataEps[eindex],
                                    ]
                            else:
                                temp_main[title['title']].append(dataEps[eindex])
                    except:
                        pass
            
            data_sorted = None
            for key, value in temp_main.items():
                data_sorted = self.sorted_(value[1:])
                data_sorted = [value[0]] + data_sorted
            
            return data_sorted
        except:
            return None

    def process_item(self, item, spider):
        if isinstance(item, AnimesItems):
            self.anime_items.append(dict(item))
            raise DropItem()  # Tidak simpan item langsung ke file agar hasil olahan yang disimpan
        elif isinstance(item, AnimeEps):
            if 'episodes' in item:
                self.anime_eps.append(dict(item['episodes'])) if item['episodes'] else None
                raise DropItem()  # Tidak simpan item langsung ke file agar hasil olahan yang disimpan
            else: 
                pass
            
        return item

    def close_spider(self, spider):
        # print('-'*30)
        # print(f'Anime Eps {self.anime_eps}')
        # print(f'Anime Detail {self.anime_items}')
        # print('-'*30)
        # combined_data = self.anime_items + self.anime_eps
        # Jalankan fungsi main pada data yang digabungkan
        result = self.dataSorted(self.anime_items, self.anime_eps)
        # print('-'*30)
        # print(f'Result pipelines : {result}')
        # print('-'*30)
        if result is not None:
            # Simpan hasil olahan ke file JSON
            with open('animesTest.json', 'w') as f:
                json.dump(result, f, indent=4)



# class AnimePipeline:
#     def __init__(self):
#         self.current_title = None  # Menyimpan title dari AnimesItems

#     def process_item(self, item, spider):
#         adapter = ItemAdapter(item)

#         if isinstance(item, AnimesItems):
#             # Proses AnimesItems
#             self.process_animes_item(adapter)

#         elif isinstance(item, AnimeEps):
#             # Proses AnimeEps
#             self.process_anime_eps(adapter)

#         return item

#     def process_animes_item(self, adapter):
#         # Ambil dan simpan title dari AnimesItems
#         self.current_title = adapter.get('title')
#         detail = adapter.get('detail')
#         print(f"Processing Anime Item: {self.current_title}")
#         # Lakukan operasi lain yang diperlukan, seperti menyimpan ke database
    
#     def process_anime_eps(self, adapter):
#         # Gunakan title yang disimpan di process_animes_item
#         listeps = adapter.get('listeps')
#         print(f"Processing Anime Episodes for {self.current_title}: {len(listeps)} episodes found")
#         # Lakukan operasi lain yang diperlukan, seperti menyimpan ke database
#         sorted_animes = self.sort_listeps(listeps=listeps)
#         adapter['listeps'] = sorted_animes
        
        
#     def extract_episode_number(self, title):
#         # Ekstrak nomor episode dari title menggunakan regex
#         match = re.search(r'Episode (\d+)', title)
#         if match:
#             return int(match.group(1))
#         return 0

#     def sort_listeps(self, listeps):
#         # Urutkan keys dalam dictionary berdasarkan nomor episode
#         sorted_keys = sorted(listeps.keys(), key=lambda title: self.extract_episode_number(title))
#         # Buat dictionary baru yang diurutkan
#         sorted_listeps = {key: listeps[key] for key in sorted_keys}
#         return sorted_listeps